# 读取输入的行数 n 和列数 m
n, m = map(int, input().split())
# 读取矩阵
matrix = [list(map(int, input().split())) for _ in range(n)]
# 创建一个新的 m × n 的矩阵用于存储旋转后的结果
temp = [[0] * n for _ in range(m)]
# 进行矩阵旋转操作
for i in range(n):  # 遍历原矩阵的每一行
    for j in range(m):  # 遍历原矩阵的每一列
        # 原矩阵第 i 行、第 j 列的元素 -> 新矩阵的第 (m - j - 1) 行，第 i 列
        temp[m - j - 1][i] = matrix[i][j]
for row in temp:
    print(*row)