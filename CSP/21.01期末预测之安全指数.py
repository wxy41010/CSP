# n = int(input())  # 输入一个整数n，表示需要处理的数据组数
# sum = 0  # 初始化总和sum为0，用于累加计算结果
# for i in range(1, n+1):  # 循环n次，从1到n，处理每一组数据
#     w, score = map(int, input().split())  # 输入两个整数w（权重）和score（分数），用空格分隔
#     result = score * w  # 计算当前组的分数与权重的乘积
#     sum += result  # 将乘积加到总和sum中
# if sum < 0:  # 如果总和sum小于0
#     sum = 0  # 将总和sum重置为0（负数结果按0处理）
# print(sum)  # 输出最终的总和sum

n = int(input())  # 输入一个整数n，表示需要处理的数据组数
total = sum(int(w) * int(score) for w, score in (input().split() for _ in range(n)))  # 计算所有组的权重w与分数score乘积的总和，使用生成器表达式
print(max(0, total))  # 输出total与0中的较大值，确保结果非负

"""
6
2 60
10 100
0 70
0 0
-10 50
10 60

1220
"""