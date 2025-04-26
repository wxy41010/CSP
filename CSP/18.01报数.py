n=int(input())
count=1
realcount=0
list=[0,0,0,0] # 初始化四个玩家的跳过次数
player=0 # 轮流报数的玩家，甲(0), 乙(1), 丙(2), 丁(3)
while realcount<n:
    if count%7==0 or '7' in str(count):
        list[player]+=1 # 如果跳过，则增加对应玩家的跳过次数
    else:# 否则增加有效报数
        realcount+=1
    count+=1
    player=(player+1)%4
for i in list:
    print(i)
