# n, i = input().split()  # 获取字符串输入并拆分
# n, i = int(n), float(i)  # 转换类型
# arr = list(map(int, input().split()))  # 获取收入支出列表
# ans = 0.0
# for k in range(n + 1):
#     ans += arr[k] * (1 + i) ** (-k)  # 计算当前价值
# print(f"{ans:.3f}") # 输出结果，保留3位小数

"""
2 0.05
-200 100 100

-14.059
"""

n,i=input().split()
n,i=int(n),float(i)
ans=0
arr=list(map(int,input().split()))
for k in range(n+1):
    ans+=arr[k]*(1+i)**(-k)
print(f"{ans:.3f}")

















