r, y, g = map(int, input().split())  # 红灯、黄灯、绿灯的最大倒计时
n = int(input())  # 道路段数
arr = [list(map(int, input().split())) for _ in range(n)]  # 交通灯信息
total_time=0
T=r+y+g
for i in range(n):
    k, t = arr[i]  # k是信号灯类型，t是倒计时或过路段的时间
    if k == 0:  # 过路段
        total_time += t
    elif k == 1:  # 红灯
        if t<=total_time %(T+t)<=g+t:
            total_time += 0
        elif total_time%(T+t)<t:
            total_time+=t
        elif total_time%(T+t)>g+t:
            total_time +=(T+t)-total_time%(T+t)
    elif k == 2:  # 黄灯
        if r+t<total_time %(T+t)<=r+g+t:
            total_time+=0
        elif total_time %(T+t)<=t or total_time %(T+t)>r+g+t:
            total_time+=t+r
        else:
            total_time+=r-total_time %(T+t)+t
    elif k == 3:  # 绿灯
        if total_time %(T+t)<=t:
            total_time+=t
        elif r+y+t<total_time%(T+t)<=T+t:
            total_time += 0  # 绿灯时直接通行，不需要等待
        elif t<total_time%(T+t)<=r+y+t:
            total_time += t+r+y-total_time
print(total_time)

