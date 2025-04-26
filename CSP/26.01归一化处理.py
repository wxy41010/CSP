from cmath import sqrt
n = int(input())  # 输入数据的个数
a = list(map(int, input().split()))  # 输入n个整数并转换为列表
avg = sum(a) / n  # 计算平均值
D = sum((x - avg) ** 2 for x in a) / n  # 计算方差
for x in a:
    f = (x - avg) / sqrt(D)
    print(f.real)  # 输出实数部分，并且是浮点数格式
