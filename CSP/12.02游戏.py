
# 输入
n, k = map(int, input().split())
# 创建小朋友列表，编号从1到n
kids = list(range(1, n + 1))
num = 1 # 当前报数
index = 0 # 当前检查的索引
while len(kids) > 1:
    # 如果当前报数是k的倍数或个位是k，则淘汰
    if num % k == 0 or num % 10 == k:
        kids.pop(index)
        # 如果移除了元素，不增加index，因为后面的元素会前移
    else:
        # 没有移除时才移动到下一个
        index += 1
    # 报数增加
    num += 1
    # 如果到达列表末尾，从头开始
    if index >= len(kids):
        index = 0
print(kids[0])