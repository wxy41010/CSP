# n=int(input())
# arr=list(map(int,input().split()))
# result=[]
# result.append(max(arr))
# if len(arr)%2!=0:
#     result.append(arr[int((n+1)/2)-1])
# else:
#     result.append(int((arr[int(n/2-1)]+arr[int(n/2)])/2))
# result.append(min(arr))
# print(*result)
n = int(input())  # 输入数据个数
arr = list(map(int, input().split()))  # 输入有序的整数列表
max_val = max(arr)# 计算最大值、最小值
min_val = min(arr)
if n % 2 != 0:# 计算中位数
    median = arr[n // 2]  # 奇数时，直接取中间的元素
else:
    median = (arr[n // 2 - 1] + arr[n // 2]) / 2  # 偶数时，取中间两个数的平均值
if median.is_integer():
    median = int(median)
else:
    median=round(median, 1)
result = [max_val, median, min_val]
result.sort(reverse=True)# 从大到小排序输出
print(*result)
