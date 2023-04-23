from functools import reduce

# -------------递归调用------------
print("-----递归调用--------")
count = 0


def tell_story():
    global count
    count += 1
    print("从前有个山，山里有个庙，庙里有个老和尚", count)
    if count < 5:
        tell_story()


tell_story()
# 从前有个山，山里有个庙，庙里有个老和尚 1
# 从前有个山，山里有个庙，庙里有个老和尚 2
# 从前有个山，山里有个庙，庙里有个老和尚 3
# 从前有个山，山里有个庙，庙里有个老和尚 4
# 从前有个山，山里有个庙，庙里有个老和尚 5

# 练习：斐波那契数列
targetMaxIndex = 10
currentNum = 0
print("斐波那契数列：", end="")


def fibonacci_func(index, lastNum):
    global targetMaxIndex
    global currentNum
    
    if index == 0:
        currentNum = 1
        print(currentNum, end=" ")
        fibonacci_func(1, currentNum)
    elif index == targetMaxIndex:
        currentNum = currentNum + lastNum
        print(currentNum, end=" ")
        print("结束")
    else:
        temp = currentNum
        currentNum = lastNum + currentNum
        lastNum = temp

        print(currentNum, end=" ")
        fibonacci_func(index + 1, lastNum)


fibonacci_func(0, currentNum)

print("\n")


# -------------匿名函数lambda------------
print("-----匿名函数lambda--------")
# 使用lambda关键词能创建小型匿名函数，省略了def声明函数的标准步骤
# 标准格式： funcName = lambda 参数列表: 运算表达式
# sum = lambda arg1, arg2: arg1 + arg2
# print('计算和：{}'.format(sum(arg1=1, arg2=2)))  # 结果：3

# 注意：lambda函数不推荐赋值给一个变量，这样跟def的作用一样了，而且还容易混淆
# 推荐的lambda使用场景，比如作为函数的实参时使用，例如下列：
# exampleFunc(playerNames, key=lambda player: player.lastYearRank+player.thisYearRank)

print("\n")







# -------------基础常见的一些内置函数------------
# -------------转换相关-------------
# bin：将数字转换成二进制
# oct：将数字转换成八进制
# hex：将数字转换成十六进制
# id：获取一个数据的内存地址
# chr：将字符编码转换成对应在字符 char(97)==>a
# ord：将字符转换成对应的编码    ord(a)==>97

# -------------输入输出-------------
# input：输入
# print：打印
# repr：把一个对象装换成字符串形式
# eval：执行字符串内的代码

# -------------数学计算-------------
# max：最大值
# min：最小值
# round：四舍五入，保留到指定小数位
# sum：求和
# divmod：传入除数和被除数，返回商和余数
print(list(divmod(22, 7)))  # [3, 1]
# abs：绝对值
print('abs: ', abs(-10))  # abs:  10
# pow：求幂运算
print('pow', pow(8, 2))  # 8的二次方 64


# -------------判断对象相关-------------
# isinstance：判断一个对象是否由一个类创建出来的
# issubclass：判断一个类是否是另一个类的子类

# -------------可迭代对象相关--------------
# all：可迭代对象内的所有元素转成布尔值后是否全是True
print('all', all([1, 2, 3, 4]))  # all True
print('all', all([0, 2, 3, 4]))  # all False
# any：可迭代对象内的所有元素转成布尔值后任意有1个是True
print('any', any([0, '']))  # any False
print('any', any([0, 'False']))  # any True
print('any', any([0, 'hello']))  # any True
# len：获取可迭代对象的长度
# iter：获取到可迭代对象的迭代器
# next、for..in：调用迭代器的next方法
# sorted：排序

# -------------其他一些函数-------------
# exit：结束整个程序，并且给定一个退出码
# format：格式化相关
# globals：查看所有全局变量
# locals：查看所有局部变量
# help：打印相关文档 help(int) help(funcName) help(className)
# dir：列出调用者所有可使用的属性和方法(数组的所有属性和方法、字典的所有属性和方法 etc..)
print(dir('hello')) 
# open：打开一个文件














# -------------sort方法的使用(内置函数)------------
print("-----sort方法的使用--------")
# 定义：def sort(*,key:,reverse:) -> None
# 功能：按照key内的函数进行排序
# 按年龄排序
students = [
    {"name": "张三", "age": 20},
    {"name": "李四", "age": 16},
    {"name": "王五", "age": 26},
]


def testFunc(tempValue):
    return tempValue["age"]


students.sort(key=testFunc)
print("students: ", students)
# students:  [{'name': '李四', 'age': 16}, {'name': '张三', 'age': 20}, {'name': '王五', 'age': 26}]

print("\n")


# -------------filter使用(内置类)------------
print("-----filter使用--------")
# 定义：filter(function or None, iterable) --> filter object
# 功能：过滤符合条件的数据并返回
ages = [16, 15, 13, 19, 20]
adultData = filter((lambda temp: temp > 18), ages)
print(type(adultData))  # <class 'filter'>
print("filterResult: ", list(adultData))  # filterResult:[19, 20]

print("\n")


# -------------map的使用(内置类)------------
print("-----map的使用--------")
# 定义：map(func, *iterables) --> map object
# 功能：每个元素都执行一次
ages222 = [17, 18, 19, 20]
mapData = map((lambda temp: temp + 3), ages222)
print(type(mapData))  # <class 'map'>
print("mapResult: ", list(mapData))  # mapResult:  [20, 21, 22, 23]

print("\n")


# -------------reduce的使用(内置函数)------------
print("-----reduce的使用--------")
# 定义：reduce(function, iterable[, initial]) -> value
# 功能: 将传入的可迭代对象内的元素，从左到右层层累计进行函数计算
# 注意：initial参数如果传值时，不能写initial=xxx，否则会报错
scroes = [2, 3, 4, 5]
def reduceFunc11(para1, para2):
    return para1 + para2
reduceData11 = reduce(reduceFunc11, scroes)  # 2+3;5+4;9+5 = 14

print(type(reduceData11))  # <class 'int'>
print("reduceResult11: ", reduceData11)  # reduceResult:  14

# ！！会报错，reduce内使用的func参数只能是2个的，其他数量的没有意义
# def reduceFunc22(para1, para2, para3):
#     return para1 + para2 - para3
# reduceData22 = reduce(reduceFunc22, scroes)  # 会报错

# 练习：计算所有人的总年龄
students222 = [
    {"name": "张三", "age": 20},
    {"name": "李四", "age": 16},
    {"name": "王五", "age": 26},
]
def reduceFunc333(para1, para2):
    return para1 + para2['age'] 
totalAge111 = reduce(reduceFunc333, students222, 0)
# totalAge111 = reduce(reduceFunc333, students222, initial=0)  # 不能这么写，会报错
print(type(totalAge111))  # <class 'int'>
print('totalAge111: ', totalAge111)  # totalAge111:  62

# 使用lambda方式写出来
totalAge222 = reduce((lambda para1, para2: para1 + para2['age']), students222, 0)
print('totalAge222: ', totalAge222)   # totalAge222:  62




