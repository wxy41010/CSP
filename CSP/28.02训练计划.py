n, m = map(int, input().split())  # 读取总天数 n 和科目数 m
p, t = [list(map(int, input().split())) for _ in range(2)]  # 读取两行输入：p（依赖关系数组），t（每科目训练时间数组）
# 最早开始时间
earliest_start = [0] * m  # 初始化 m 个科目最早开始时间为 0
# 计算每个科目的最早开始时间
for i in range(m):  # 遍历每个科目
    if p[i] == 0:  # 如果没有依赖（p[i] == 0）
        earliest_start[i] = 1  # 该科目从第 1 天开始
    else:  # 如果有依赖
        earliest_start[i] = earliest_start[p[i] - 1] + t[p[i] - 1]  # 依赖科目（p[i]-1）结束后开始

# 检查是否能在 n 天内完成
for i in range(m):  # 遍历每个科目
    if earliest_start[i] + t[i] - 1 > n:  # 如果该科目的结束时间超过 n 天
        # 如果无法在 n 天内完成，输出最早开始时间并结束
        print(*earliest_start)  # 使用 * 解包列表，直接输出每个元素，用空格分隔
        exit()  # 使用内置的 exit() 函数退出程序

# 最晚开始时间
latest_start = [0] * m  # 初始化 m 个科目最晚开始时间为 0
# 计算最晚开始时间（假设所有科目都在 n 天内完成）
for i in range(m):  # 遍历每个科目
    latest_start[i] = n - t[i] + 1  # 最晚开始时间 = 总天数 - 训练时间 + 1

# 倒序更新每个科目的最晚开始时间，考虑依赖关系
for i in range(m-1, -1, -1):  # 从最后一个科目倒序到第一个
    if p[i] != 0:  # 如果当前科目有依赖
        latest_start[p[i] - 1] = min(latest_start[p[i] - 1], latest_start[i] - t[p[i] - 1])  # 更新依赖科目的最晚开始时间

print(*earliest_start)
print(*latest_start)