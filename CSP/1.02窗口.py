# 模拟点击窗口
"""
    思路:
    1) 接收输入窗口数目 n 点击次数 m
    2) 将每一个输入的窗口保存为一个列表 win_list 将每一次点击也以列表形式保存 click_list
    3) 遍历 click_list 然后依次在 win_list 中检查该次点击是否输入该窗口(下标最大的元素为最上层窗口)
    4) 找到对应的窗口后,移动窗口位置,将其置于最上层,也就是成为列表的最后一个元素
"""
# n, m = map(int, input().split())
# win_list = [list(map(int, input().split())) + [i + 1] for i in range(n)]
# click_list = [list(map(int, input().split())) for _ in range(m)]
# for k in range(m):
#     # 遍历点击事件
#     x, y = click_list[k]
#     idx = n - 1  #最顶层开始遍历到最底层
#     while idx >= 0:
#         flag = False  # 假设没有找到鼠标点击的窗口
#         if win_list[idx][0] <= x <= win_list[idx][2] and win_list[idx][1] <= y <= win_list[idx][3]:
#             # 判断点击是否在窗口内
#             flag = True
#             print(win_list[idx][4])
#             # 如果在窗口内,则调整 win_list
#             # 采用先pop()再添加的策略，因为列表会自动维护顺序
#             move_win = win_list.pop(idx)
#             win_list.append(move_win) #列表的最后代表最顶层
#             # 找到窗口后,跳出while循环,依次检查下一次的点击
#             break
#         idx -= 1
#     if not flag:
#         print("IGNORED")


n,m = map(int,input().split())
win=[list(map(int,input().split())) +[i+1] for i in range(n)]
click=[list(map(int,input().split())) for _ in range(m)]
for j in range(m): # 遍历每个点击
    idx=n-1
    x,y=click[j]
    while idx>=0:# 遍历每个窗口
        flag=False
        if win[idx][0]<=x<=win[idx][2] and win[idx][1]<=y<=win[idx][3]:
            print(win[idx][4])
            flag=True
            move=win.pop(idx)
            win.append(move)
            break
        idx-=1
    if not flag:
        print("IGNORED")