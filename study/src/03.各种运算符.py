# ------算数运算符---------
# 加减乘除+ - * / %   
# 除法：python3中，两个int值相除，结果是float类型的 4/2=2.0   在python2中结果是整数忽略小数点后数值
print(10/3)  # 结果：3.33333
print(10/2)  # 结果：5.0

# 幂运算**
print(3 ** 3)  # 结果27
print(81 ** (1/2)) # 结果：9.0  81的开平方根
print((3 ** 3) ** (1/2)) # 结果：5.196  3的3次方，然后开平方根

# 取整除 //（向下取整）
print(9 // 2)   # 结果：int类型 4
print(9.3 // 2) # 结果：float类型 4.0
print(-5 // 2)  # 结果：int类型 -3 注意：向下取整

# 取余 %
print(10 % 3) # 结果：1
print(10.2 % 3) # 结果：1.1999999

# -----------字符串支持的有限的运算符--------
# 使用加法+（拼接字符串） 注意 数字不能和字符串使用加号拼接
print("hello" + "world") # 结果：helloworld

# 使用乘法*（字符串*数字 将字符串重复多次）
print("hello" * 2) # 结果：hellohello



# -------------赋值运算符-------------

# ----传递值----
a = b = c = d = "hello" 

# ----拆包----
# 注意：拆包需要数量对应  m,n = 1,2,3,4,5会报错   m,n,e,f = 1,2也会报错
m,n = 3,5 
# 使用*表示可变长度
mm,*nn,ff = 1,2,3,4,5,6
print(mm,nn,ff) # 结果：1 [2, 3, 4, 5] 6
xx,yy,*zz = 1,2,3,4,5,6
print(xx,yy,zz) # 结果：1 2 [3, 4, 5, 6]


# ----元组----
aa = ("hello","good","yes")
bb = "hello","good","yes"
print(aa) # 结果：('hello', 'good', 'yes')
print(bb) # 结果：('hello', 'good', 'yes')

# ----复合赋值----
x = 1
x += 2
x -= 3
x *= 4
x /= 5
x **= 6
x //=7 



# -----------------比较运算符-----------------
# 大于>  小于<  大于等于>=  小于等于<=  等于==  不等于!=
print(2 > 1)  # True
print(3 < 4)  # True
print(3 >= 2) # True
print(3 <= 4) # True
print(3 == 3) # True
print(3 != 4) # True

# ----比较运算符在字符串中的使用----
# 注意：字符串使用比较运算符，会根据俄哥哥字符的编码值逐一进行比较
print("a" > "b")    # 结果：False
print("b" > "a")    # 结果：True
print("abc" > "c")  # 结果：False
print("abc" > "a")  # 结果：True

# 注意：int和str进行==计算时，不会比较编码值，统一结果False
print("a" == 97) # 结果：False  
print("a" == 90) # 结果：False

# 注意：int和str进行!=计算时，不会比较编码值，统一结果True
print("a" != 97)  # 结果：True

# 注意：int和str类型不能进行大小比较
# print("a" > 90) # 报错



# --------------逻辑运算符----------
# 逻辑与and  
print(2 > 1 and 3 > 1 and 4 > 1) # 结果：True
print(2 > 1 and 3 > 1 and 0 > 1) # 结果：False

# 逻辑或or 
print(2 > 3 or 3 > 4 or 4 > 1) # 结果：True
print(2 > 3 or 3 > 4 or 4 > 5) # 结果：False

# 逻辑非not
print(not(2 > 1)) # 结果：False

''' 短路
    1.逻辑与运算，只要有一个运算数是False，后面的就不会执行了
    2.逻辑或运算，只要有一个运算符是True，后面的就不会执行了
'''
4 > 3 and print("你好111") # 结果：你好111
4 < 3 and print("你好222") # 结果：空，没打印
4 > 3 or print("你好333")  # 结果：空，没打印
4 < 3 or print("你好444")  # 结果：你好444

# 逻辑运算的结果，不一定是布尔值
print(3 and 5 and 0 and "hellow") # 结果：0
print(3 and 5 and 6 and "hellow") # 结果：hellow
print("niu" and "qing" and "shan" and 100) # 结果：100
print(0 or [] or () or "niu" or 5 or "ok") # 结果：niu


# --------------位运算符----------
# 按位与& 按位或| 按位异或^ 按位左移<< 按位右移>> 按位取反~
''' 
    按位与&    ： 同为1则为1，否则为0
    按位或|    ： 只要有一个为1，就位1
    按位异或^  ： 相同为0，不同为1
    按位左移<< ：二级制右边加n个0  a<<n ==> a*(2的n次方)
    按位右移>> ：二进制左边加n个0  a>>n ==> a/(2的n次方)
    按位取反~  ：二进制每一位都取反
'''



# ------------运算符的优先级------------
'''
    优先级从上至下依次递减：
    **            指数优先级最高
    ~ + -         按位翻转、正负号
    * / % //      乘、除、取模、取余
    + -           加法、减法
    << >>         位移
    &             按位与
    ^ |           按位或、按位异或
    < > <= >=     比较运算符
    == !=         等于运算符
    = %= /= //= += -= *= **=  赋值运算符
    is   is not   身份运算符
    in   not in   成员运算符
    not>and>or    逻辑运算符
'''

# 注意 not>and>or，不能从左往右习惯性的计算，所以开发中强烈建议多加括号 
print(True or True and False) # 结果True 先算右边True and False，再算左边
print(False or not False) # 结果：True  先算右边 not False，再算左边
