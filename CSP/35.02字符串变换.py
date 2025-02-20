# def process_queries():
#     # Step 1: 读取输入数据
#     initial_str = input()[1:-1]  # 去掉两侧的井号 #
#     n = int(input())  # 替换对的数量
#     replace_dict = {}
#
#     # Step 2: 构建替换函数
#     for _ in range(n):
#         rule = input()[1:-1]  # 去掉井号 #
#         f_from, f_to = rule[0], rule[1]
#         replace_dict[f_from] = f_to
#
#     # Step 3: 读取查询数量
#     m = int(input())  # 查询次数
#     queries = list(map(int, input().split()))  # 查询的次数列表
#
#     # Step 4: 定义替换函数
#     def transform(s, k):
#         for _ in range(k):
#             s = ''.join(replace_dict.get(ch, ch) for ch in s)
#         return s
#
#     # Step 5: 对每个查询进行处理并输出结果
#     for k in queries:
#         result = transform(initial_str, k)
#         print(f"#{result}#")
#
# # 调用函数执行
# process_queries()


# def main():
#     initstr=input()[1:-1]
#     n=int(input())
#     replace={}
#     for _ in range (n):
#         tran=input()[1:-1]
#         f_from,f_to=tran[0],tran[1]
#         replace[f_from]=f_to
#     m=int(input())
#     list1=list(map(int,input().split()))
#     def transform(s,m):
#         for _ in range(m):
#             s="".join(replace.get(ch,ch) for ch in s)
#         return s
#     for k in list1:
#         result=transform(initstr,k)
#         print(f"#{result}#")
# main()

"""
#Hello World#
6
#HH#
#e #
# r#
#re#
#oa#
#ao#
3
1 2 3
"""

"""
#H llarWaeld#
#HrlloeWo ld#
#Hella Warld#
"""
# # 读取输入数据
# initstr = input().strip()[1:-1]  # 读取并去掉前后引号
# n = int(input().strip())  # 读取替换规则的个数
# replace = {}
# # 读取替换规则
# for _ in range(n):
#     tran = input().strip()[1:-1]  # 读取并去掉前后引号
#     f_from, f_to = tran[0], tran[1]  # 获取替换对
#     replace[f_from] = f_to
# # 读取转换次数
# m = int(input().strip())
# # 读取转换步数的列表
# list1 = list(map(int, input().split()))
# def main():
#     """执行字符串转换并输出结果"""
#     for k in list1:
#         s = initstr
#         for _ in range(k):
#             s = "".join(replace.get(ch, ch) for ch in s)
#         print(f"#{s}#")
# # 运行主函数
# main()


arr=input()[1:-1]
n=int(input())
replace={}
for _ in range(n):
    char=input()[1:-1]
    f_from,f_to=char[0],char[1]
    replace[f_from]=f_to
m=int(input())
list1=list(map(int,input().split()))
def main(replace,list1):
    for k in list1:
        s=arr
        for _ in range(k):
            s="".join(replace.get(ch,ch)for ch in s)
        print(f"#{s}#")
main(replace,list1)
