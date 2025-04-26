r, y, g = map(int, input().split())  # 红灯、黄灯、绿灯持续时间
n = int(input())  # 道路段数
arr = [list(map(int, input().split())) for _ in range(n)]
total_time = 0
cycle = r + g + y  # 总周期
for k, t in arr:
    if k == 0:  # 路段
        total_time += t
    else:
        remain = t - total_time % cycle  # 到达时的剩余时间
        if k == 1:  # 红灯
            total_time += remain if remain > 0 else (r - (-remain) % cycle if remain < -g else 0)
        elif k == 2:  # 黄灯
            total_time += remain + r if remain > 0 else (r - (-remain) % cycle if -r < remain <= 0 else r + y - (-remain) % cycle)
        elif k == 3:  # 绿灯
            total_time += 0 if remain > 0 or (y + r) <= (-remain) % cycle <= cycle else (y + r - (-remain) % cycle)
print(total_time)