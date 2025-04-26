n=int(input())
arr=list(map(int,input().split()))
max_diff=0
for i in range(1,n):
    max_diff=max(max_diff,abs(arr[i]-arr[i-1]))
print(max_diff)
