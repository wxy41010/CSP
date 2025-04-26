N = int(input())  # 读取可用钱数
ans = 0  # 用于记录获得的酱油瓶数
count_5 = N // 50 # 优先使用买5瓶送2瓶的方式
ans += count_5 * 7  # 每50元可以买7瓶
N -= count_5 * 50  # 剩余的钱
count_3 = N // 30  # 然后使用买3瓶送1瓶的方式
ans += count_3 * 4  # 每30元可以买4瓶
N -= count_3 * 30  # 剩余的钱
ans += N // 10  # 最后，用剩下的钱买单瓶酱油
print(ans)
