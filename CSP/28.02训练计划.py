import sys

n, m = map(int, input().split())
p, t = [list(map(int, input().split())) for _ in range(2)]

# 最早开始时间
earliest_start = [0] * m
# 计算每个科目的最早开始时间
for i in range(m):
    if p[i] == 0:
        earliest_start[i] = 1  # 没有依赖的科目从第一天开始
    else:
        earliest_start[i] = earliest_start[p[i] - 1] + t[p[i] - 1]  # 依赖的科目p[i] - 1结束后开始

# 遍历每个科目得训练时间
for i in range(m):
    if earliest_start[i] + t[i] - 1 > n:
        # 如果某个科目的训练无法在n天内完成，直接输出最早开始时间并退出
        print(" ".join(map(str, earliest_start)))
        sys.exit()  # 退出程序

# 最晚开始时间
latest_start = [0] * m
# 计算最晚结束时间（所有科目都在n天内完成）
for i in range(m):
    latest_start[i] = n - t[i] + 1  # 最晚结束时间是n减去训练时间再加1

# 倒序更新每个科目的最晚开始时间
for i in range(m-1, -1, -1):
    if p[i] != 0:
        latest_start[p[i] - 1] = min(latest_start[p[i] - 1], latest_start[i] - t[i])
# 输出最早开始时间
print(" ".join(map(str, earliest_start)))
# 输出最晚开始时间
print(" ".join(map(str, latest_start)))
