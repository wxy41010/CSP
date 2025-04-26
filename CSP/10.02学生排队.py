n=int(input())
l=[i for i in range(1,n+1)]
m=int(input())
for i in range(m):
    p,q=map(int,input().split())
    for j in range(n):# 找到所要移动的元素位置，用k记录
        if l[j]==p:
            k=j
            continue
    st=l[k]
    if q>0:# 后移
        for j in range(q):# 将k+1到k+q位置的元素前移一个位置
            l[k+j]=l[k+j+1]
        l[k+q]=st
    else:# 前移
        for j in range(0,q,-1):#range(abs(q)):---k-j---k-j-1
            l[k+j]=l[k+j-1]
        l[k+q]=st
print(*l)

"""
8
3
3 2
8 -3
3 -2

1 2 4 3 5 8 6 7
"""
