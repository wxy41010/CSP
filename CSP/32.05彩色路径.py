import sys
from collections import defaultdict

# 常量定义
INF = float('inf')
N = 105  # 节点数上限
M = 5005  # 边数上限

# 输入处理函数
def work():
    # 读取输入
    n, m, l, k = map(int, input().split())
    c = list(map(int, input().split()))  # 节点颜色
    U = [0] + list(map(int, input().split()))  # 边起点，索引从 1 开始
    V = [0] + list(map(int, input().split()))  # 边终点，索引从 1 开始
    D = [0] + list(map(int, input().split()))  # 边长度，索引从 1 开始

    # 构建正向和反向邻接表
    g = [[] for _ in range(n)]   # 正向图
    gg = [[] for _ in range(n)]  # 反向图
    for i in range(1, m + 1):
        g[U[i]].append((V[i], D[i]))
        gg[V[i]].append((U[i], D[i]))

    # 调整 l 为路径长度（节点数 - 1）
    l -= 1
    ll = l // 2  # 前半段长度
    lr = l - ll  # 后半段长度

    # dp[u][s] 表示从 0 到 u，已用颜色集合 s 的最大路径长度
    dp = [{} for _ in range(n)]
    dpp = [{} for _ in range(n)]

    # 前向 DP：从节点 0 开始
    dp[0][1 << c[0]] = 0
    for _ in range(1, ll + 1):
        for u in range(n):
            if not dp[u]: continue
            for s, val in list(dp[u].items()):
                if bin(s).count('1') != _: continue  # 检查颜色数量
                for v, w in g[u]:
                    if s & (1 << c[v]): continue  # 颜色冲突
                    new_s = s | (1 << c[v])
                    dp[v][new_s] = max(dp[v].get(new_s, float('-inf')), val + w)

    # 后向 DP：从节点 n-1 开始
    dpp[n - 1][1 << c[n - 1]] = 0
    for _ in range(1, lr + 1):
        for u in range(n):
            if not dpp[u]: continue
            for s, val in list(dpp[u].items()):
                if bin(s).count('1') != _: continue  # 检查颜色数量
                for v, w in gg[u]:
                    if s & (1 << c[v]): continue  # 颜色冲突
                    new_s = s | (1 << c[v])
                    dpp[v][new_s] = max(dpp[v].get(new_s, float('-inf')), val + w)

    # 合并结果
    ans = 0
    for i in range(n):
        if not dp[i] or not dpp[i]: continue
        # 提取前向和后向的路径长度和状态
        v = [(val, s) for s, val in dp[i].items()]
        vv = [(val, s) for s, val in dpp[i].items()]
        v.sort(reverse=True)  # 按路径长度降序
        vv.sort(reverse=True)

        for val1, s1 in v:
            if val1 + vv[0][0] <= ans: break  # 剪枝
            for val2, s2 in vv:
                if val1 + val2 <= ans: break  # 剪枝
                # 检查颜色集合是否只在节点 i 处重叠
                if (s1 & s2) == (1 << c[i]):
                    ans = max(ans, val1 + val2)

    print(ans)
work()