def bag01(n, c, v):  # 定义一个函数 bag01，用于解决 0-1 背包问题，参数分别是物品数量 n、背包容量 c 和物品价值数组 v
    f = [[0]*(c+1) for _ in range(n+1)]  # 创建一个二维数组 f，大小为 (n+1) 行 (c+1) 列，初始化全为 0，用于存储动态规划的状态
    for i in range(1, n+1):  # 外层循环，从第 1 个物品到第 n 个物品，逐个考虑
        for j in range(1, c+1):  # 内层循环，背包容量从 1 到 c，尝试不同的容量限制
            if j < v[i-1]:  # 如果当前容量 j 小于第 i 个物品的价值（重量），无法放入
                f[i][j] = f[i-1][j]  # 不选第 i 个物品，结果等于前 i-1 个物品在容量 j 下的值
            else:  # 如果容量足够放入第 i 个物品
                f[i][j] = max(f[i-1][j], f[i-1][j-v[i-1]] + v[i-1])  # 比较不选和选的最大值：不选是 f[i-1][j]，选是 f[i-1][j-v[i-1]] + v[i-1]
    return f[n][c]  # 返回前 n 个物品在容量 c 下的最大价值

n, x = map(int, input().split())  # 从输入读取两个整数 n（书的总数）和 x（包邮门槛），用空格分隔
value = [int(input()) for _ in range(n)]  # 创建列表 value，读取 n 行输入，每行一个整数，表示每本书的价格
capacity = sum(value) - x  # 计算背包容量 capacity，即所有书总价减去包邮门槛，表示最多能删掉的价格
value_max = bag01(n, capacity, value)  # 调用 bag01 函数，计算在容量 capacity 下能删掉的最大价格，存入 value_max
ans = sum(value) - value_max  # 计算答案：所有书总价减去能删掉的最大价格，得到满足包邮条件的最小花费
print(ans)  # 输出答案，即满足 m ≥ x 的最小花费