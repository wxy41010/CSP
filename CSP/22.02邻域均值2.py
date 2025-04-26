def solve_dark_pixels_optimized(n, L, r, t, A):
    # 构建积分图
    S = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(n):
            S[i + 1][j + 1] = S[i + 1][j] + S[i][j + 1] - S[i][j] + A[i][j]
    count = 0
    # 遍历每个像素
    for i in range(n):
        for j in range(n):
            # 计算邻域边界
            x_start = max(0, i - r)
            x_end = min(n - 1, i + r)
            y_start = max(0, j - r)
            y_end = min(n - 1, j + r)
            # 使用积分图计算邻域和
            area_sum = (S[x_end + 1][y_end + 1] -
                        S[x_end + 1][y_start] -
                        S[x_start][y_end + 1] +
                        S[x_start][y_start])
            # 通过邻域矩阵的长和宽 计算邻域像素数量
            neighbor_count = (x_end - x_start + 1) * (y_end - y_start + 1)
            # 计算平均值并判断
            avg = area_sum / neighbor_count
            if avg <= t:
                count += 1
    return count
n, L, r, t = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
result = solve_dark_pixels_optimized(n, L, r, t, A)
print(result)