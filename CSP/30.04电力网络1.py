from collections import defaultdict
from heapq import heappush, heappop

N, M, K = map(int, input().split())
money = [list(map(int, input().split())) for _ in range(N)]
graph = defaultdict(list)

for _ in range(M):
    l = list(map(int, input().split()))
    u, v = l[0], l[1]
    costs = l[2:]
    T = [[0] * K for _ in range(K)]
    for i in range(K):
        for j in range(K):
            T[i][j] = costs[i * K + j]  #端点i到j的造价  下面转置即为j到i的造价
    graph[u].append((v, T))
    graph[v].append((u, [[T[j][i] for j in range(K)] for i in range(K)]))

def prim_variant():
    dp = [[float('inf')] * K for _ in range(N)]  # dp[u][k]: u 选 k 的最小造价
    in_tree = [False] * N  # 标记节点是否加入
    chosen = [-1] * N  # 记录选择的地址
    pq = []  # 优先队列

    # 初始化节点 0
    for k in range(K):
        dp[0][k] = money[0][k]
        heappush(pq, (dp[0][k], 0, k))

    total_cost = 0
    while pq:
        cost, u, k = heappop(pq)
        if in_tree[u]:
            continue
        in_tree[u] = True
        chosen[u] = k
        total_cost += money[u][k]

        for v, T in graph[u]:
            if not in_tree[v]:
                for l in range(K):
                    new_cost = money[v][l] + T[k][l]
                    if new_cost < dp[v][l]:
                        dp[v][l] = new_cost
                        heappush(pq, (total_cost + new_cost, v, l))
    # 计算线路造价
    used_edges = set()
    for u in range(N):
        for v, T in graph[u]:
            if in_tree[v] and (v, u) not in used_edges:
                total_cost += T[chosen[u]][chosen[v]]
                used_edges.add((u, v))
    return total_cost
print(prim_variant())