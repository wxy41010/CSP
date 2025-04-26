import numpy as np  # 引入 NumPy 库

n, d = map(int, input().split())  # 读取矩阵大小，n 表示矩阵行数，d 表示列数

# 读取矩阵 Q, K, V，并转换为 NumPy 数组
Q = np.array([list(map(int, input().split())) for _ in range(n)])  # n 行 d 列的矩阵 Q
K = np.array([list(map(int, input().split())) for _ in range(n)])  # n 行 d 列的矩阵 K
V = np.array([list(map(int, input().split())) for _ in range(n)])  # n 行 d 列的矩阵 V

# 读取权重向量 W
W = list(map(int, input().split()))  # 读取 n 维向量 W

# 计算最终结果，逐行计算，避免存储 n x n 矩阵
result = [[0]*d for _ in range(n)]  # 初始化结果矩阵
for i in range(n):
    ans = Q[i] @ K.T  # 计算 QK_T 的第 i 行，即 Q[i] 和 K 的转置相乘
    ans *= W[i]  # 逐行乘以 W[i]，对应 Softmax 权重调整
    result[i] = ans @ V  # 计算最终结果，QK_T_row 乘以矩阵 V

# 输出结果，每行输出 d 个整数
for row in result:
    print(*row)  # 逐行打印计算结果

"""
3 2
1 2
3 4
5 6
10 10
-20 -20
30 30
6 5
4 3
2 1
4 0 -5

480 240
0 0
-2200 -1100
"""
#全部的测试数据满足：n≤10000且d≤20；输入矩阵、向量中的元素均为整数，且绝对值均不超过1000。
