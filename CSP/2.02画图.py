n = int(input())
grid = [[False] * 101 for _ in range(101)]  # 初始化101×101的网格
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):  # 注意：x2不包含
        for y in range(y1, y2):  # 注意：y2不包含
            grid[x][y] = True  # 标记被涂色的区域
# 统计被涂色的格子数
result=sum(sum(row)for row in grid)
print(result)

# 2
# 1 1 4 4
# 2 3 6 5

# 15
