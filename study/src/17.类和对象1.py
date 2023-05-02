
# 使用class定义类 命名使用大驼峰规则
# 1.class <类名>
# 1.class <类名>(object)


class Student(object):
    
    # # 默认方法，申请内存，创建一个对象，并把对象类型设置为cls
    # def __new__(cls): 
    #     nqs_instance = object.__new__(cls)
    #     return nqs_instance
    
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





# 设置缺省参数,初始化时就可以不用传了
class Friend(object):
    def __init__(self, name, age, friends=None) -> None:
        # 处理缺省参数
        if friends is None:
            friends = []
            
        self.name = name
        self.age = age
        self.friends = friends

f1 = Friend('牛牛', 18)
print(f1)



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





# -----------类里的内置属性--------
'''
**********生命周期相关***************
    dir()：查看所有属性
    p.__dir__       查看所有属性
    p.__class__     查看对象的类
    p.__dict__      以字典形式，显示对象的所有属性和方法
    p.__doc__       打印注释
    Person.__doc__  打印注释
    p.__module__    打印模块名(__name__性质的)
    p.__slots__     打印允许出现的属性
'''

class Animal(object):
    '''这是个动物类'''
    
    def __init__(self, name) -> None:
        self.name = name
    
    def eat(self):
        print('进食')
    
animal111 = Animal('老虎')
print(dir(animal111))       # 查看所有属性  ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'eat', 'name']
print(animal111.__dir__())  # 同上

print(animal111.__class__)  # <class '__main__.Animal'>
print(animal111.__dict__)   # {'name': '老虎'}   以字典形式，显示对象的所有属性和方法

print(animal111.__doc__)    # 这是个动物类  打印注释
print(Animal.__doc__)       # 这是个动物类  打印注释

print(animal111.__module__) # __main__  模块名
# print(animal111.__slots__)

print()






# -----------类里的内置特殊方法--------
# 特点1：都是__xxx__格式
# 特点2：方法名都是系统规定好的，无需手动调用，合适时机自动调用

'''
**********生命周期相关***************
    __init__方法：创建对象时自动调用
    __del__方法： 对象被销毁时调用
    __call__方法：使实例对象能够进行调用，例如：实例对象名()
    __str__方法：print(一个类的实例对象)，会触发类的__str__方法或__repr__方法,如果两个方法都实现了，会执行__str__
                类型转换为字符串时也会调,比如print(str(num111))
    __float__方法：类型转换为float时.....
    __int__方法：类型转换为int时....
    __getitem__   将对象当字典一样操作,获取属性的值
    __setitem__   将对象当字典一样操作,设置属性的值
    __delitem__   将对象当字典一样操作,删除属性的值
    
**********运算符相关***************
    __eq__方法：两个实例对象p1==p2 进行比较时进行调用,返回结果  类似于result = p1.__eq__(p2)
    __ne__方法：两个实例对象p1!=p2 进行比较时进行调用,返回结果  如果没有找到ne方法，会触发__eq__方法
    __gt__方法：两个实例对象p1>p2  进行对比时进行盗用,返回结果 greater than的缩写
    __lt__方法：两个实例对象p1<p2  进行对比时进行盗用,返回结果 less than的缩写
    __sub__方法：两个实例对象p1-p2 进行对比时进行盗用,返回结果 
    __add__方法：两个实例对象p1+p2 进行对比时进行盗用,返回结果
    __mul__方法：两个实例对象p1*p2 进行对比时进行盗用,返回结果 
    __truediv__方法：除法p1/p2
    __mod__方法：取模
    __pow__方法：取余
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
        
    def __getitem__(self, key) -> None:
        print('get方法被调用了，key={}'.format(key))
        
    def __setitem__(self, key, value) -> None:
        self.__dict__[key] = value
        print('set方法被调用了，key={} value={}'.format(key, value))
        
    def __delitem__(self, key) -> None:
        del self.__dict__[key]
        print('del方法被调用了，key={}'.format(key))
        

sanmu1 = TestDemo222('荔枝', 8)


print(sanmu1.__dict__)     # {'name': '荔枝', 'age': 8}
sanmu1['name'] = '荔枝2号'  # set方法被调用了，key=name value=荔枝2号
sanmu1['age'] = 10         # set方法被调用了，key=age value=10
print(sanmu1.__dict__)     # {'name': '荔枝2号', 'age': 10}

print(sanmu1['name'])      # get方法被调用了，key=name

del sanmu1['age']          # del方法被调用了，key=age
print(sanmu1.__dict__)     # {'name': '荔枝2号'}
print()



class TestDemo333(object):
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def __eq__(self, __value: object) -> bool:
        print('__eq__, 实例对象的值进行对比')
        return (self.name == __value.name) and (self.age == __value.age)
    
    def __ne__(self, __value: object) -> bool:
        print('__ne__, 实例对象的值进行!=对比')
        return not ((self.name == __value.name) and (self.age == __value.age))
        
    def __gt__(self, __value: object) -> bool:
        print('__gt__, 实例对象的值进行>对比')
        return self.age > __value.age
        
    def __sub__(self, __value: object) -> bool:
        print('__sub__, 实例对象的值相减')
        return self.age - __value.age
        
    def __add__(self, __value: object) -> bool:
        print('__add__, 实例对象的值相加')
        return self.age + __value.age
    
    def __mul__(self, __value: object) -> bool:
        print('__mul__, 实例对象的值相乘')
        return self.age * __value.age
    
    def __truediv__(self, __value: object) -> bool:
        print('__mul__, 实例对象的值相除')
        return self.age / __value.age
        
nqs1 = TestDemo333('牛牛', 18)
nqs2 = TestDemo333('琳琳', 18)
print(nqs1 == nqs2)
print(nqs1 != nqs2)
print(nqs1 > nqs2)
print(nqs1 - nqs2)
print(nqs1 + nqs2)
print(nqs1 * nqs2)
print(nqs1 / nqs2)

''' 
执行结果输出：

__eq__, 实例对象的值进行对比
False

__ne__, 实例对象的值进行!=对比
True

__gt__, 实例对象的值进行>对比
False

__sub__, 实例对象的值相减
0

__add__, 实例对象的值相加
36
__mul__, 实例对象的值相乘
324

__mul__, 实例对象的值相除
1.0

'''










# 练习：往房子里面添加家具，并且实时计算剩余面积
class Furniture(object):
    '''家具类'''
    def __init__(self, name, area) -> None:
        self.name = name
        self.area = area
        print('')
        
class House(object):
    '''房子容器'''
    def __init__(self, house_type, total_area) -> None:
        self.house_type = house_type
        self.total_area = total_area
        self._free_area = total_area
        self._furniture_list = []
    
    def addFurniture(self, item: Furniture):
        if item.area > self._free_area:
            print('房间剩余空间不足，不能继续放置')
        else:
            print('空间够，继续放')
            self._free_area -= item.area
            self._furniture_list.append(item.name)
            
    def __str__(self) -> str:
        return ('房型:{},总面积:{},剩余面积:{},家具列表:{}'.format(self.house_type, self.total_area, self._free_area, self._furniture_list))



house1 = House('一室一厅', 50)

furn1 = Furniture('大床', 10)
furn2 = Furniture('书桌', 10)
furn3 = Furniture('化妆桌', 10)
furn4 = Furniture('衣柜', 20)
furn5 = Furniture('茶几', 10)
house1.addFurniture(furn1)  # 空间够，继续放
house1.addFurniture(furn2)  # 空间够，继续放
house1.addFurniture(furn3)  # 空间够，继续放
house1.addFurniture(furn4)  # 空间够，继续放
house1.addFurniture(furn5)  # 房间剩余空间不足，不能继续放置
print(house1)
# 房型:一室一厅,总面积:50,剩余面积:0,家具列表:['大床', '书桌', '化妆桌', '衣柜']
