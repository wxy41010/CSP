import math
def area(a,b,c):
    p=(a+b+c)/2
    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(f'{s:.2f}')
a,b,c=map(float,input().split())
area(a,b,c)