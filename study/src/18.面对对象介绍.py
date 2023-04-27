
# 使用class定义类 命名使用大驼峰规则
# 1.class <类名>
# 1.class <类名>(object)


class Student(object):
    def __init__(self, name, age, height) -> None:
        self.name = name
        self.age = age
        self.height = height
        
    def run(self):
        print(self.name+'正在跑步')
        
    def eat(self):
        print(self.name+'正在吃饭')
        
        
stu1 = Student('牛牛', 18, 175)
stu2 = Student('琳琳', 16, 160)
print('stu1:name={}, age={}, height={} '.format(stu1.name, stu1.age, stu1.height))
# stu1:name=牛牛, age=18, height=175

stu1.run() # 牛牛正在跑步
stu2.eat() # 琳琳正在吃饭

''' 
这段代码发生了什么？stu1 = Student('牛牛', 18, 175)
    1.调用__new__方法，申请一段内存空间
    2.调用__init__方法，让self指向刚才申请的内存空间
    3.各个属性赋上传入的值：name、age、height
    4.stu1也指向这块内存空间
'''




# ----python是动态语言，对一个不存在的属性赋值，会给这个类动态添加一个属性----

# print(stu1.city)  # 报错，没有定义
stu1.city = '上海'
print(stu1.city)  # 上海

# -------防止动态添加属性，类里的属性可控：使用__slots__
# __slots__是个元组，用来规定类里可以存在的属性
class Person(object):
    __slots__ = ('name', 'age')
    # __slots__ = () # 空的时候标识类里不能定义任何属性
    
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
person1 = Person('牛牛', 18)
# person1.city = '上海' # 会触发报错：AttributeError: 'Person' object has no attribute 'city'














# -----------类里的一些特殊方法--------
# 特点1：都是__xxx__格式
# 特点2：方法名都是系统规定好的，无需手动调用，合适时机自动调用

'''
**********生命周期相关***************
    __init__方法：创建对象时自动调用
    __del__方法： 对象被销毁时调用
    __str__方法： print(一个类的实例对象)，会触发类的__str__方法或__repr__方法,如果两个方法都实现了，会执行__str__
    __call__方法：使实例对象能够进行调用，例如：实例对象名()
**********运算符相关***************
    __eq__方法：两个实例对象p1==p2进行比较时进行调用,返回结果  类似于result = p1.__eq__(p2)
'''

class TestDemo(object):
    def __init__(self) -> None:
        print('__init__, 类被创建了')
    
    def __str__(self) -> str:
        return '__str__, 实例对象被打印了'
        
    def __repr__(self) -> str:
        return '__repr__, 实例对象被打印了'
    
    def __del__(self) -> None:
        print('__del__, 类被销毁了')
        
    def __call__(self, *args, **kwds):
        print('__call__,实例对象可以执行调用了')
        x = args[0]
        y = args[1]
        fn = kwds['fn']
        return fn(x, y)
    
testDemo1 = TestDemo()
print(testDemo1)
result = testDemo1(111, 333, fn=lambda x, y: x + y)
print(result)

''' 
执行结果输出：
__init__, 类被创建了
__str__, 实例对象被打印了
__call__,实例对象可以执行调用了
444
__del__, 类被销毁了
'''




class TestDemo222(object):
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        
    def __eq__(self, __value: object) -> bool:
        print('__eq__, 实例对象的值进行对比')
        return (self.name == __value.name) and (self.age == __value.age)
    
nqs1 = TestDemo222('牛牛', 18)
nqs2 = TestDemo222('琳琳', 18)
print(nqs1 == nqs2)
''' 
执行结果输出：
__eq__, 实例对象的值进行对比
False
'''