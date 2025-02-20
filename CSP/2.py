# def moves(n,queries):
#     result=[]
#     for x,y,remove in queries:
#         for move in remove:
#             if move=="f" and y+1<=n:
#                 y+=1
#             elif move=="b" and y-1>=1:
#                 y-=1
#             elif move=="l"and x-1>=1:
#                 x-=1
#             elif move=="r"and x+1<=n:
#                 x+=1
#         result.append(f"{x} {y}")
#     return result
#
# n,k=map(int,input().split())
# queries=[]
# for _ in range(k):
#     x,y,move=input().split()
#     queries.append((int(x),int(y),move))
#
# for result in moves(n,queries):
#     print(result)


# def main():
#     # 读取n的值
#     n = int(input())
#     length = n + 1  # 数组a和b的长度是n+1
#     # 读取a数组的元素，输入是一行空格分隔的数字，将它们转换为整数并存入a数组
#     a = list(map(int, input().split()))
#     # 初始化b数组，长度为n+1，所有元素初始为0
#     b = [0] * length
#     # 读取b数组的值，从输入的第二行获取空格分隔的整数
#     b_values = list(map(int, input().split()))
#     # 将输入的b数组值赋给b数组，从索引1开始填充
#     for i in range(1,length):
#         b[i]=b_values[i-1]
#     for i in range(1,length):
#         sum=0
#         temp=b[i]
#         b[i]=0
#         max_ans =0
#         for j in range(1,length):
#             sum=sum+a[j]-b[j]
#             ans=max(sum+a[0],a[0]) #当前步骤的最小初始能量
#             max_ans = max(max_ans, ans)  # 记录全局最大 `ans`，走完一圈的最小初始能量
#         b[i]=temp
#         print(max_ans,end=" ")
#
# if __name__ == "__main__":
#     main()

# def calculate_min_initial_energy(n, a, b_values):
#     length = n + 1  # 区域数量是 n + 1
#     b = length * [0]  # 初始化补给数组
#     for i in range(1, length):
#         b[i] = b_values[i - 1]  # 将补给数组赋值
#
#     results = []
#
#     # 遍历每个区域，计算如果该区域没有补给时所需的最小初始能量
#     for i in range(1, length):
#         temp = b[i]  # 保存当前区域的补给值
#         sum = 0  # 剩余能量初始化为 0
#         b[i] = 0  # 假设该区域没有能量补给
#         max_ans = 0  # 用于记录最小初始能量
#         for j in range(1, length):  # 遍历整个区域
#             sum = sum + a[j] - b[j]  # 更新剩余能量
#             ans = max(sum + a[0], a[0])  # 计算在初始能量为 a[0] 时的剩余能量
#             max_ans = max(ans, max_ans)  # 更新最大值
#         b[i] = temp  # 恢复补给值
#         results.append(max_ans)  # 存储结果
#
#     return results
#
#
# n = int(input())  # 输入区域数量 n
# a = list(map(int, input().split()))  # 每个区域的能量消耗
# b_values = list(map(int, input().split()))  # 各个区域的补给能量
#
# # 调用封装的函数计算最小初始能量
# results = calculate_min_initial_energy(n, a, b_values)
#
# # 输出结果
# print(" ".join(map(str, results)))

#
# def dreamfind(n,a,b_value):
#     length=n+1
#     b=[0]*length
#     for i in range(1,length):
#         b[i]=b_value[i-1]
#
#     results=[]
#     for i in range(1,length):
#         temp=b[i]
#         sum=0
#         b[i]=0
#         maxans=0
#         for j in range(1,length):
#             sum=sum+a[j]-b[j]
#             ans=max(sum+a[0],a[0])
#             maxans=max(ans,maxans)
#         b[i]=temp
#         results.append(maxans)
#     return results
# n=int(input())
# a=list(map(int,input().split()))
# b_value=list(map(int,input().split()))
# # result= dreamfind(n,a,b_value)
# # print(" ".join(map(str,result)))
#
# for result in dreamfind(n,a,b_value):
#     print(result,end=" ")




def dreamfind(n,a,b_value):
    length =n+1
    b=[0]*length
    result=[]
    for i in range(1,length):
        b[i]=b_value[i-1]
    for i in range(1,length):
        temp=b[i]
        b[i]=0
        sum=0
        maxans=0
        for j in range(1,length):
            sum=sum+a[j]-b[j]
            ans=max(sum+a[0],a[0])
            maxans=max(ans,maxans)
        b[i]=temp
        result.append(maxans)
    return result

n=int(input())
a=list(map(int,input().split()))
b_value=list(map(int,input().split()))
for result in dreamfind(n,a,b_value):
    print(result,end=" ")

