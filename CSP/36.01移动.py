def moves(n,arr):  # 定义一个函数moves，接受网格大小n和移动指令数组arr作为参数
    result=[]  # 创建一个空列表，用于存储每个移动序列的最终位置
    for x,y,move in arr:  # 遍历arr中的每个元组，解包为起始x坐标、y坐标和移动指令字符串
        for m in move:  # 遍历移动指令字符串中的每个字符m
            if m=="f" and y+1<=n:  # 如果指令是"f"（向前）且移动后y坐标不超过网格上限n
                y+=1  # y坐标加1（向上移动）
            elif m=="b" and y-1>=1:  # 如果指令是"b"（向后）且移动后y坐标不小于1
                y-=1  # y坐标减1（向下移动）
            elif m=="l" and x-1>=1:  # 如果指令是"l"（向左）且移动后x坐标不小于1
                x-=1  # x坐标减1（向左移动）
            elif m=="r" and x+1<=n:  # 如果指令是"r"（向右）且移动后x坐标不超过网格上限n
                x+=1  # x坐标加1（向右移动）
        result.append(f"{x} {y}")  # 将最终的x和y坐标以字符串形式（"x y"）添加到结果列表
    return result  # 返回所有移动序列的最终位置列表
n,k=map(int,input().split())  # 获取输入的网格大小n和移动序列数量k，转换为整数
arr=[]  # 创建一个空列表，用于存储移动序列数据
for _ in range(k):  # 循环k次，处理每条移动序列
    x,y,move=input().split()  # 获取输入的起始x坐标、y坐标和移动指令字符串，并分割
    arr.append((int(x),int(y),move))  # 将x和y转换为整数，与move组成元组，添加到arr列表
for result in moves(n,arr):  # 调用moves函数并遍历返回的结果
    print(result)  # 打印每条移动序列的最终位置
