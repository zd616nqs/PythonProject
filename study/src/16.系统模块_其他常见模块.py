import math
import random
import datetime
import time
import calendar
import hashlib
import hmac
import uuid
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

# 生成[0,1)范围内的随机数
print(random.random())  # 0.45400357916352896
# 生成[a,b]范围内的随机整数
print(random.randint(2, 5))   # 4
# 生成[a,b)范围内的随机整数
print(random.randrange(2, 10)) # 8
print(random.randrange(2, 10, 3)) # 结果在2/5/8内随机出现



# 在可迭代对象里随机抽取一个数据
print(random.choice(['牛', '青', '山'])) # 山

# 在可迭代对象里随机抽取多个数据,以数组形式返回，并且是乱序的
print(random.sample(['牛', '青', '山', '到', '此', '一', '游'], 2)) # ['山', '到']
print(random.sample(('牛', '青', '山', '到', '此', '一', '游'), 2)) # ['青', '游']
print(random.sample(('牛', '青', '山', '到', '此', '一', '游'), 5)) # ['青', '山', '一', '到', '游']



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
# 计算时间间隔三天以后的时间
print(datetime.datetime.now() + datetime.timedelta(3))  # 2023-04-29 22:56:43.272681





# ----------time时间模块-------
# 官方文档：https://docs.python.org/zh-cn/3.11/library/time.html
# 参考链接：https://blog.csdn.net/Huangqingmeng/article/details/110788850
# time模块不仅能显示时间，还可以控制程序，让程序暂停(sleep函数)

'''  
----time.struct_time结构体说明----
下标  属性名       说明          值的范围
0	 tm_year	4位数的年份      2008年
1	 tm_mon	    月              1至12
2	 tm_mday	天              1至31
3	 tm_hour	小时            0至23
4	 tm_min	    分钟            0至59
5	 tm_sec	    秒              0到61（60或61是leap秒）
6	 tm_wday	星期几          0到6（0是星期一）
7	 tm_yday	一年中的一天     1至366（儒略日）
8	 tm_isdst	夏令时          -1、0、1，-1表示库确定DST
'''

# 1.time.time()    时间戳：从1970.01.01 UTC零点到现在的秒数
print(time.time())  # 1682521223.727482

# 2.1 time.strftime  按照指定格式输出 为时间字符串
print(time.strftime("%Y-%m-%d %H:%M:%S"))  # 2023-04-26 23:02:18

# 2.2 time.strptime 按照指定的格式把一个时间字符串 解析为 时间元组
print(time.strptime('2023-04-26 23:02:18', "%Y-%m-%d %H:%M:%S"))

# 3.time.asctime(元组)   打印 周几 月 日 时间 年
print(time.asctime())  # Sun Jun  4 22:12:52 2023

# 4.time.gmtime()  将一个时间戳转换为UTC时区（0时区）的struct_time，可选的参数sec表示从1970-1-1以来的秒数。其默认值为time.time()，函数返回time.struct_time类型的对象
print(time.gmtime())
# 结果：time.struct_time(tm_year=2023, tm_mon=6, tm_mday=4, tm_hour=14, tm_min=22, tm_sec=2, tm_wday=6, tm_yday=155, tm_isdst=0)

# 5.time.localtime(sec) 作用是格式化时间戳为本地的时间。 如果sec参数未输入，则以当前时间为转换标准
# 类似time.gmtime()
print(time.localtime())  
print(time.localtime())  
# 结果：time.struct_time(tm_year=2023, tm_mon=6, tm_mday=4, tm_hour=14, tm_min=22, tm_sec=2, tm_wday=6, tm_yday=155, tm_isdst=0)

# 6.time.ctime() 把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式
# 参数未给时默认会把time.time()设为参数
# 相当于time.asctime(time.localtime())
print(time.ctime())                    # Sun Jun  4 22:23:27 2023
print(time.asctime(time.localtime()))  # Sun Jun  4 22:23:27 2023


# 7. time.mktime(tumple) 把time.struct_time元组转换成时间戳
# 与gmtime()/localtime() 是相反的操作
test_struck_time = (1992, 9, 9, 0, 0, 0, 0, 0, 0)
birthday_timestamp = time.mktime(test_struck_time)
birthday_desc = time.ctime(birthday_timestamp)
print(f"生日时间戳:{birthday_timestamp}       生日日期:{birthday_desc}")   
# 生日时间戳:715968000.0       生日日期:Wed Sep  9 00:00:00 1992

# 8.time.timezone 时区 >0美洲 ,<=0大部分欧洲，亚洲，非洲）
print(time.timezone) # -28800

# 练习:计算两个时间之间的秒数  https://blog.csdn.net/WJUNSING/article/details/107338356
nqs_start_str = "2023:06:01:09:30:00"
nqs_end_str   = "2023:06:01:09:32:00"
for i in range(0, 2):
    if i == 0:
        # 方式1：使用time模块
        nqs_start_time_tuple = time.strptime(nqs_start_str, "%Y:%m:%d:%H:%M:%S")
        nqs_end_time_tuple = time.strptime(nqs_end_str, "%Y:%m:%d:%H:%M:%S")
        start_time_stamp = int(time.mktime(nqs_start_time_tuple))
        end_time_stamp = int(time.mktime(nqs_end_time_tuple))
        time_interval = end_time_stamp - start_time_stamp
        print(f"时间间隔：{time_interval}秒") # 时间间隔：120秒
    else:
        # 方式2：使用datatime模块
        nqs_start_time_tuple = datetime.datetime.strptime(nqs_start_str, "%Y:%m:%d:%H:%M:%S")
        nqs_end_time_tuple = datetime.datetime.strptime(nqs_end_str, "%Y:%m:%d:%H:%M:%S")
        time_interval = (nqs_end_time_tuple - nqs_start_time_tuple).seconds
        print(f"时间间隔：{time_interval}秒") # 时间间隔：120秒

# ------睡眠几秒-----
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




# ----------hashlib哈希模块-------
# 官方文档：https://docs.python.org/zh-cn/3.11/library/hashlib.html

# digest() 返回的是二进制数据
# hexdigest() 返回的是十六进制数据

# md5加密
# 方式1：
test_md5 = hashlib.md5()                # 生成一个md5对象
test_md5.update("牛青山".encode('utf8')) # 加密一段字符串
print(test_md5.hexdigest())             # d7e31ef085af56d4913e83b70da33353
# 方式2：
h0 = hashlib.md5('牛青山'.encode())      
print(h0.hexdigest())                   # d7e31ef085af56d4913e83b70da33353


# sha加密
h1 = hashlib.sha1('12345'.encode())
h2 = hashlib.sha224('12345'.encode())
h3 = hashlib.sha256('12345'.encode())
print(h1.hexdigest()) # 8cb2237d0679ca88db6464eac60da96345513964
print(h2.hexdigest()) # a7470858e79c282bc2f6adfd831b132672dfd1224c1e78cbf5bcd057
print(h3.hexdigest()) # 5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5




# ----------hmac秘钥模块-------
# 官方文档：https://docs.python.org/zh-cn/3.11/library/hmac.html
# https://blog.csdn.net/weixin_38819889/article/details/122457122
# hmac也是单向加密
# 格式参数: hmac.new(key, msg, digestmod)
h4 = hmac.new('12345'.encode(), 'msg_加密盐'.encode(), hashlib.md5)
h5 = hmac.new('12345'.encode(), 'msg_加密盐'.encode(), hashlib.sha1)
print(h4.hexdigest())  # a85e8302af328ed0654bfe40c45d7be7
print(h5.hexdigest())  # 2ccabed4d1f5b4a3cc5da86410abb35072535b48


# ----------uuid模块-------
# 用于生成全局唯一值
# 官方文档：https://docs.python.org/zh-cn/3.11/library/uuid.html

# uuid1 基于mac地址、时间戳、随机数生成唯一uuid，可保证全球范围唯一性
print(uuid.uuid1()) # 57f429be-e44d-11ed-9188-76a74c640473

# uuid3(namespace,name) 根据命名空间标识符（这是一个UUID）和名称（这是一个字符串）的MD5哈希值，生成一个UUID
# namespace并不是自己手动置顶的字符串或者其他量，而是在uuid模块内给出的一些值，比如：uuid.NAMESPACE_DNS uuid.NAMESPACE_OID,这些值本身也是UUID对象，根据一定规则生成
# 多次运行生成的值是固定的
print(uuid.uuid3(uuid.NAMESPACE_DNS, '牛牛')) # 0079474e-c7d6-3809-9f41-54e12ba0075b

# uuid4 通过为随机数得到uuid，有一定概率重复
# 开发过程中使用的最多
print(uuid.uuid4()) # 291aef17-222a-42db-bfda-95f2c776dd01

# uuid5 跟uuid3类似，只不过采用的散列算法是sha1
# 多次运行生成的值是固定的
print(uuid.uuid5(uuid.NAMESPACE_DNS, '牛牛')) # 67c746d8-5f40-5623-a1c1-5573eab4f225