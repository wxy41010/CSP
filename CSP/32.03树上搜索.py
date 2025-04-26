def dfs(pre, no, wi, yes):              # 定义DFS函数，计算子树权重并收集有效节点
    if pre in no: return 0              # 如果当前节点在排除集合中，返回0（不计入权重）
    yes.add(pre)                        # 将当前节点加入有效节点集合yes
    total = wi[pre]                     # 初始化total为当前节点的初始权重
    for i in ls[pre]:                   # 遍历当前节点的子节点
        if i not in no:                 # 如果子节点未被排除
            total += dfs(i, no, wi, yes)# 递归计算子节点权重并累加到total
    wi[pre] = total                     # 更新当前节点的权重为子树总权重
    return total                        # 返回子树总权重

def check(idx, t, no):                  # 定义检查函数，判断目标t是否在idx子树中
    return idx == t or any(check(i, t, no) for i in ls[idx] if i not in no) # 返回idx等于t或任一未排除子节点包含t

n, m = map(int, input().split())        # 读取输入：n为类别数，m为测试数
wi = [0] + list(map(int, input().split())) # 读取权重数组，首位补0，索引从1开始
ls = [[] for _ in range(n + 1)]         # 初始化邻接表，ls[i]存储节点i的子节点
[ls[p].append(i) for i, p in enumerate(map(int, input().split()), 2)] # 构建树，p为父节点，i为子节点从2开始

for _ in range(m):                      # 对每个测试用例循环
    t, pre, no = int(input()), 1, set() # 初始化：t为目标类别，pre为当前节点（根1），no为空排除集合
    ans = []                            # 初始化答案列表，存储每次询问的类别
    while True:                         # 开始询问循环
        yes = set()                     # 初始化有效节点集合
        w = wi.copy()                   # 复制初始权重数组，用于本次计算
        dfs(pre, no, w, yes)            # 执行DFS，更新权重并收集有效节点
        if len(yes) <= 1: break         # 如果只剩1个或0个节点，退出循环
        idx = min(yes, key=lambda j: (abs(2 * w[j] - w[pre]), j != 1, j)) # 选择wδ最小的节点，优先避免根节点
        ans.append(idx)                 # 将选择的节点加入答案
        if check(idx, t, no):           # 如果目标t在idx子树中
            pre = idx                   # 更新当前节点为idx（回答“是”）
        else:                           # 如果目标t不在idx子树中
            no.add(idx)                 # 将idx加入排除集合（回答“否”）
    print(*ans)