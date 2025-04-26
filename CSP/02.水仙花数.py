def waterflower(n):
    a=n%10
    b=(n%100)//10
    c=n//100
    if a**3+b**3+c**3==n:
        print(n)
for i in range(100,100000):
    waterflower(i)
