import heapq  # 导入 heapq 模块，用于实现优先队列（最小堆），在 Dijkstra 算法中用来高效获取最小距离节点

n, m = map(int, input().split())  # 从输入中读取两个整数 n（节点数）和 m（基站数），用 map 将字符串转为整数
nodes = [tuple(map(int, input().split())) for _ in range(n)]  # 读取 n 行，每行两个整数表示节点坐标 (x, y)，存为元组列表
stations = [tuple(map(int, input().split())) for _ in range(m)]  # 读取 m 行，每行四个整数表示基站信息 (x, y, r, t)，存为元组列表

graph = [[] for _ in range(n)]  # 初始化图的邻接表，一个长度为 n 的列表，每个元素是一个空列表，用于存储节点间的边

for sx, sy, r, t in stations:  # 遍历每个基站，解包为坐标 (sx, sy)、半径 r 和延迟 t
    # 找到当前基站覆盖的节点
    covered = [i for i in range(n) if abs(nodes[i][0] - sx) <= r and abs(nodes[i][1] - sy) <= r]  # 用列表推导式找出被当前基站覆盖的节点索引 i，条件是节点坐标 (x, y) 在以 (sx, sy) 为中心、边长 2r 的正方形内
    # 两两连边
    for i in range(len(covered)):  # 遍历 covered 列表的索引 i
        for j in range(i + 1, len(covered)):  # 遍历从 i+1 到末尾的索引 j，避免重复连接同一对节点
            u, v = covered[i], covered[j]  # 获取两个节点编号 u 和 v
            graph[u].append((v, t))  # 在节点 u 的邻接表中添加边 (v, t)，表示 u 到 v 的延迟为 t
            graph[v].append((u, t))  # 在节点 v 的邻接表中添加边 (u, t)，表示 v 到 u 的延迟为 t（无向图）

# Dijkstra算法
dist = [float('inf')] * n  # 初始化距离数组 dist，长度为 n，所有元素设为无穷大，表示从起点到各节点的初始距离
dist[0] = 0  # 将起点（节点1，索引0）的距离设为 0，因为起点到自身的距离为 0
pq = [(0, 0)]  # 初始化优先队列 pq，存入元组 (距离, 节点)，初始元素为 (0, 0)，表示起点距离为 0，节点为 0

while pq:  # 当优先队列不为空时循环
    d, u = heapq.heappop(pq)  # 从优先队列中弹出当前距离最小的元素，解包为距离 d 和节点 u
    if d > dist[u]:  # 如果弹出的距离 d 大于当前记录的 dist[u]，说明 u 已通过更短路径处理过，跳过此次循环
        continue
    for v, t in graph[u]:  # 遍历节点 u 的所有邻接节点 v 及其对应的延迟 t
        if dist[u] + t < dist[v]:  # 如果通过 u 到 v 的新距离 (dist[u] + t) 小于当前记录的 dist[v]
            dist[v] = dist[u] + t  # 更新 v 的最短距离为新距离
            heapq.heappush(pq, (dist[v], v))  # 将更新后的 (距离, 节点) 加入优先队列，以便后续处理 v 的邻接节点

print(dist[n-1] if dist[n-1] != float('inf') else "Nan")  # 输出结果：如果 dist[n-1]（起点到终点的最短距离）不是无穷大，则打印该值；否则打印 "Nan"，表示无法到达