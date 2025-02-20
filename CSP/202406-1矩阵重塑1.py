def read_matrix(total_elements):
    """读取矩阵元素，并返回一个列表"""
    return list(map(int, input().split()))

def print_matrix(arr, rows, cols):
    """按指定格式打印矩阵"""
    t = 0  # 数组的索引
    for i in range(rows):  # 遍历每一行
        for j in range(cols):  # 遍历当前行的每一列
            print(arr[t], end=" ")  # 打印当前元素
            t += 1
        print()  # 换行

def main():
    # 读取矩阵的维度
    n, m, p, q = map(int, input().split())
    # 计算矩阵的总元素数量
    total_elements = n * m
    # 读取矩阵元素
    arr = read_matrix(total_elements)
    # 按 p 行 q 列的格式打印矩阵
    print_matrix(arr, p, q)

if __name__ == "__main__":
    main()
