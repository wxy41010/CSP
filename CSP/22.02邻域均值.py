def solve_dark_pixels(n, L, r, t, A):
    count = 0  # 计数器，记录处于较暗区域的像素数
    # 遍历矩阵每个像素
    for i in range(n):
        for j in range(n):
            # 计算邻域边界，防止超出矩阵范围
            x_start = max(0, i - r)  # 邻域上边界
            x_end = min(n, i + r + 1)  # 邻域下边界
            y_start = max(0, j - r)  # 邻域左边界
            y_end = min(n, j + r + 1)  # 邻域右边界
            # 计算邻域内的像素和与像素数量
            neighbor_sum = 0  # 邻域像素值总和
            neighbor_count = 0  # 邻域像素数量
            # 遍历邻域，计算总和
            for x in range(x_start, x_end):#对应上面的end值+1，因为取不到end
                for y in range(y_start, y_end):
                    neighbor_sum += A[x][y]
                    neighbor_count += 1
            # 计算邻域平均值
            avg = neighbor_sum / neighbor_count
            # 如果平均值小于等于阈值，计数加1
            if avg <= t:
                count += 1
    return count
n, L, r, t = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
result = solve_dark_pixels(n, L, r, t, A)
print(result)