n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# 将坐标转为集合，便于快速查找
points = set((x, y) for x, y in arr)
# 存储每种评分的选址个数
scores = [0] * 5  # 索引0-4对应评分0-4
# 检查每个点是否适合建回收站
for x, y in arr:
    # 条件1：上下左右4个邻居必须都有垃圾
    neighbors = [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]
    if all(p in points for p in neighbors):  # 所有邻居都存在
        # 条件2：计算对角4个位置的评分
        diagonals = [(x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)]
        score = sum(1 for p in diagonals if p in points)  # 统计对角垃圾点数
        scores[score] += 1
for s in scores:
    print(s)