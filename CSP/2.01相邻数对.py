# n = int(input())
# arr = set(map(int, input().split()))  # 使用集合提高查找效率
# count = 0
# for i in arr:
#     if i + 1 in arr:
#         count += 1
# print(count)

n=int(input())
arr=list(map(int,input().split()))
count=0
for i in arr:
    if i+1 in arr:
        count+=1
print(count)