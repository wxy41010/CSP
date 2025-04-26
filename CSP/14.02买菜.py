n = int(input())# 读取时间段数量
# 读取小H的时间段
H = [tuple(map(int, input().split())) for _ in range(n)]
# 读取小W的时间段
W = [tuple(map(int, input().split())) for _ in range(n)]
# 找到最大时间点
max_time = max(max(max(h) for h in H), max(max(w) for w in W))
# 创建时间线数组
HH = [0] * (max_time + 1)
WW = [0] * (max_time + 1)
for start, end in H: # 标记小H的时间段
    for t in range(start, end ):
        HH[t] = 1
for start, end in W: # 标记小W的时间段
    for t in range(start, end):
        WW[t] = 1
# 计算总聊天时间
total_chat_time = 0
for t in range(max_time + 1):
    if HH[t] == 1 and WW[t] == 1:
        total_chat_time += 1
print(total_chat_time)