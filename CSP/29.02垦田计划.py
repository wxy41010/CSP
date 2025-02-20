n, m, k = map(int, input().split())
regions = [list(map(int, input().split())) for _ in range(n)]
# 二分查找最小的最大耗时
def can_complete_in_time(T):
    total_resources_needed = 0
    for t, c in regions:
        if t > T:
            # 如果当前区域耗时超过 T，需要投入资源来缩短
            total_resources_needed += (t - T) * c
            if total_resources_needed > m:  # 如果资源已经超出
                return False
    return total_resources_needed <= m
# 二分查找
low, high = k, max(t for t, c in regions)
ans = high
while low <= high:
    mid = (low + high) // 2
    if can_complete_in_time(mid):
        ans = mid
        high = mid - 1 #mid 可行时，我们缩小搜索范围的右侧
    else:
        low = mid + 1  #mid 不可行时，我们缩小搜索范围的左侧
print(ans)

"""
4 9 2
6 1
5 1
6 2
7 1

5
"""

