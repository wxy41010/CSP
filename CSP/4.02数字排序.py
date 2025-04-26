from collections import Counter
n = int(input())
nums = list(map(int, input().split()))
# 使用 Counter 统计 nums 列表中每个数字的出现次数，返回一个字典 {数字: 频率}
count = Counter(nums)
# 对统计结果进行排序：
# 1. `-x[1]` 表示按出现次数（x[1]）的降序排列
# 2. `x[0]` 表示当出现次数相同时，按数字（x[0]）的升序排列
sorted_items = sorted(count.items(), key=lambda x: (-x[1],x[0]))
# 遍历排序后的列表，按格式输出每个数字及其出现次数
for num, freq in sorted_items:
    print(num, freq)

"""
12
5 2 3 3 1 3 4 2 5 2 3 5

3 4
2 3
5 3
1 1
4 1
"""