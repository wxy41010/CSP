# 读取输入数据
n, m = map(int, input().split())  # 读取点的数量 n 和查询的数量 m
# 读取 n 个点的信息，每个点由 (x, y, type) 组成
points = [input().split() for _ in range(n)]
# 读取 m 个查询，每个查询是一条直线的参数 (θ0, θ1, θ2)
lines = [list(map(int, input().split())) for _ in range(m)]
# 遍历每条查询直线，检查是否能完美分隔 A、B 类点
for i in range(m):
    # 初始化计数变量
    # Aa: 直线上方的 A 类点数量
    # Ab: 直线上方的 B 类点数量
    # Ba: 直线下方的 A 类点数量
    # Bb: 直线下方的 B 类点数量
    Aa = Ab = Ba = Bb = 0
    # 遍历所有点，判断其相对于直线的位置
    for j in range(n):
        x, y, t = int(points[j][0]), int(points[j][1]), points[j][2]  # 解析点的坐标和类别
        # 计算点相对于直线的位置
        val = lines[i][0] + lines[i][1] * x + lines[i][2] * y
        if val > 0:  # 该点在直线的一侧
            if t == 'A':
                Aa += 1  # 记录 A 类点的数量
            else:
                Ab += 1  # 记录 B 类点的数量
        else:  # 该点在直线的另一侧
            if t == 'A':
                Ba += 1
            else:
                Bb += 1
    # 判定是否可以完美分隔 A、B 类点
    # 条件1: 直线一侧只有 A，另一侧只有 B（Aa 和 Bb 存在，Ab 和 Ba 为 0）
    # 条件2: 直线一侧只有 B，另一侧只有 A（Ab 和 Ba 存在，Aa 和 Bb 为 0）
    if (Aa == 0 and Bb == 0) or (Ab == 0 and Ba == 0):
        print("Yes")
    else:
        print("No")