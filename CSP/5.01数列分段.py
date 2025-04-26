n=int(input())
arr=list(map(int,input().split()))
count=1
for i in range(1,n):
    # 如果当前元素与前一个元素不同，则新的一段开始
    if arr[i]!=arr[i-1]:
        count+=1
print(count)