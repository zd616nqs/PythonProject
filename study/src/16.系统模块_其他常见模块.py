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




# ----------hashlib哈希模块-------
# 官方文档：https://docs.python.org/zh-cn/3.11/library/hashlib.html

# md5加密
test_md5 = hashlib.md5()                # 生成一个md5对象
test_md5.update("牛青山".encode('utf8')) # 加密一段字符串
print(test_md5.hexdigest())             # d7e31ef085af56d4913e83b70da33353

h0 = hashlib.md5('牛青山'.encode())      
print(h0.hexdigest())                   # d7e31ef085af56d4913e83b70da33353

# sha加密
h1 = hashlib.sha1('12345'.encode())
print(h1.hexdigest()) # 8cb2237d0679ca88db6464eac60da96345513964
h2 = hashlib.sha224('12345'.encode())
print(h2.hexdigest()) # a7470858e79c282bc2f6adfd831b132672dfd1224c1e78cbf5bcd057
h3 = hashlib.sha256('12345'.encode())
print(h3.hexdigest()) # 5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5




# ----------hmac秘钥模块-------
# 官方文档：https://docs.python.org/zh-cn/3.11/library/hmac.html
# hmac也是单向加密
h4 = hmac.new('12345'.encode(), 'msg_加密盐'.encode(), hashlib.md5)
print(h4.hexdigest())  # a85e8302af328ed0654bfe40c45d7be7
h5 = hmac.new('12345'.encode(), 'msg_加密盐'.encode(), hashlib.sha1)
print(h5.hexdigest())  # 2ccabed4d1f5b4a3cc5da86410abb35072535b48
print()

# ----------uuid模块-------
# 用于生成全局唯一值
# 官方文档：https://docs.python.org/zh-cn/3.11/library/uuid.html

# uuid1 基于mac地址、时间戳、随机数生成唯一uuid，可保证全球范围唯一性
print(uuid.uuid1()) # 57f429be-e44d-11ed-9188-76a74c640473

# uuid3(namespace,name) 根据命名空间标识符（这是一个UUID）和名称（这是一个字符串）的MD5哈希值，生成一个UUID
# namespace并不是自己手动置顶的字符串或者其他量，而是在uuid模块内给出的一些纸，比如：uuid.NAMESPACE_DNS uuid.NAMESPACE_OID,这些值本身也是UUID对象，根据一定规则生成
# 多次运行生成的值是固定的
print(uuid.uuid3(uuid.NAMESPACE_DNS, '牛牛')) # 0079474e-c7d6-3809-9f41-54e12ba0075b

# uuid4 通过为随机数得到uuid，有一定概率重复
# 开发过程中使用的最多
print(uuid.uuid4()) # 291aef17-222a-42db-bfda-95f2c776dd01

# uuid5 跟uuid3类似，只不过采用的散列算法是sha1
# 多次运行生成的值是固定的
print(uuid.uuid5(uuid.NAMESPACE_DNS, '牛牛')) # 67c746d8-5f40-5623-a1c1-5573eab4f225