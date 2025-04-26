n=int(input()) # 记录条数
arr=list(map(int,input().split())) # 读者编号列表
l=[0]*1000
result=[]
for i in arr:
    l[i]+=1
    result.append(l[i])
print(*result)
