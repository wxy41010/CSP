n,m,p,q=map(int,input().split())
arr=[]
for _ in range(n): # 读取矩阵并展平
    arr.extend(map(int,input().split()))
for i in range(p): # 按 p × q 维度重塑矩阵
    print(*arr[i*q:(i+1)*q])

'''
2 3 3 2
1 2 3
4 5 6

1 2
3 4
5 6
'''