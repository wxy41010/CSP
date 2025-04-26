n = int(input())  # 输入天数
arr = list(map(int, input().split()))  # 输入销售量数据
count = 0
for i in range(1, n-1):  # 从第二天到倒数第二天
    if (arr[i] > arr[i-1] and arr[i] > arr[i+1]) or (arr[i] < arr[i-1] and arr[i] < arr[i+1]):
        count += 1  # 如果是折点，计数增加
print(count)  # 输出折点的数量
