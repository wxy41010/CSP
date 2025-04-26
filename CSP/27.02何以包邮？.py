n, x = map(int, input().split())
v = [int(input()) for _ in range(n)]  # 书的价格列表
# 计算所有书总和
total_sum = sum(v)
# 最多能删掉的价格（背包容量）
c = total_sum - x
# 动态规划：计算能删掉的最大总和
f = [[0] * (c + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, c + 1):
        if j < v[i-1]:  # 容量不够删第 i 本书
            f[i][j] = f[i-1][j]
        else:  # 比较不删和删的最大值
            f[i][j] = max(f[i-1][j], f[i-1][j - v[i-1]] + v[i-1])
# 结果：总和 - 能删掉的最大值
min_cost = total_sum - f[n][c]
print(min_cost)