
# 函数的高阶使用

# 1.一个函数作为两位一个函数的参数   典型例如lambda
# 2.一个函数作为两位一个函数的返回值  return 调用函数
def demoFunc1():
    print("descFunc1")
def demoFunc2():
    print("descFunc2")
    return demoFunc1
def demoFunc3():
    print("descFunc3")
    return demoFunc1()
print(demoFunc1())    # descFunc1 None
print(demoFunc2())    # descFunc2 <function descFunc1 at 0x102f884a0>
print(demoFunc2()())  # descFunc2 descFunc1 None
print(demoFunc3())    # descFunc3 descFunc1 None
# print(demoFunc3()())
# 3.函数内部再定义一个函数
def outerMethod():
    m = 100
    p = 666
    
    def innerMethod():
        n = 99
        nonlocal m 
        m = 188
        print('inner函数', m, n, p)  # inner函数 188 99 666
    print("outer函数")
    return innerMethod
    
outerMethod()()

# nonlocal和global的区别
# https://blog.csdn.net/weixin_43439761/article/details/127869277

# -------------递归调用------------
print("-----递归调用--------")
