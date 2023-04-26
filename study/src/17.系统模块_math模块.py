import math
import random
import datetime
import time
import calendar
# ----------math系统模块-------
# 官方文档：https://docs.python.org/zh-cn/3.11/library/math.html


# 向下取整
print(math.floor(4.2))  # 4  
# 向上取整
print(math.ceil(4.2))   # 5  
# 四舍五入(math内没有round方法)
print(round(4.6))       # 5

# 幂运算
print(math.pow(2, 3))  # 8.0 
# pow(2, 3)
# 2 ** 3

# 三角函数 pi=180°
print(math.sin(math.pi / 6))  # 0.49999999999999994
print(math.cos(math.pi / 3))  # 0.5000000000000001
print(math.tan(math.pi / 4))  # 0.9999999999999999





# ----------random随机数模块-------
# 官方文档：https://docs.python.org/zh-cn/3.11/library/random.html


# 生成[a,b]范围内的随机整数
print(random.randint(2, 5))   # 4
# 生成[a,b)范围内的随机整数
print(random.randrange(2, 5)) # 3

# 生成[0,1)范围内的随机数
print(random.random())  # 0.45400357916352896

# 在可迭代对象里随机抽取一个数据
print(random.choice(['牛', '青', '山'])) # 山

# 在可迭代对象里随机抽取多个数据,以数组形式返回
print(random.sample(['牛', '青', '山'], 2)) # ['青', '山']
print(random.sample(('牛', '青', '山'), 2)) # ['青', '牛']



# ----------datetime日期时间模块-------
# 官方文档：https://docs.python.org/zh-cn/3.11/library/datetime.html
''' 
datetime模块内的类：
    date：用来显示日期
    time：用来显示时间
    datetime：用来显示日期时间
    timedelta：用来计算时间
'''
# 创建一个日期
print(datetime.date(2022, 12, 12))  # 2022-12-12
# 创建一个时间
print(datetime.time(15, 30, 11))    # 15:30:11
# 获取当前日期和时间
print(datetime.datetime.now())                          # 2023-04-26 22:56:48.969704
# 计算三天以后的时间
print(datetime.datetime.now() + datetime.timedelta(3))  # 2023-04-29 22:56:43.272681






# ----------time时间模块-------
# 官方文档：https://docs.python.org/zh-cn/3.11/library/time.html
# time模块不仅能显示时间，还可以控制程序，让程序暂停(sleep函数)

# 从1970.01.01 UTC零点到现在的秒数
print(time.time())  # 1682521223.727482
# 按照制定格式输出时间
print(time.strftime("%Y-%m-%d %H:%M:%S"))  # 2023-04-26 23:02:18
# 打印 周几 月 日 时间 年           time.asctime(元组)
print(time.asctime()) # Wed Apr 26 23:03:26 2023
# 另外一种打印 周几 月 日 时间 年   time.ctime("时间戳")
print(time.ctime()) # Wed Apr 26 23:03:26 2023
# 睡眠几秒
time.sleep(1)




# ----------calendar日历模块-------
# 官方文档：https://docs.python.org/zh-cn/3.11/library/calendar.html

# 设置每周的起始日期是周几 周一到周日分别对应0~6
calendar.setfirstweekday(calendar.SUNDAY)
# 返回每周的起始日期。默认情况返回0即周一
print(calendar.firstweekday()) # 6
# 打印某一年的日历
print(calendar.calendar(2022))
# 打印某个月的日历
print(calendar.month(2023, 10))
# 是否是闰年
print(calendar.isleap(2020)) # True
# 打印xxxx年~yyyy年中间有多少个闰年
print(calendar.leapdays(2001, 2009)) # 2
