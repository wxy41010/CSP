def checkpassword(password):  # 定义一个名为checkpassword的函数，接受一个密码字符串作为输入
    a=False  # 初始化标志'a'为False，用于跟踪密码中是否含有字母
    b=False  # 初始化标志'b'为False，用于跟踪密码中是否含有数字
    c=False  # 初始化标志'c'为False，用于跟踪密码中是否含有'*'或'#'
    for i in password:  # 遍历密码字符串中的每个字符'i'
        if i.isalpha():  # 检查当前字符是否为字母
            a=True  # 如果找到字母，将标志'a'设置为True
        elif i.isdigit():  # 检查当前字符是否为数字
            b=True  # 如果找到数字，将标志'b'设置为True
        elif i in "*#":  # 检查当前字符是否为'*'或'#'
            c=True  # 如果找到'*'或'#'，将标志'c'设置为True
    if not (a and b and c):  # 检查是否所有条件（字母、数字、特殊字符）都满足
        return 0  # 如果任一条件不满足，返回0
    arr={}  # 创建一个空字典，用于统计每个字符出现的次数
    for j in password:  # 再次遍历密码中的每个字符'j'
        if j in arr:  # 如果字符已在字典中
            arr[j]+=1  # 将该字符的计数增加1
        else:  # 如果字符不在字典中
            arr[j]=1  # 初始化该字符的计数为1
    for count in arr.values():  # 遍历字典中所有字符的计数
        if count>2:  # 检查是否有字符出现次数超过2次
            return 1  # 如果有字符出现超过2次，返回1
    return 2  # 如果所有条件满足且无字符重复超过2次，返回2
n=int(input())  # 从用户输入获取测试用例的数量，并转换为整数
for _ in range(n):  # 循环n次，处理每个测试用例
    password=input().strip()  # 获取用户输入的密码字符串并去除首尾空格
    print(checkpassword(password))  # 调用checkpassword函数并打印结果

"""
4
csp#ccsp
csp#ccsp2024
Csp#ccsp2024
CSP#2024

0
1
2
2
"""