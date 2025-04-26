n, k, t, xl, yd, xr, yu = map(int, input().split())  # 输入n（人数），k（逗留时间阈值），t（时间点数），xl（区域左下x坐标），yd（区域左下y坐标），xr（区域右上x坐标），yu（区域右上y坐标）
passed = 0  # 经过高危区域的人数，初始化为0
stayed = 0  # 逗留的人数，初始化为0
for _ in range(n):  # 循环n次，处理每个人的轨迹
    coords = list(map(int, input().split()))  # 输入一个人的坐标序列，转换为整数列表
    positions = [(coords[i], coords[i+1]) for i in range(0, 2*t, 2)]  # 将坐标序列转换为(x, y)坐标对列表，每对表示一个时间点的坐标
    in_area = False  # 标记此人是否进入过高危区域，初始化为False
    max_stay = 0  # 记录此人连续逗留的最大时间，初始化为0
    current_stay = 0  # 记录当前连续逗留时间，初始化为0
    for x, y in positions:  # 遍历此人的每个位置坐标(x, y)
        if xl <= x <= xr and yd <= y <= yu:  # 判断当前坐标是否在高危区域内
            in_area = True  # 如果在区域内，标记此人经过高危区域
            current_stay += 1  # 当前连续逗留时间加1
            max_stay = max(max_stay, current_stay)  # 更新最大连续逗留时间
        else:  # 如果当前坐标不在高危区域内
            current_stay = 0  # 重置当前连续逗留时间为0
    if in_area:  # 如果此人经过高危区域
        passed += 1  # 经过人数加1
    if max_stay >= k:  # 如果此人最大连续逗留时间大于等于阈值k
        stayed += 1  # 逗留人数加1
print(passed)  # 输出经过高危区域的总人数
print(stayed)  # 输出逗留人数