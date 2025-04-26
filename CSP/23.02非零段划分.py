def count_segments(arr, p):  # 定义函数，计算数组 arr 在阈值 p 下的连续非零段数
    count = 0                # 初始化段数计数器为 0
    in_segment = False       # 布尔变量，表示当前是否在一个非零段中，初始为 False
    for i in range(len(arr)):  # 遍历数组的每个索引 i
        if arr[i] >= p:      # 如果当前元素大于等于阈值 p，则保留（视为非零）
            if not in_segment:  # 如果之前不在段中，说明这是一个新段的开始
                count += 1    # 段数加 1
                in_segment = True  # 标记当前处于一个非零段中
        else:               # 如果当前元素小于 p，视为 0
            in_segment = False  # 段中断，标记当前不在段中
    return count            # 返回计算出的段数

n = int(input())           # 输入数组的长度 n，并转换为整数
A = list(map(int, input().split()))  # 输入数组 A，字符串按空格分割并转换为整数列表
max_segments = 0           # 初始化最大段数为 0
for p in range(1, max(A) + 1):  # 遍历所有可能的阈值 p，从 1 到数组最大值 max(A)
    segments = count_segments(A, p)  # 计算当前 p 值下的段数
    max_segments = max(max_segments, segments)  # 更新最大段数，取当前段数和之前最大值的较大者
print(max_segments)        # 输出最大段数