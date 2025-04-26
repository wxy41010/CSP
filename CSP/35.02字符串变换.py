# arr=input()[1:-1]  # 获取用户输入的字符串，并去掉首尾字符（通常是括号或引号）
# n=int(input())  # 获取替换规则的数量，并转换为整数
# replace={}  # 创建一个空字典，用于存储字符替换规则
# for _ in range(n):  # 循环n次，处理每条替换规则
#     char=input()[1:-1]  # 获取用户输入的替换对字符串，并去掉首尾字符
#     f_from,f_to=char[0],char[1]  # 从替换对中提取起始字符f_from和目标字符f_to
#     replace[f_from]=f_to  # 将替换规则（f_from -> f_to）存入字典
# m=int(input())  # 获取需要处理的替换次数列表的长度，并转换为整数
# list1=list(map(int,input().split()))  # 获取替换次数列表，转换为整数列表
# def main(replace,list1):  # 定义main函数，接受替换规则字典和替换次数列表作为参数
#     for k in list1:  # 遍历替换次数列表中的每个数字k
#         s=arr  # 将初始字符串arr赋值给变量s
#         for _ in range(k):  # 对字符串执行k次替换操作
#             s="".join(replace.get(ch,ch)for ch in s)  # 对s中的每个字符ch应用替换规则，若无规则则保持原字符
#         print(f"#{s}#")  # 打印替换后的字符串，首尾添加'#'符号
# main(replace,list1)  # 调用main函数，传入替换规则和替换次数列表

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

#H llarWaeld#
#HrlloeWo ld#
#Hella Warld#
"""
