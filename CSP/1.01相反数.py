n=int(input())
arr=list(map(int,input().split()))
count=0
for i in arr :
    if -i in arr:
        count+=1
print(int(count/2))

