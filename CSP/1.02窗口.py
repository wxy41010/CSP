import functools  # 导入 functools 库，用于比较函数

# 读取窗口数量 n 和点击次数 m
n, m = map(int, input().split())
windows = []  # 用来存储所有窗口的信息
click = []    # 用来存储所有点击位置的信息
# 读取窗口的信息：坐标 (x1, y1) 到 (x2, y2)，窗口的编号和层级
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    windows.append([x1, y1, x2, y2, i + 1, n - i])  # 每个窗口的结构：[x1, y1, x2, y2, 窗口编号, 层级]
# 读取点击位置的信息：点击位置 (x, y)
for i in range(m):
    x, y = map(int, input().split())
    click.append([x, y])
# 比较函数，用于根据窗口层级进行排序
def cmp(a, b):
    if a[-1] > b[-1]:  # 如果窗口 a 的层级大于 b 的层级
        return 1  # 返回 1 表示 a 排在 b 前面
    return -1  # 否则，返回 -1 表示 b 排在 a 前面
# 处理每次点击事件
def cout(lst):
    # 先根据层级从大到小排序窗口，确保层级高的窗口排在前面
    windows.sort(key=functools.cmp_to_key(cmp))  # 将 cmp 函数转化为 key 函数来进行排序
    # 遍历所有窗口，判断是否有窗口被点击
    for j in windows:
        if lst[0] >= j[0] and lst[0] <= j[2] and lst[1] >= j[1] and lst[1] <= j[3]:  # 如果点击位置在窗口内
            # 点击到窗口后，更新窗口层级，使当前窗口置于最顶层
            for k in windows:
                if k[-1] < j[-1]:  # 对比每个窗口的层级，如果窗口 k 的层级小于 j 的层级
                    k[-1] = k[-1] + 1  # 层级加 1，升到上面
                else:
                    break  # 一旦遇到层级大于等于 j 的窗口，就停止
            j[-1] = 1  # 当前窗口层级设置为 1，表示它是最上层窗口
            return j[-2]  # 返回窗口的编号（即窗口的第 5 个元素，编号存储在 j[-2]）
    return "IGNORED"  # 如果点击的区域不在任何窗口内，返回 "IGNORED"
# 处理每次点击事件并打印结果
for i in click:
    print(cout(i))  # 对每次点击调用 cout 函数并打印窗口编号或 "IGNORED"
