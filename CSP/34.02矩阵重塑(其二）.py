import sys
# 读取输入
n, m, t = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(matrix)
for _ in range(t):
    arr = list(map(int, sys.stdin.readline().split()))
    if arr[0] == 1:  # 重塑操作
        p, q = arr[1], arr[2]
        flat = [num for row in matrix for num in row]  # 转为一维列表
        matrix = [flat[i * q:(i + 1) * q] for i in range(p)]  # 构造新矩阵
        n, m = p, q  # 更新当前矩阵的行列数
    elif arr[0] == 2:  # 转置操作
        matrix = [[matrix[j][i] for j in range(n)] for i in range(m)]  # 直接转置
        print(matrix)
        n, m = m, n  # 交换行列数
    elif arr[0] == 3:  # 查询操作
        i, j = arr[1], arr[2]
        print(matrix[i][j])
'''
3 2 3
1 2
3 4
5 6
3 0 1
1 2 3
3 1 2

2
6
'''