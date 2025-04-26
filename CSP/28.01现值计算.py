n,i=input().split()  # 获取输入的字符串，包含两个值n和i，用空格分隔
n,i=int(n),float(i)  # 将n转换为整数，i转换为浮点数
ans=0  # 初始化答案变量ans为0，用于累加计算结果
arr=list(map(int,input().split()))  # 获取输入的数组arr，转换为整数列表
for k in range(n+1):  # 遍历从0到n的索引k
    ans+=arr[k]*(1+i)**(-k)  # 计算每项arr[k]*(1+i)的-k次幂，并累加到ans
print(f"{ans:.3f}")  # 将结果ans格式化为保留3位小数并打印

"""
2 0.05
-200 100 100

-14.059
"""















