## 几个move字符串--几个输出坐标
# def process_queries(n, queries):
#     results = []
#     for x, y, instructions in queries:
#         for move in instructions:
#             if move == 'f' and y + 1 <= n:
#                 y += 1
#             elif move == 'b' and y - 1 >= 1:
#                 y -= 1
#             elif move == 'l' and x - 1 >= 1:
#                 x -= 1
#             elif move == 'r' and x + 1 <= n:
#                 x += 1
#         results.append(f"{x} {y}")
#
#     return results
#
# # 读取输入
# n, k = map(int, input().split())
# queries = []
# for _ in range(k):
#     x, y, moves = input().split()
#     queries.append((int(x), int(y), moves))
#
# # 处理查询并输出结果
# for result in process_queries(n, queries):
#     print(result)
def moves(n,arr):
    result=[]
    for x,y,move in arr:
        for m in move:
            if m=="f"and y+1<=n:
                y+=1
            elif m=="b"and y-1>=1:
                y-=1
            elif m=="l"and x-1>=1:
                x-=1
            elif m=="r"and x+1<=n:
                x+=1
        result.append(f"{x} {y}")
    return result
n,k=map(int,input().split())
arr=[]
for _ in range(k):
    x,y,move=input().split()
    arr.append((int(x),int(y),move))
for result in moves(n,arr):
    print(result)