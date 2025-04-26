r, y, g = map(int, input().split())  # 红灯、黄灯、绿灯的最大倒计时
n = int(input())  # 道路段数
arr = [list(map(int, input().split())) for _ in range(n)]  # 交通灯信息
total_time = 0  # 总时间
for i in range(n):
    k, t = arr[i]  # k是信号灯类型，t是倒计时或过路段的时间
    if k == 0:  # 过路段
        total_time += t
    elif k == 1:  # 红灯
        total_time += t  # 等待红灯倒计时的时间
    elif k == 2:  # 黄灯
        total_time += t+r  # 等待黄灯倒计时的时间要加上下一次的红灯时间
    elif k == 3:  # 绿灯
        total_time += 0  # 绿灯时直接通行，不需要等待
print(total_time)
