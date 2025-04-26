n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# 记录需要消除的位置
to_remove = [[False] * m for _ in range(n)]
# 检查行
for i in range(n):
    j = 0
    while j < m - 2:
        if arr[i][j] == arr[i][j + 1] == arr[i][j + 2]:
            k = j
            while k < m and arr[i][k] == arr[i][j]:  # 继续标记直到不同
                to_remove[i][k] = True
                k += 1
        j += 1
# 检查列
for j in range(m):
    i = 0
    while i < n - 2:
        if arr[i][j] == arr[i + 1][j] == arr[i + 2][j]:
            k = i
            while k < n and arr[k][j] == arr[i][j]:  # 继续标记直到不同
                to_remove[k][j] = True
                k += 1
        i += 1
# 生成新棋盘
for i in range(n):
    for j in range(m):
        if to_remove[i][j]:
            arr[i][j] = 0
# 输出结果
for row in arr:
    print(*row)


    # 检查列时，while k < n and arr[k][j] == arr[i][j] 依赖于 arr[i][j] 的原始值
    # 所以不能直接在原表上修改，除非是需要满足没有三个相同元素相连接的情况即可时
