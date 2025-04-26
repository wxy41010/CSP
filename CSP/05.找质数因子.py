def zyz(n):
    y=2
    list=[]
    while n!=y:
        if n%y==0:
            list.append(y)
            n/=y
        else:
            y+=1
    list.append(int(n))
    return list
print(*zyz(1000))