# 读取输入的第一行：出行计划数n，查询数m，等待时间k
n, m, k = map(int, input().split())  # 输入n, m, k并用空格分隔转换为整数
# 初始化出行计划列表
plans = []  # 创建空列表用于存储出行计划
# 读取n个出行计划
for i in range(n):  # 循环n次读取出行计划
    t, c = map(int, input().split())  # 读取每个出行计划的时间t和要求时限c
    plans.append((t, c))  # 将(t, c)元组添加到plans列表中
# 处理m个查询
for j in range(m):  # 循环m次处理每个查询
    q = int(input())  # 读取查询时间q并转换为整数
    count = 0  # 初始化计数器，统计满足条件的出行计划数
    start_time = q + k  # 计算核酸结果生效时间
    for t, c in plans:  # 遍历每个出行计划
        #(end_time - start_time + 1) = c  0-23 即24个时间节点
        end_time = start_time + c -1  # 计算该出行计划下核酸结果的截止时间
        if start_time <= t <= end_time:  # 检查当前出行时间是否在有效区间内
            count += 1  # 如果满足条件，计数器加1
    print(count)  # 输出当前查询的结果