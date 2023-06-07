# -------------函数的基本介绍-----------
print('-----函数的基本介绍--------')
# 在python中，使用关键字def来声明一个函数
def testMethod(para1, para2):
    print('您输入的是{}和{}'.format(para1, para2))

# tempSplit1, tempSplit2 = input('请输入姓名和年龄，使用逗号分隔：').split(',')
tempSplit1 = '闪闪闪'
tempSplit2 = '88'
testMethod(tempSplit1, tempSplit2)
testMethod('牛青山', 30)
testMethod(para1='琳琳', para2=22)
print('\n')




# ----函数的返回值----
print('-----return返回值--------')
def addExample(a, b):
    c = a + b
    return c

tempAdd1, tempAdd2 = 111, 222
addResult = addExample(tempAdd1, tempAdd2)
print('addResult: ', addResult)  # 结果：addResult:  333
print('\n')

# ----返回多个值(元组、字典、数组、对象都行)----
print('-----多个返回值--------')
def addExample222(a, b):
    return a, b  # (以元组的形式返回)
testReturnResult = addExample222(3, 4)
print('testReturnResult: ', testReturnResult)  # 结果：testReturnResult:  (3, 4)
print('\n')

# ----声明返回值的类型-------
def addExample333(para1, para2) -> list:
    templist = []
    templist.append(para1)
    templist.append(para2)
    return templist



# ----定义行数参数和返回值的类型----
print('-----定义行数参数和返回值的类型--------')
# 下面的写法声明类型只能起到参考作用，int可以相加，但是串两个str进去，不会报错的
# ！！！注意：声明类型是没用的，只是参考作用
def typeExampleMethod(para1: int, para2: int):
    restult: int = para1 + para2
    return restult
typeResult = typeExampleMethod('abc', 'xyz')
print('typeResult: ', typeResult)  # 结果：typeResult:  abcxyz
print('\n')
# 使用inpect模块校验类型参考链接
# https://blog.csdn.net/ammmao/article/details/89527349
# https://blog.csdn.net/qq_39246147/article/details/129157112




# ----函数的缺省参数----
print('-----函数的缺省参数--------')
def testDefaultParaMethod(name, age, location='郑州'):
    print('姓名：{}，年龄：{}，籍贯：{}'.format(name, age, location))
testDefaultParaMethod('牛牛', 18)         # 结果：姓名：牛牛，年龄：18，籍贯：郑州
testDefaultParaMethod('牛牛', 18, '上海')  # 结果：姓名：牛牛，年龄：18，籍贯：上海
print('\n')

# ----函数入参的拼装----
# multipleParas = []
# # 以此输入 123 abc 673 exit
# while True:
#     inputData = input('请输入参数，直到输入exit结束:')
#     if inputData == 'exit':
#         break
#     multipleParas.append(inputData)
# print('multipleParas: ', multipleParas)  # 结果：multipleParas:  ['123', 'abc', '673']


# ---------函数的参数动态获取（*args和**kwargs）-----------------
print('-----函数的参数动态获取（*args和**kwargs）--------')
# ---- *argname：可变位置参数(传入没有定义的变量名会报错)----
# 用来发送一个 非键值对 的可变数量的参数列表给一个函数
# 保存形式：元组
def dynamicParasMethod111(a, b, *nqs_args):
    print('a={}, b={}, args={}'.format(a, b, nqs_args))
dynamicParasMethod111(1, 2, 3, 4)           # a=1, b=2, args=(3, 4)
dynamicParasMethod111(1, 2, 3, 4, 5, 6, 7)  # a=1, b=2, args=(3, 4, 5, 6, 7)
# dynamicParasMethod111(1, 2, 3, x=1, y=2)    # 会报错，传入没有定义的变量名x和y

# ---- **kwargs  可变的关键字参数----
# 多余的**kwargs变量，传入时必须显式声明变量名
# **kwargs 允许你将不定长度的键值对, 作为参数传递给一个函数。 
# 如果你想要在一个函数里处理带名字的参数, 你应该使用**kwargs。比如：a=10。
# 保存形式：字典
# **krargs 本质上就是把参数转换成字典传递给内部，所以可以直接传个字典进去

def dynamicParasMethod222(a, b, **nqs_kwargs):
    print('a={}, b={}, args={}'.format(a, b, nqs_kwargs))
# dynamicParasMethod222(1, 2, 3, 4)                # 会报错，没有显式声明3和4对应的变量名
dynamicParasMethod222(1, 2, mm=3, nn=4)            # a=1, b=2, args={'mm': 3, 'nn': 4}
dynamicParasMethod222(1, 2, **{'mm': 3, 'nn': 4})  # a=1, b=2, args={'mm': 3, 'nn': 4}

print('\n')



# --------------强制使用关键字参数-----------
# 方式：在定义参数时，在希望声明关键字的第n个参数开始写*，则*右边的所有参数在调用时必须写上参数名
def testnnn(*, para1=100, para2=333, para3=0):
    pass
# testnnn(22, 33, 55)  # 会报错
testnnn(para1=11, para2=22, para3=33)


def testnnn22(para1=100, *, para2=333, para3=0):
    pass
testnnn22(33, para2=44, para3=66)






# ------局部变量和全局变量的作用域----
print('-----局部变量和全局变量的作用域--------')
# 在python内，全局变量和局部变量可以同名！！各是各的，不会相互影响。但是还是尽量避免同名
# 如果想在函数内修改全局变量的值，使用global关键字

# ---nonlocal和global的区别:----
# 1.nonlocal: 
#   1.1 在内层可以将外层变量看做本地变量，赋予了内层函数对外层函数变量的修改权
#   1.2 必须定义在闭包内，即nonlocal的使用上层不能是主体，上层必须是在某一层的def内。
#   1.3 定义的变量不仅在嵌套的inner函数内生效，在整个大函数里面都有效
# 2.global:
#   2.1将变量声明为全局变量，使内部变量能够被外部访问，同时也实现了在函数内部改变变量值，变相的把外部变量引进函数内部了
#   2.2 整个代码环境内都有效

# 参考说明：
# https://blog.csdn.net/weixin_43439761/article/details/127869277
# https://zhuanlan.zhihu.com/p/467568306
# https://blog.csdn.net/jhsxy2005/article/details/107451737

aaa = 100
bbb = 'hello'

def tempfunc111():
    aaa = 999
    print('局部变量aaa: ', aaa)  # 结果：局部变量aaa:  999
    
    global bbb
    print('局部变量bbb修改前: ', bbb) # hello
    bbb = 'world'
    print('局部变量bbb修改后: ', bbb)  # world

print('全局变量aaa: ', aaa)  # 结果：全局变量aaa:  100
print('全局变量bbb: ', bbb)  # 结果：全局变量bbb:  world
print('\n')





# ----查看变量----
print('-----查看变量--------')
# globals：查看所有全局变量
# locals：查看所有局部变量
def tempfunc222():
    tempPara = 673
    print('locals所有局部变量：{}'.format(locals()))  # 结果：locals所有局部变量：{'tempPara': 673}
    # print('globals所有全局变量：{}'.format(globals())) # 结果：非常长。。省略了
tempfunc222()
print('\n')



# python内定义：
# 不可变类型：字符串、数字、元组
# 可变类型：列表、字典、集合
# -----入参的类型问题(可变/不可变类型参数)-------
print('-----入参的类型问题(可变/不可变类型参数)--------')

testStr = 'niuniuniu'
testTuple = (1, 2, 3)
testInt = 673
def testImmutableType(paraStr, paraTuple, paraInt):
    paraStr = 'shanshanshan'
    paraTuple = (888, 999)
    paraInt = 123
    print('paraStr={}, paraTuple={}, testInt={}'.format(paraStr, paraTuple, paraInt))
testImmutableType(testStr, testTuple, testInt)  
# 都没变 paraStr=niuniuniu, paraTuple=(1, 2, 3), testInt=673


testList = [1, 2, 3]
testDict = {'x': 1, 'y': 2, 'z': 3}
testSet = {7, 8, 9}
def testMutableType(paraList, paraDict, paraSet):
    paraList = [111, 222, 333]
    paraDict = {'mm': 666, 'nn': 777}
    paraSet = {777, 888, 999}
    print('paraList={}, paraDict={}, paraSet={}'.format(paraList, paraDict, paraSet))
testMutableType(testList, testDict, testSet)
# 都改变了 paraList=[111, 222, 333], paraDict={'mm': 666, 'nn': 777}, paraSet={888, 777, 999}
print('\n')



