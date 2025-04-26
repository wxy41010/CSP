n, a, b = map(int, input().split())
u = []
for _ in range(a):
    index, value = map(int, input().split())
    u.append((index, value))
# 读取向量 v 的稀疏表示
v = []
for _ in range(b):
    index, value = map(int, input().split())
    v.append((index, value))
# 计算内积
dot_product = 0
i = 0  # u 的指针
j = 0  # v 的指针
# 双指针遍历，找相同 index 的乘积
while i < a and j < b:
    if u[i][0] == v[j][0]:  # index 相同
        dot_product += u[i][1] * v[j][1]  # value 相乘
        i += 1
        j += 1
    elif u[i][0] < v[j][0]:  # u 的 index 较小
        i += 1
    else:  # v 的 index 较小
        j += 1
# 输出结果
print(dot_product)