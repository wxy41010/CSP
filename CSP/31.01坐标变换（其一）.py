n,m=map(int,input().split())
matrix=[list(map(int,input().split())) for _ in range(n)]
start=[list(map(int,input().split()))for _ in range(m)]
for xj, yj in start:
    for dx, dy in matrix:
        xj += dx
        yj += dy
    print(xj, yj)

'''
3 2
10 10
0 0
10 -20
1 -1
0 0

21 -11
20 -10

'''