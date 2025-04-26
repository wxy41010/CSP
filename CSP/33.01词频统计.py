n, m = map(int, input().split())  # n: 文章数, m: 单词编号上限
matrix=[list(map(int,input().split()))[1:] for _ in range(n) ]
# 初始化两个列表
article_count = [0] * (m + 1)  # 记录每个单词出现的文章数
total_count = [0] * (m + 1)  # 记录每个单词出现的总次数
# 遍历每篇文章
for arr in matrix:
    appeared = set()  # 用集合记录每篇文章中出现过的单词，避免重复计算
    for word in arr:
        total_count[word] += 1  # 每次遇到 word，就增加其总出现次数
        if word not in appeared:  # 如果 word 还没有在当前文章中出现过
            article_count[word] += 1  # 增加该单词出现在文章中的篇数
            appeared.add(word)  # 将 word 加入到 appeared 集合，表示它在当前文章中已经出现过
# 输出结果
for i in range(1, m + 1):
    print(article_count[i], total_count[i])
'''
4 3
5 1 2 3 2 1
1 1
3 2 2 2
2 3 2

2 3
3 6
2 2

'''
