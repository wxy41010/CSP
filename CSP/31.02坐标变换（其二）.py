import math
n,m=map(int,input().split())
operations=[list(map(float,input().split())) for _ in range(n)]
find=[list(map(int,input().split())) for _ in range(m)]
result=[]
for i,j,x,y in find:
    for op,k in operations[i-1:j]: # 仅遍历 t_i 到 t_j
        if op==1: # 拉伸
            x*=k
            y*=k
        else: # 旋转
            x=x*math.cos(k)-y*math.sin(k)
            y=x*math.sin(k)+y*math.cos(k)
    result.append(f'{x:.3f} {y:.3f}')
for i in range(m):
    print(result[i])

'''
10 5
2 0.59
2 4.956
1 0.997
1 1.364
1 1.242
1 0.82
2 2.824
1 0.716
2 0.178
2 4.094
1 6 -953188 -946637
1 9 969538 848081
4 7 -114758 522223
1 9 -535079 601597
8 8 159430 -511187

-1858706.758 -83259.993
-1261428.460 201113.678
-75099.123 -738950.159
-119179.897 -789457.532
114151.880 -366009.892
'''

