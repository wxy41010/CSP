# import re
# from collections import Counter
#
# def check_password_security(password):
#     # 判断密码是否包含字母、数字和特殊字符
#     contains_letters = bool(re.search(r'[a-zA-Z]', password))
#     contains_digits = bool(re.search(r'\d', password))
#     contains_special = bool(re.search(r'[\*\#]', password))
#     if not (contains_letters and contains_digits and contains_special):
#         return 0  # 如果缺少字母、数字或特殊字符，则为低安全度
#     # 判断字符是否超过2次
#     char_count = Counter(password)
#     if any(count > 2 for count in char_count.values()):
#         # 如果某个字符出现超过2次，属于中安全度
#         return 1
#     # 如果满足高安全度条件
#     return 2
#
# n = int(input())  # 输入待判别密码的个数
# for _ in range(n):
#     password = input().strip()  # 读取每个密码
#     print(check_password_security(password))  # 输出对应的安全度
#

# def check_crypto_security(password):
#     a=False
#     b=False
#     c=False
#     for char in password:
#         if char.isalpha():
#             a=True
#         elif char.isdigit():
#             b=True
#         elif char in "*#":
#             c=True
#     if not (a and b and c):
#         return 0
#
#     arr={}
#     for char in password:
#         if char in arr:
#             arr[char]+=1
#         else:
#             arr[char]=1
#     for count in arr.values():
#         if count >2:
#             return 1
#     return 2
#
# n=int(input())
# for _ in range(n):
#     password=input().strip()
#     print(check_crypto_security(password))

# def check_password(password):
#     a=False
#     b=False
#     c=False
#     for i in password:
#         if i.isalpha():
#             a=True
#         elif i.isdigit():
#             b=True
#         elif i in "*#":
#             c=True
#     if not (a and b and c):
#         return 0
#
#     arr={}
#     for char in password:
#         if char in arr:
#             arr[char]+=1
#         else:
#             arr[char]=1
#     for count in arr.values():
#         if count>2:
#             return 1
#     return 2
#
# n=int(input())
# for _ in range(n):
#     password=input().strip()
#     print(check_password(password))
#
#
def checkpassword(password):
    a=False
    b=False
    c=False
    for i in password:
        if i.isalpha():
            a=True
        elif i.isdigit():
            b=True
        elif i in "*#":
            c=True
    if not (a and b and c):
        return 0
    arr={}
    for j in password:
        if j in arr:
            arr[j]+=1
        else:
            arr[j]=1
    for count in arr.values():
        if count>2:
            return 1
    return 2
n=int(input())
for _ in range(n):
    password=input().strip()
    print(checkpassword(password))

