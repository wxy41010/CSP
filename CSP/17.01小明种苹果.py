# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# T_total = 0  # 所有树剩余苹果的总数
# P = []  # 存储每棵树疏果的总数量
# max_removed = 0  # 当前最大疏果数量
# k = -1  # 记录最多疏果的树编号，初始化为-1
# for i in range(N):
#     initial_apples = arr[i][0]  # 第i棵树的初始苹果数量
#     total_removed = 0  # 记录当前树去掉的苹果数量
#     # 计算去掉的苹果数量
#     for j in range(1, M + 1):
#         total_removed += abs(arr[i][j])  # 每一轮疏果去掉的苹果数
#     # 更新T_total（剩余的苹果数量）
#     T_total += initial_apples - total_removed
#     # 存储该树的疏果总数
#     P.append(total_removed)
#     # 判断是否是最大疏果数的树
#     if total_removed > max_removed:
#         max_removed = total_removed
#         k = i + 1  # 树的编号从1开始，所以i+1
# # 输出最终结果
# print(T_total, k, max_removed)

N,M=map(int,input().split())
arr = [list(map(int, input().split()))for _ in range(N)]
T=0
T_total=0 # 所有树剩余苹果的总数
k=0
P=[] # 存储每棵树疏果的总数量
P_count=0
for ap in arr:
    T_total+=ap[0]
    for i in range(1,M+1):
        P_count+=abs(ap[i])
    P.append(P_count)
    P_count=0
for i in range(N):
    if max(P)==P[i]: #疏果个数最多的苹果树编号
        k=i+1
        break
T_total-=sum(P)
print(T_total,k,P[k-1]) #P[k-1]，第k个苹果树的疏果个数
