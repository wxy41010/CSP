n,m=map(int,input().split()) #n 仓库个数 ；m 编码维数
matrix=[list(map(int,input().split()))for _ in range(n)]
result=[0]*n # 结果数组，默认为0表示没有上级仓库
for i in range(n):
    for j in range(n):
        if i!=j: #可以删除这个判断，不过能快速省略一步
            if all(matrix[j][k]>matrix[i][k]for k in range(m)):
                if result[i]==0 or result[i]>j+1:
                    result[i]=j+1
for i in result:
    print(i)

"""
4 2
0 0
-1 -1
1 2
0 -1

3
1
0
3
"""