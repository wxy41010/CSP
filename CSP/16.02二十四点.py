n=int(input())
def cal(a,b,c):
    if b=="+":
        return a+c
    elif b=="-":
        return a-c
    elif b=="x":
        return a*c
    elif b=="/":
        return a//c
s3=0
for i in range(n):
    l=input()
    if l[1] in '+-x*/' and l[3] in '+-x*/' and l[5] in '+-x*/':
        a, b, c, d, e, f, g = l
        a, c, e, g = int(a), int(c), int(e), int(g)  # 转换为整数
        if d=="+" or d=="-":
            s1=cal(a,b,c)
            s2=cal(e,f,g)
            s3=cal(s1,d,s2)
        else:
            s1=cal(a,b,c)
            s2=cal(s1,d,e)
            s3=cal(s2,f,g)
        if s3==24:
            print("Yes")
        else:
            print("No")

"""
10
9+3+4x3
5+4x5x5
7-9-9+8
5x6/5x4
3+5+7+9
1x1+9-9
1x9-5/9
8/5+6x9
6x7-3x6
6x4+4/5

Yes
No
No
Yes
Yes
No
No
No
Yes
Yes
"""