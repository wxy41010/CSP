n, k = map(int, input().split())  # n: 变量个数，k: 赋值语句条数
say = [list(map(int, input().split())) for _ in range(k)]  # 读取k条赋值语句
initialized = set()  # 用来记录已经初始化的变量
count = 0  # 记录右值未初始化的赋值语句的数量
for x, y in say:
    if y > 0 and y not in initialized:  # y不为常量且未初始化
        count += 1
    initialized.add(x)  # 将左值x加入已初始化的集合
print(count)
