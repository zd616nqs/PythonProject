''' 
__all__
__name__
__file__
__init__.py
'''


# ------------模块导入的方式介绍-----------
# python为了方便开发，提供了很多内置模块，导入模块后，就可以使用这个模块内的func和var了
# 注意点：import一个模块后，这个模块文件会被执行，里面的print啥的都会打印
''' 
1.导入一整个模块
import time 

2.导入一个模块并起个别名
import datetime as nqs_dt

3.导入一个模块内的方法或者变量
from random import randint 

4.导入一个模块内的方法或者变量并起个别名
from copy import deepcopy as nqs_dp

nqs_dp([1, 2, 3])

5.导入一个模块内某个文件的变量或方法
from nqs_module.file1 import testFunc

'''


# 6.导入一个模块内的所有方法和变量(尽量少用,代码看着会很乱)
# from math import *           
''' 
本质是读取了模块的__all__属性(不会读取_下划线开头的变量和方法)
    举例：定义个模块文件：
    
    文件内容：nqs_module.py
        __all__ = ['testVarNqs111', 'testDemoFunc111']
        testVarNqs111 = 100
        testVarNqs222 = 200
        
        def testDemoFunc111():
            printf('执行方法testDemoFunc111')
        def testDemoFunc222():
            printf('testDemoFunc222')

    文件内容：test.py文件内引入模块
        from nqs_module import *
    
    
    
    分析：nqs_module.py文件内是否显式声明了__all__属性
    1.没有显式声明的情况：test.py内可以访问nqs_module内的所有变量和方法（不包含_开头的）
        testVarNqs111、testVarNqs222、testDemoFunc111、testDemoFunc222
    
    2.显式声明的情况：
        test.py只能访问testVarNqs111和testDemoFunc111
'''



# 强制禁止 变量或者方法被外部调用，使用del()
def testFunc():
    print('打印方法')
def _testInnerFunc():
    print('打印方法')
mmm = 100
_nnn = 200
    
del (testFunc, _testInnerFunc, mmm, _nnn)





# ----------7.给模块内的类方法添加别名，使外部import模块后，不用初始化类就能直接调用特定方法---
class CustomPerson(object):
    def __init__(self, name) -> None:
        self.name = name
        
    def eat(self, foodName):
        print(self.name + '正在吃' + foodName)

p = CustomPerson('牛牛')
eat = p.eat  # 起别名

# import 当前模块文件名
# 当前模块文件名.eat('西红柿鸡蛋')   #打印：牛牛正在吃西红柿鸡蛋


# ------------__init__.py介绍-----------
''' 
区分是普通文件夹还是一个包的点就是是否包含有__init__.py文件
__init__.py 控制着包的导入行为,别的地方引入这个包时，会先执行一遍__init__.py内的代码
    为空时，代表仅仅把这个包导入，不会导入包里的模块
    不为空时。。。。todo:niu 待补充
'''

# __init__.py文件编辑注意事项

# 导入模块内不同的文件
''' 
from . import file1
from . import file2
from .file3 import testFunc
from .file4 import testClass
'''

