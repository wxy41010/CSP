# def prime_factors(n, k):
#     res = 1
#     i = 2
#     # 从2到sqrt(n)检查是否是n的因子
#     while i * i <= n:
#         co = 0
#         while n % i == 0:
#             n //= i
#             co += 1
#         if co >= k:
#             res *= i ** co  # 将因子i的幂次乘到结果中
#         i += 1
#     # 如果剩下的n大于1，说明n是一个质数
#     if n > 1:
#         if k == 1:
#             res *= n
#     return res
#
# # 主程序
# q = int(input())  # 输入查询的次数
# for _ in range(q):
#     n, k = map(int, input().split())  # 输入每个查询的n和k
#     print(prime_factors(n, k))

"""
3
2155895064 3
2 2
10000000000 10

2238728
1
10000000000
"""
def prime(n,k):
    ans=1
    i=2
    while i*i<n:
        count=0
        while n%i==0:
            count+=1
            n//=i
        if count>=k:
            ans*=i**count
        i+=1
    return ans
q=int(input())
for _ in range(q):
    n,k=map(int,input().split())
    print(prime(n,k))