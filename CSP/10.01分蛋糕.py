# 读取输入的 n（蛋糕数量）和 k（每个朋友至少要获得的重量）
n, k = map(int, input().split())
# 读取蛋糕重量，并存入列表
arr = list(map(int, input().split()))
# 记录分到蛋糕的朋友数量
ans = 0
# 记录当前朋友已分得的蛋糕总重量
count = 0
# 遍历所有蛋糕
for i in range(n):
    count += arr[i]  # 分配当前蛋糕
    # 如果当前朋友分到的蛋糕总重量 >= k，计入一个朋友，并重置计数
    if count >= k:
        ans += 1  # 朋友数量+1
        count = 0  # 重新开始计算下一个朋友的蛋糕重量
# 如果蛋糕分完后，仍然有未满 k 但已经开始分配的朋友，算作一个朋友
if count > 0:
    ans += 1
# 输出最终分到蛋糕的朋友数量
print(ans)

# 6 9
# 2 6 5 6 3 5

# 3