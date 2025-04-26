n, N, q = map(int, input().split()) # 读取 n（路数）、N（组数）、q（指令数）
ops = [list(map(int, input().split())) for _ in range(q)] # 读取 q 条指令，每条包含操作类型 o 和内存块编号 a
cache = [[] for _ in range(N)] # 初始化缓存：N 个组，每个组是一个列表，存储 (block_id, dirty) 元组
result = [] # 输出结果
for o, a in ops: # 遍历每条指令，o 是操作类型，a 是内存块编号
    group = a // n % N # 计算内存块 a 所属的组号，取模确保在 0 到 N-1
    group_cache = cache[group] # 获取该组的缓存行
    hit = False # 检查是否命中，初始化为 False
    for i, (block_id, dirty) in enumerate(group_cache): # 遍历该组缓存行，i 是索引，(block_id, dirty) 是缓存行内容
        if block_id == a: # 命中，当前缓存行存储的块等于目标块
            hit = True # 标记为命中
            group_cache.pop(i) # 更新 LRU：移除命中的块
            group_cache.insert(0, (a, dirty or o == 1)) # 将命中的块移到最前，更新 dirty 状态（写操作置 True）
            break # 命中后退出循环
    if not hit: # 未命中
        if len(group_cache) < n: # 组内有空位，缓存行数小于路数 n
            result.append([0, a]) # 读入内存块 a，添加读操作到结果
            group_cache.insert(0, (a, o == 1)) # 加入缓存，放在最前，dirty 根据操作类型设置
        else: # 组满，需要替换
            block_id, dirty = group_cache.pop() # LRU 替换：移除最久未使用的块，返回其 block_id 和 dirty
            if dirty: # 如果被替换的块被修改过
                result.append([1, block_id]) # 写回内存，添加写操作到结果
            result.append([0, a]) # 读入新块 a，添加读操作到结果
            group_cache.insert(0, (a, o == 1)) # 加入缓存，放在最前，dirty 根据操作类型设置
for op, addr in result: # 遍历结果列表，输出每次内存操作
    print(op, addr) # 输出操作类型和内存块编号，用空格分隔