def tetris_fall(init_matrix, square, start_col):
    rows, cols = 15, 10
    # 方块的宽度和高度
    block_h = 4
    block_w = 4
    # 检测方块可以落到的位置
    def can_place(r, c):
        for i in range(block_h):
            for j in range(block_w):
                if square[i][j]:  # 只有在有方块的位置才需要检查
                    if r + i >= rows or init_matrix[r + i][c + j]:  # 超出边界或已有方块
                        return False
        return True
    # 找到方块能落下的最低位置
    start_col -= 1  # 题目给的是从1开始的列索引，需要转换为0索引
    drop_row = 0
    while can_place(drop_row+1, start_col):#当第一行不满足时，drop_row=0
        drop_row += 1
    # 放置方块
    for i in range(block_h):
        for j in range(block_w):
            if square[i][j]:
                init_matrix[drop_row + i][start_col + j] = 1
    return init_matrix
# 读取输入
init_matrix = [list(map(int, input().split())) for _ in range(15)]
square = [list(map(int, input().split())) for _ in range(4)]
start_col = int(input())
# 计算最终状态并输出
result = tetris_fall(init_matrix, square, start_col)
for row in result:
    print(*row)
