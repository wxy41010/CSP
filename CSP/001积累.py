a=input()
if a.isalpha():
    print(True)
elif a.isdigit():
    print(True)
else:
    print(False)
import math

math.sqrt(16)  # 4.0  平方根
math.pow(2, 3)  # 8.0  幂运算
math.exp(2)  # e^2
math.log(8, 2)  # 3.0  以2为底的对数
math.sin(math.pi / 2)  # 1.0  正弦
math.cos(0)  # 1.0  余弦
math.tan(math.pi / 4)  # 1.0  正切
math.factorial(5)  # 120  阶乘
math.gcd(48, 18)  # 6  最大公约数
.2

positions = [(coords[i], coords[i+1]) for i in range(0, 2*t, 2)]  # 将坐标序列转换为(x, y)坐标对列表，每对表示一个时间点的坐标

a=list(map(int,input().split(",")))
N=int(input())
n,m=map(int,input().split())
print(sum(map(int, N)))

y = list(range(1, N + 1))

y[y.index(0)]=1

a,b,c=map(float,input().split())


grid = [[False] * 101 for _ in range(101)]  # 初始化101×101的网格
x1, y1, x2, y2 = map(int, input().split())

#4
sorted_items = sorted(count.items(), key=lambda x: (-x[1], x[0]))

#5
month_days = [31, 29 if is_leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#7
# 复制初始矩阵
grid = [row[:] for row in init_matrix]

min_diff = float('inf')  # 初始化最小差值为无穷大

coords = list(map(int, input().split()))
positions = [(coords[i], coords[i+1]) for i in range(0, 2*t, 2)]
# 将坐标序列转换为(x, y)坐标对列表，每对表示一个时间点的坐标

m = int(input())
data = [list(map(int, input().split())) for _ in range(m)]
# 获取所有可能的阈值（去重并排序）
thresholds = sorted(set(y for y, _ in data))

a = list(map(int, input().split()))  # 输入n个整数并转换为列表
avg = sum(a) / n  # 计算平均值
D = sum((x - avg) ** 2 for x in a) / n  # 计算方差

print(f.real)  # 输出实数部分，并且是浮点数格式

for _ in range(n): # 读取矩阵并展平
    arr.extend(map(int,input().split()))

#30.02
import numpy as np
Q = np.array([list(map(int, input().split())) for _ in range(n)])  # n 行 d 列的矩阵 Q
K = np.array([list(map(int, input().split())) for _ in range(n)])  # n 行 d 列的矩阵 K
for i in range(n):
    ans=Q[i] @ K.T  #@ 运算符（矩阵乘法）和 .T（转置）

import heapq
lst = [5, 2, 7, 1, 9]
heapq.heappush(lst, 5)
heapq.heappop(lst)
heapq.heapify(lst)# 输出: [1, 2, 7, 5, 9]
smallest = heapq.nsmallest(3, lst) # 输出: [1, 2, 5]
largest  = heapq.nlargest(3, lst) # 输出: [9, 7, 5]