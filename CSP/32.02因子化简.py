def prime(n,k):
    ans=1
    i=2
    while i*i<n: # 从2到sqrt(n)检查是否是n的因子
        count=0
        while n%i==0:
            count+=1
            n//=i
        if count>=k:
            ans*=i**count # 将因子i的幂次乘到结果中
        i+=1
    return ans
q=int(input())
for _ in range(q):
    n,k=map(int,input().split())
    print(prime(n,k))


"""
3
2155895064 3
2 2
10000000000 10

2238728
1
10000000000
"""