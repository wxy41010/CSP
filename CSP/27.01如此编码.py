def restore_answers(n, m, a):
    # 计算前缀乘积c
    c = [1] * n
    for i in range(1, n):
        c[i] = c[i-1] * a[i-1]
    # 结果数组
    b = [0] * n
    # 根据公式恢复每个bi
    for i in range(n-1, -1, -1):
        b[i] = m // c[i]  # 求出bi
        m %= c[i]  # 更新m为剩余的部分
    return b
# 输入数据
n, m = map(int, input().split())
a = list(map(int, input().split()))
# 计算并输出结果
result = restore_answers(n, m, a)
for i in range(len(result)):
    print(result[i], end=" ")