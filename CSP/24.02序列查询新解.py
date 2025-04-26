n, N = map(int, input().split())  # 输入两个整数n和N，用空格分隔，并转换为整数类型
A = [0] + list(map(int, input().split()))  # 输入数组A，在开头添加A0=0，然后将输入的字符串转换为整数列表
r = N // (n + 1)  # 计算r的值，为N除以(n+1)的下取整
f = [0] * N  # f(i)数组，长度为N
g = [0] * N  # g(i)数组，长度为N
ans = [0] * N  # 答案数组，长度为N
# 计算f(i)：对于每个i，找到A中小于等于i的最大数的下标
for i in range(N):
    idx = 0
    while idx <= n and A[idx] <= i:
        idx += 1
    f[i] = idx - 1 # 减1因为我们想要最后一个小于等于i的数的下标
for i in range(N): # 计算g(i)和ans(i)
    g[i] = i // r  # 计算g(i)，为i除以r的下取整
    ans[i] = abs(g[i] - f[i])  # 计算|g(i)-f(i)|的绝对值
total_sum = sum(ans)  # 计算总和
print(total_sum)  # 输出结果