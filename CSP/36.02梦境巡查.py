n=int(input())  # 获取输入的整数n，表示数组的长度
a=list(map(int,input().split()))  # 获取输入的数组a，转换为整数列表
b_value=list(map(int,input().split()))  # 获取输入的数组b_value，转换为整数列表
def main(n,a,b_value):  # 定义main函数，接受长度n、数组a和b_value作为参数
    length=n+1  # 定义length为n+1，因为数组索引从1开始计算
    b=[0]*length  # 创建一个长度为length的列表b，初始化全为0
    for i in range(1,length):  # 遍历从1到length-1的索引
        b[i]=b_value[i-1]  # 将b_value的值赋给b数组，从b[1]开始填充
    result=[]  # 创建一个空列表，用于存储每次计算的最大结果
    for i in range(1,length):  # 遍历从1到length-1的索引，依次处理b[i]
        temp=b[i]  # 保存b[i]的原始值，以便后续恢复
        b[i]=0  # 将b[i]置为0，模拟移除该位置的影响
        sum=0  # 初始化累加和为0
        maxans=0  # 初始化最大答案为0
        for j in range(1,length):  # 遍历从1到length-1的索引，计算每次的和
            sum=sum+a[j]-b[j]  # 更新累加和，计算a[j]-b[j]的差值累加
            ans=max(sum+a[0],a[0])  # 计算当前答案，取sum+a[0]和a[0]的最大值
            maxans=max(maxans,ans)  # 更新最大答案，取当前maxans和ans的最大值
        b[i]=temp  # 恢复b[i]的原始值
        result.append(maxans)  # 将本次计算的最大答案添加到结果列表
    return result  # 返回所有计算结果的列表

for r in main(n,a,b_value):  # 遍历main函数返回的结果
    print(r,end=" ")  # 打印每个结果，末尾用空格分隔

"""
3
9 4 6 2
9 4 6

15 10 9
"""
