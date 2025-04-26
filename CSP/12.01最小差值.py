n = int(input())
arr = list(map(int, input().split()))
arr.sort()  # 排序数组
min_diff = float('inf')  # 初始化最小差值为无穷大
# 计算相邻元素的差值
for i in range(1, n):
    min_diff = min(min_diff, arr[i] - arr[i - 1])
print(min_diff)
