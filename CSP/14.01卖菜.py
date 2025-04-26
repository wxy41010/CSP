n = int(input())  # 输入商店数量
arr = list(map(int, input().split()))  # 输入第一天的菜价
# 初始化结果数组
result = [0] * n
# 边界处理
result[0] = (arr[0] + arr[1]) // 2
result[n - 1] = (arr[n - 2] + arr[n - 1]) // 2
# 中间部分商店的价格
for i in range(1, n - 1):
    result[i] = (arr[i - 1] + arr[i] + arr[i + 1]) // 3
# 输出第二天的价格
print(*result)
