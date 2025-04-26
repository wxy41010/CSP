MOD = 998244353                         # 定义模数常量，所有矩阵元素需对此取模
def mat_mul(a, b):                      # 定义2×2矩阵乘法函数，输入两个矩阵a和b
    c = [[0, 0], [0, 0]]               # 初始化结果矩阵c为2×2全零矩阵
    c[0][0] = (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % MOD # 计算c[0][0]，对应矩阵乘法第一行第一列，模MOD
    c[0][1] = (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % MOD # 计算c[0][1]，对应矩阵乘法第一行第二列，模MOD
    c[1][0] = (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % MOD # 计算c[1][0]，对应矩阵乘法第二行第一列，模MOD
    c[1][1] = (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % MOD # 计算c[1][1]，对应矩阵乘法第二行第二列，模MOD
    return c                            # 返回乘法结果矩阵c
identity = [[1, 0], [0, 1]]            # 定义2×2单位矩阵，作为空队列时的默认密码
def solve_segment(cmds, l, r):          # 定义函数，计算指令区间[l,r]执行后的密码
    dq = []                             # 初始化双端队列dq，用于存储矩阵
    time = []                           # 初始化时间列表time，记录每个矩阵的插入时间
    cur_time = 0                        # 初始化当前时间戳cur_time，用于标记插入顺序
    for i in range(l - 1, r):           # 遍历指令区间[l,r]，注意索引从l-1到r-1
        op = cmds[i][0]                 # 获取第i条指令的操作类型（1,2,3之一）
        if op == 1:                     # 如果操作类型为1（头部插入）
            dq.insert(0, cmds[i][1])    # 将指令中的矩阵插入队列头部
            time.insert(0, cur_time)    # 记录该矩阵的插入时间，插入头部
            cur_time += 1               # 时间戳递增，表示新矩阵插入
        elif op == 2:                   # 如果操作类型为2（尾部插入）
            dq.append(cmds[i][1])       # 将指令中的矩阵追加到队列尾部
            time.append(cur_time)       # 记录该矩阵的插入时间，追加到尾部
            cur_time += 1               # 时间戳递增，表示新矩阵插入
        elif op == 3 and dq:            # 如果操作类型为3且队列非空（删除最近插入的矩阵）
            max_time = max(time)        # 找到最近插入的时间戳（最大值）
            idx = time.index(max_time)  # 获取该时间戳对应的矩阵索引
            dq.pop(idx)                 # 从队列中移除该矩阵
            time.pop(idx)               # 从时间列表中移除对应时间戳
    if not dq:                          # 如果队列为空
        return identity                 # 返回单位矩阵作为密码
    result = dq[0]                      # 初始化结果矩阵为队列第一个矩阵
    for i in range(1, len(dq)):         # 遍历队列从第二个矩阵到最后一个
        result = mat_mul(result, dq[i]) # 将结果矩阵与当前矩阵相乘，更新结果
    return result                       # 返回最终的密码矩阵

n, m = map(int, input().split())        # 读取输入：n为指令数，m为事件数
cmds = []                               # 初始化指令列表cmds，存储所有指令
for _ in range(n):                      # 循环n次，读取初始指令
    line = list(map(int, input().split())) # 读取一行输入，转换为整数列表
    if line[0] == 3:                    # 如果指令类型为3（删除操作）
        cmds.append((3, None))          # 添加元组(3, None)到指令列表，表示无矩阵
    else:                               # 如果指令类型为1或2（插入操作）
        mat = [[line[1], line[2]], [line[3], line[4]]] # 构造2×2矩阵，从输入中提取四个元素
        cmds.append((line[0], mat))     # 添加元组(操作类型, 矩阵)到指令列表

for _ in range(m):                      # 循环m次，处理每个事件
    line = list(map(int, input().split())) # 读取一行输入，转换为整数列表
    if line[0] == 1:                    # 如果事件类型为1（更新指令）
        i = line[1] - 1                 # 获取要更新的指令索引（输入从1开始，转换为0-based）
        if line[2] == 3:                # 如果新指令类型为3（删除操作）
            cmds[i] = (3, None)         # 更新第i条指令为(3, None)
        else:                           # 如果新指令类型为1或2（插入操作）
            mat = [[line[3], line[4]], [line[5], line[6]]] # 构造新2×2矩阵，从输入中提取四个元素
            cmds[i] = (line[2], mat)    # 更新第i条指令为(新操作类型, 新矩阵)
    else:                               # 如果事件类型为2（查询密码）
        l, r = line[1], line[2]         # 获取查询区间[l,r]
        result = solve_segment(cmds, l, r) # 调用solve_segment计算区间[l,r]的密码
        print(result[0][0], result[0][1], result[1][0], result[1][1]) # 输出密码矩阵的四个元素