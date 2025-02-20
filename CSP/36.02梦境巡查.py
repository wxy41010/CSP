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
#     for i in range(1, length):
#         b[i] = b_values[i - 1]  # 填充b数组，从b[1]到b[n]
#     # 对每个i从1到n，计算结果并输出
#     for i in range(1, length):
#         ans = 0  # 初始化答案
#         sum = 0  # 初始化当前和
#         temp = b[i]  # 临时保存b[i]的值
#         b[i] = 0  # 将b[i]置为0，进行计算
#         # 遍历整个数组，更新sum并计算最小值
#         for j in range(length):
#             sum = sum - a[j] + b[j]  # 更新sum，减去a[j]加上b[j]
#             ans = min(ans, sum)  # 更新最小值
#         # 恢复b[i]的值
#         b[i] = temp
#         # 输出当前的最小值的绝对值
#         print(abs(ans), end=" ")
#
#     # 输出换行符，结束一行的输出
#     print()
#
# if __name__ == "__main__":
#     main()
n=int(input())
a=list(map(int,input().split()))
b_value=list(map(int,input().split()))
def main(n,a,b_value):
    length=n+1
    b=[0]*length
    for i in range(1,length):
        b[i]=b_value[i-1]
    result=[]
    for i in range(1,length):
        temp=b[i]
        b[i]=0
        sum=0
        maxans=0
        for j in range(1,length):
            sum=sum+a[j]-b[j]
            ans=max(sum+a[0],a[0])
            maxans=max(maxans,ans)
        b[i]=temp
        result.append(maxans)
    return result

for r in main(n,a,b_value):
    print(r,end=" ")

"""
3
9 4 6 2
9 4 6
"""
"""
15 10 9
"""
