# n, m, p, q = map(int, input().split())
# a = []
# # 读取矩阵并展平
# for i in range(n):
#     a.extend(map(int, input().split()))
# # 按 p × q 维度重塑矩阵
# # for i in range(p):
# #     print(*a[i * q:(i + 1) * q])
#
#     # 输出时按照列数 `<= q` 进行切片
# for i in range(0, len(a), q):
#     print(*a[i:i + q])
'''
2 3 3 2
1 2 3
4 5 6
'''

n,m,p,q=map(int,input().split())
arr=[]
for _ in range(n):
    arr.extend(map(int,input().split()))
for i in range(p):
    print(*arr[i*q:(i+1)*q])