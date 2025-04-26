N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
T = 0  # 剩余苹果总数
drop_trees = [False] * N  # 记录每棵树是否掉落
# 处理每棵树
for i in range(N):
    ops = arr[i]  # 当前树的记录
    m = ops[0]    # 操作次数
    current_apples = ops[1]  # 当前苹果数（初始值）
    T += current_apples      # 先加初始值，后面减去疏果
    # 从第二个操作开始检查
    for j in range(2, m + 1):
        if ops[j] > 0:  # 重新统计
            if ops[j] < current_apples:  # 如果新统计数小于之前总数，说明掉落
                drop_trees[i] = True
            T += ops[j] - current_apples  # 更新 T（减去旧值，加上新值）
            current_apples = ops[j]       # 更新当前苹果数
        else:  # 疏果
            current_apples -= abs(ops[j])
            T -= abs(ops[j])  # 减去疏果数量
# 计算 D：发生掉落的树数
D = sum(drop_trees)
# 计算 E：连续三棵树掉落的组数
E = 0
for i in range(N):
    # 检查 Ai, Ai-1, Ai+1 是否都掉落（圆形处理）
    prev = (i - 1) % N
    next_i = (i + 1) % N
    if drop_trees[prev] and drop_trees[i] and drop_trees[next_i]:
        E += 1
print(T, D, E)