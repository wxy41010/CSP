n, m, L = map(int, input().split())
A = [0] * L  # 创建长度为 L 的直方图数组
# 直接统计灰度值出现的次数
for _ in range(n):
    for x in map(int, input().split()):
        A[x] += 1
# 输出结果
print(*A)
# n,m,L=map(int,input().split())
# A=[list(map(int,input().split())) for i in range(n)]
# A=sum(A,[])
# for i in range(L):
#     count=A.count(i)
#     print(count,end=" ")