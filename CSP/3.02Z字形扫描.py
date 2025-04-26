n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
result = []
for k in range(2 * n - 1):  # k 代表对角线编号
    if k % 2 == 0:  # 偶数编号，对角线从左下到右上（↗）
        #起点[row,col]
        row = min(k, n - 1)  # 确保 row 不超过 n-1
        col = k - row
        while row >= 0 and col < n:
            result.append(matrix[row][col])
            row -= 1
            col += 1
    else:  # 奇数编号，对角线从右上到左下（↙）
        col = min(k, n - 1)
        row = k - col
        while col >= 0 and row < n:
            result.append(matrix[row][col])
            row += 1
            col -= 1
print(*result)

# 4
# 1  5  3  9
# 3  7  5  6
# 9  4  6  4
# 7  3  1  3

# 1 5 3 9 7 3 9 5 4 7 3 6 6 4 1 3
