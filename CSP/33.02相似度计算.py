n, m = map(int, input().split())  # 读取两个正整数n和m
words1 = input().split()  # 读取第一篇文章的单词
words2 = input().split()  # 读取第二篇文章的单词
# 将单词转换为小写并转化为集合去重
set1 = set(word.lower() for word in words1)
set2 = set(word.lower() for word in words2)
# 计算交集和并集
intersection = set1 & set2  # 交集
union = set1 | set2  # 并集
# 输出结果
print(len(intersection))  # 交集的大小
print(len(union))  # 并集的大小

"""
9 7
Par les soirs bleus dete jirai dans les sentiers
PICOTE PAR LES BLES FOULER LHERBE MENUE

2
13
"""
