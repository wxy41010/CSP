arr = list(map(int, input().split()))
ans = 0
count = 0  # 连续跳到方块中心的次数
for i in arr:
    if i == 1:
        ans += 1
        count = 0  # 跳到方块上但不在中心，count重置
    elif i == 2:
        count += 1
        ans += 2 * count  # 每次跳到方块中心时，得分增加 2 * count
    elif i == 0:
        break  # 跳跃失败，结束游戏
print(ans)
