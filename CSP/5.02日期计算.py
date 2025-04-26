y = int(input())
d = int(input())
# 判断是否是闰年
is_leap = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
# 各月份的天数
month_days = [31, 29 if is_leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 计算对应的月份和日期
month, day = 0, d
for i, days in enumerate(month_days):
    if day <= days:
        month = i + 1
        break
    day -= days
print(month)
print(day)

# 2015
# 80

# 3
# 21
