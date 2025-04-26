n, m, k = map(int, input().split())
cnt = [0] * (2*10**5 + 10)
for _ in range(n):
    t, c = map(int, input().split())
    x = t + 1 - k - c
    y = t - k
    if y <= 0:
        continue  # 上界不能小于0，不然没意义
    x = max(1, x)  # 下界不能小于1，不然是没意义的
    cnt[x] += 1  # 差分
    cnt[y + 1] -= 1
# 计算前缀和
for i in range(1, 2 * 10**5 + 1):
    cnt[i] += cnt[i - 1]
# 查询部分
for _ in range(m):
    q = int(input())
    print(cnt[q])

