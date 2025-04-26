from collections import defaultdict  # 导入 defaultdict 用于构建邻接表

N, M, K = map(int, input().split())  # 读取城镇数 N、边数 M、候选地址数 K
money = [list(map(int, input().split())) for _ in range(N)]  # 读取 N 个城镇的 K 个变电站造价
graph = defaultdict(list)  # 初始化邻接表，用于存储图结构

# 读取 M 条输电线路
for _ in range(M):  # 循环 M 次读取每条边
    l = list(map(int, input().split()))  # 读取一行输入，包含 K^2 + 2 个整数
    u, v = l[0], l[1]  # 前两个数是边的两端城镇编号
    costs = l[2:]  # 剩余 K^2 个数是造价矩阵的行主序存储
    T = [[0] * K for _ in range(K)]  # 初始化 K×K 的造价矩阵
    for i in range(K):  # 将行主序存储转换为矩阵
        for j in range(K):  # 遍历 K×K 个元素
            T[i][j] = costs[i * K + j]  # 填充矩阵元素
    graph[u].append((v, T))  # 将边 (u, v) 和矩阵 T 添加到 u 的邻接表
    graph[v].append((u, [[T[j][i] for j in range(K)] for i in range(K)]))  # 添加反向边 (v, u) 和转置矩阵

# 树形 DP（适用于 M = N-1 的情况）
def dp_on_tree():  # 定义树形 DP 函数
    dp = [[float('inf')] * K for _ in range(N)]  # dp[u][k] 表示以 u 为根选择 k 的最小造价
    visited = [False] * N  # 初始化访问标记数组

    def dfs(u, parent):  # 定义 DFS 函数，参数为当前节点 u 和父节点 parent
        visited[u] = True  # 标记节点 u 已访问
        children = [v for v, _ in graph[u] if v != parent]  # 获取 u 的子节点（排除父节点）
        # 初始化 dp[u][k] 为变电站造价
        for k in range(K):  # 遍历 u 的 K 个候选地址
            dp[u][k] = money[u][k]  # 设置初始值为变电站造价

        # 如果是叶子节点，直接返回
        if not children:  # 如果没有子节点
            return  # 结束递归

        # 处理每个子节点
        for v, T in graph[u]:  # 遍历 u 的邻接节点和对应造价矩阵
            if v == parent:  # 如果是父节点
                continue  # 跳过
            dfs(v, u)  # 递归处理子节点 v
            # 更新 dp[u][k]
            for k in range(K):  # 遍历 u 的地址 k
                min_child_cost = float('inf')  # 初始化子节点最小造价为无穷大
                for l in range(K):  # 遍历子节点 v 的地址 l
                    min_child_cost = min(min_child_cost, dp[v][l] + T[k][l])  # 更新最小造价
                dp[u][k] += min_child_cost  # 将子树最小造价加到 dp[u][k]

    # 从节点 0 开始 DFS
    dfs(0, -1)  # 以 0 为根，父节点设为 -1
    return min(dp[0])  # 返回根节点所有地址选择的最小值

# 检查是否是树（M = N-1）
if M == N - 1:  # 如果边数等于节点数减 1
    result = dp_on_tree()  # 调用树形 DP 计算结果
else:  # 如果不是树
    # 对于非树情况，此处仅提示需扩展，当前实现假设输入是树
    result = dp_on_tree()  # 注意：完整解法需扩展到一般图

# 输出结果
print(result)  # 打印最低总造价