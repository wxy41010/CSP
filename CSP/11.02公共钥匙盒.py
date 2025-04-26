N, K = map(int, input().split())
y = list(range(1, N + 1))
events = []
for _ in range(K):
    w, s, c = map(int, input().split())
    events.append((s, 1, w))  # 取钥匙事件
    events.append((s + c, 0, w))  # 归还钥匙事件
events.sort()  # 按时间排序，时间相同则归还(0)优先
for time, event, key in events:
    if event:  # 取钥匙
        y[y.index(key)] = 0
    else:  # 归还钥匙
        y[y.index(0)] = key
print(*y)

# 5 2
# 4 3 3
# 2 2 7

# 1 4 3 2 5