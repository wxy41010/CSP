# 定义函数，计算可能的宝藏位置数量
def count_possible_treasure_locations(n, L, S, tree_positions, treasure_map):  # 参数：树的数量n，网格大小L，宝藏地图大小S，树的位置列表，宝藏地图
    grid = [[0] * (L + 1) for _ in range(L + 1)]  # 用二维列表表示网格，初始值全为0
    for x, y in tree_positions:  # 遍历每棵树的位置坐标 (x, y)
        grid[x][y] = 1  # 在网格对应位置标记为1，表示有树

    def matches(x, y):  # 参数：检查区域的左上角坐标 (x, y)
        for i in range(S + 1):  # 遍历宝藏地图的每一行（0到S）
            for j in range(S + 1):  # 遍历宝藏地图的每一列（0到S）
                if grid[x + i][y + j] != treasure_map[S - i][j]:  # 如果当前位置不匹配
                    return False  # 返回False，表示不匹配
        return True  # 所有位置都匹配，返回True

    count = 0  # 用于统计满足条件的宝藏位置数量，测试数据保证count > 0
    for x in range(L - S + 1):  # x范围：0到L-S，确保子区域不超出网格
        for y in range(L - S + 1):  # y范围：0到L-S，确保子区域不超出网格
            if grid[x][y] == 1 and matches(x, y):  # 如果当前位置有树且子区域匹配
                count += 1  # 计数器加1
    return count  # 返回满足条件的宝藏位置总数

n, L, S = map(int, input().split())  # 读取树的数量n，网格大小L，宝藏地图大小S，用空格分隔
tree_positions = [tuple(map(int, input().split())) for _ in range(n)]  # 读取n行，每行两个整数表示树的坐标，存为元组列表
treasure_map = [list(map(int, input().split())) for _ in range(S + 1)]  # 读取S+1行，每行S+1个整数表示宝藏地图，存为二维列表
result = count_possible_treasure_locations(n, L, S, tree_positions, treasure_map)  # 调用函数，传入参数计算宝藏位置数量
print(result)  # 输出可能的宝藏位置数量