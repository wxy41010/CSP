n = int(input())
B = list(map(int, input().split()))
sum_max = sum(B)
sum_min = B[0]  # A1 必然等于 B1
prev = B[0]
for i in range(1, n):
    if B[i] > prev:
        sum_min += B[i]  # 取新的最大值
    prev = B[i]
print(sum_max)
print(sum_min)


