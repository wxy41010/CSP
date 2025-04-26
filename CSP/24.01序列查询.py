n, N = map(int, input().split())  # 输入两个整数 n 和 N，用空格分隔
A = [0] + list(map(int, input().split()))  # 输入数组 A，并在开头加上 A0 = 0
total_sum = 0  # 初始化总和为 0
idx = 0  # 初始化下标为 0，表示当前指向数组的哪个位置
f = [0] * N  # f(i)数组，长度为N
for i in range(N):  # 遍历 x 从 0 到 N-1
    while idx <= n and A[idx] <= i:  #  x作为分段的间隔 表示区间内下标的值
        idx += 1  # 移动下标到下一个位置
    f[i] = idx - 1
total_sum = sum(f)  # 将当前下标加到总和中
print(total_sum)  # 输出总和