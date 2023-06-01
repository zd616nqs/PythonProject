import random


# ----------------------if判断--------------------
# 常见的语句： if /  if else /  if elif elif elif else
''' 
    if语句 注意点：
    1.python中不支持switch case语句
    2.区间判断的区别：oc、java等语言区间不能连写，但是python中 逻辑运算可以连续连接起来使用：30<xx<60
    3.隐式类型转换：if判断里，int值会隐式转换成bool值
    4.三元表达式的区别：xx = num1 if (num1 > num2) else num2
'''


# ------if else---------
num = int(float(input("请输入一个数字:")))
if (num % 4 == 0 and num % 3 == 0):
    print("可以被3和4整除")
else:
    print("不能被整除") 


# ------if elif else---------
score = int(float(input("请输入分数：")))
if score < 60:
    print("成绩不及格")
elif (60 <= score <= 80):
    print("成绩一般")
else:
    print("成绩优秀")
    

# --------pass关键词进行占位---------
# 使用pass关键字占位，没有意义，只是单纯的用来占位
# 场景：比如if后面还没想好怎么写，但是python校验缩进，所以必须有东西，就是用pass占位
height = 666
if height > 100:
    pass  # 占位使用
print("你好1111")
# 使用pass，打印：你好111
# 不使用pass，缩进校验失败，会报错


# 随机数
player = random.randint(0, 3)  # 随机数[0,3]
print("随机数:" + str(player))





# ----------------------循环语句--------------------
''' 
    循环语句 注意点：
    1.python中不支持自增自减++/--操作: age++会报错
    2.
'''

# -----while循环-----
i = 0
result = 0
while i < 10:
    i += 1
    if (i % 2 == 0):
        result += 1
print("结果：" + str(result))  # 结果：5


# -----forin循环-----
# for循环内的可迭代对象支持的类型为：字符串、列表、字典、元组、集合、range
listArr = ["niu", "qing", "shan"]
for temp1 in listArr:
    print(temp1)  # 结果:niu、qing、shan
for temp2 in range(3, 6):  # 相当于区间[3,6)
    print(temp2)  # 结果:3、4、5
for temp3 in "niu":
    print(temp3)  # 结果:n、i、u
    
# ------for循环------
for tempIdx, tempStr in enumerate(listArr):
    print('当前下标：%d，当前数据：%s' % (tempIdx, tempStr))
# 当前下标：0，当前数据：niu
# 当前下标：1，当前数据：qing
# 当前下标：2，当前数据：shan

    
# -----break和continue-----
# continue结束本轮循环(continue所在行后面的的行不会被执行)
# break结束整个循环

userName = input("请输入用户名：(张三)")
passWord = input("请输入密码：（123）")
# while not(userName == "张三" and passWord == "123"):
#     print("账号密码错误，请重试：")
#     userName = input("请输入用户名：")
#     passWord = input("请输入密码：")
# print("恭喜您，登录成功")

while True:
    if (userName == "张三" and passWord == "123"):
        print("恭喜您，登录成功")
        break
    print("账号密码错误，请重试：")
    userName = input("请输入用户名：")
    passWord = input("请输入密码：")


# -----for in...else...-----
# 当for循环内的break没有执行时，会执行else
for temp in range(1, 101):
    if temp == 200:
        print("符合条件")
        break
else:
    print("没有符合条件的数")


# 练习：打印水仙花数
for temp in range(100, 1000):
    gewei = temp % 10
    shiwei = temp // 10 % 10
    baiwei = temp // 100 % 10
    if ((gewei ** 3) + (shiwei ** 3) + (baiwei ** 3) == temp):
        print("水仙花数：", temp)
'''  
水仙花数： 153
水仙花数： 370
水仙花数： 371
水仙花数： 407
'''

# 练习 取100~200内的质数（除了1和自身以外没有可以整除的数）
print("获取100-200内的质数：")
for temp in range(100, 201):
    for temp22 in range(2, temp):
        if (temp % temp22 == 0):
            # print("被整除了，不是质数")
            break
    else:
        print(temp, end=" ")
print()
# 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197 199 
        

# 练习 求斐波那契数的第十二个数
currentNum = 0
lastNum = 0
count = 0
targetNum = 0
print("打印斐波那契数列：")
for temp in range(0, 20):
    count += 1
    findTarget = (count == 12)
    if currentNum == 0:
        currentNum += 1
        lastNum = currentNum
    else:
        temp = currentNum
        currentNum = lastNum + currentNum
        lastNum = temp
    print(currentNum, end=" ")
    
    if findTarget:
        targetNum = currentNum
print()
# 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 
if (targetNum > 0): 
    print("第12个斐波那契数字是：", targetNum)
    # 第12个斐波那契数字是： 233