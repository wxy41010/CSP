from collections import Counter
n = int(input())
arr = list(map(int, input().split()))
freq = Counter(arr)
# 对数组进行排序
arr_sorted = sorted(arr)
found = False  # 标记是否找到中间数
# 遍历排序后的数组
for i in range(n):
    current = arr_sorted[i]  # 当前数
    # 计算当前数左边小于它的数字个数
    count_left = arr_sorted.index(current)
    # 计算当前数右边大于它的数字个数
    count_right = n - count_left - freq[current]
    # 判断是否左右数量相等
    if count_left == count_right:
        print(current)  # 输出找到的中间数
        found = True
        break  # 退出循环
# 如果没有找到符合条件的中间数，输出 -1
if not found:
    print(-1)
