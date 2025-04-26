n, X, Y = map(int, input().split())
points = []
for i in range(1, n + 1):
    x, y = map(int, input().split())
    dist = (X - x)**2 + (Y - y)**2  # 计算平方距离 可以不开方
    points.append((dist, i))  # 存储 (距离, 检测点编号)
points.sort() # 按 (距离, 编号) 排序
for i in range(3):# 输出前三个检测点编号
    print(points[i][1])

