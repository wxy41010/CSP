n=int(input())
peo=map(int,input().split())
car=[0] * 100#车厢座位
h=[5]*20#每排剩下的座位数
for i in peo:
    bl = False
    for j in range(20):#遍历行
        if h[j]>=i:#找能坐在一起的座位
            for k in range(i):
                num=5*j+5-h[j]+k+1
                car[num]=num
                print(car[num],end=' ')
            bl=True
            h[j]-=i
            break
    if bl==False:#没有坐在一起的座位，空位排着坐
        for j in range(100):
            if car[j]==0:
                car[j]=j+1 #索引从0开始，座位号要加1
                i-=1
                print(car[j],end=' ')
            if i==0:
                break
    print()

"""
4
2 5 4 2

1 2
6 7 8 9 10
11 12 13 14
3 4
"""