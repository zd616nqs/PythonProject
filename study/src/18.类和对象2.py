

# ----------------------类属性 和 实例属性---------------------
class Lizhi(object):
    type = '猫咪'
    
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

lizhi111 = Lizhi('荔枝1号', 10)
lizhi222 = Lizhi('荔枝2号', 10)

# 1.类属性的查找：实例对象没有找到实例属性时，就会查找类属性
# 类属性type可以通过 类对象 和 实例对象 获取
print(Lizhi.type)     # 猫咪
print(lizhi111.type)  # 猫咪

# 2.类属性的修改：只能通过类对象进行修改
lizhi111.type = '狗狗'  # 并不会修改类属性，而是给实例对象lizhi111添加了一个新的对象属性
print(Lizhi.type) # 猫咪

Lizhi.type = '猴子'
print(lizhi222.type) # 猴子


# --------------------私有变量---------------------
# 可见性：以两个_下划线开始的属性或者方法，对外不可见，不能被直接调用
# 备注：如果__xxx__前后都加双下划线，就又变成对外可见了
# 原理：底层被改成了：_类名__属性名
class Coco(object):
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        self.__height = '10.5斤'  # 私有变量以两个_下划线开始

    def get_height_func(self) -> str:
        print('查询了体重')
        return self.__height
    
    def set_height_func(self, __value: str) -> str:
        if type(__value) != str:
            print('设置的体重得是字符串')
            return
        print('修改了体重')
        self.__height = __value
        
    def __demo(self):
        print('我是私有函数__demo')
        

coco111 = Coco('coco1号', 2)

# -------私有变量调用------
# 0.常规获取方式，会报错，获取不到私有变量
# coco111.__demo()        # 报错
# print(coco111.__height) # 报错

# 1. 使用 实例对象._类名__私有方法名/变量名的方式可行
coco111._Coco__demo()          # 我是私有函数__demo
print(coco111._Coco__height)      # 10.5斤   

# 2.自定义set和get方法手动获取
print(coco111.get_height_func())  # 10.5斤   
coco111.set_height_func('9斤')
print(coco111.get_height_func())  # 9斤

# 3.使用@property声明 变相控制getter、setter方法-------
# @property装饰器就是负责把一个方法变成属性调用的
# 备注：指定的当做set和get的方法名必须一致
# 参考链接：https://www.tianqiweiqi.com/python-property.html
class LizhiCat(object):
    def __init__(self) -> None:
        self.__age = 0
    
    @property
    def tempage(self):
        return self.__age
    
    @tempage.setter
    def tempage(self, age):
        self.__age = age

lizhi = LizhiCat()
lizhi.tempage = 3
print(lizhi.tempage) # 3





# --------------------类或实例对象调用：实例方法、静态方法、类方法 ---------------------
class Dog(object):
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        
    # 1.实例方法，类调用和实例对象 都可以调用，实例对象调用时不用传self
    # 使用场景：方法的执行者是 实例对象
    def eat(self, food):
        print(self.name + '在吃' + food)
        
    # 2.一个方法没有用到任何实例对象(即self),可以使用staticmethod定义为静态方法
    # 使用场景：方法的执行者不要求是实例对象、没必要多此一举实例化对象的时候
    @staticmethod
    def run():
        print('这是一个狗狗')
    
    # 3.一个方法只用到了类cls属性，使用clsasmethod定义，不用手动传入cls(类比不用手动传入self)
    # 使用场景：方法的执行者不要求是实例对象、没必要多此一举实例化对象的时候
    @classmethod
    def jump(cls):
        print(cls)


# 1.调用实例方法：类调用和实例对象 都可以调用
dog111 = Dog('安娜', 10)
dog111.eat('面条子')      # 入参不用显示传入self
Dog.eat(dog111, '大骨头') # 入参需要显示传入self实例对象

# 2.调用静态方法：类调用和实例对象 都可以调用
dog111.run() # 这是一个狗狗
Dog.run()    # 这是一个狗狗

# 类方法：类调用和实例对象 都可以调用(入参不用显示传入cls)
dog111.jump() # <class '__main__.Dog'>
Dog.jump()    # <class '__main__.Dog'>






# ---------------------单例的使用-----------
# 还有其他5种实现方式：todo:niu 待补充进笔记 
# https://blog.csdn.net/weixin_51213906/article/details/125905589 
class SingletonTest(object):
    def __init__(self, name) -> None:
        self.name = name
    
    # 重写申请内存方法
    def __new__(cls, *args, **kwargs): 
        if not hasattr(SingletonTest, "nqs_instance"):
            SingletonTest.nqs_instance = object.__new__(cls)
        return SingletonTest.nqs_instance

        
single1 = SingletonTest('第一次创建') 
print(hex(id(single1)))  # 0x1042265d0
single2 = SingletonTest('第二次创建')
print(hex(id(single2)))  # 0x1042265d0
print(hex(id(single1)), hex(id(single2))) # 0x1042265d0 0x1042265d0

print(single1.name, single2.name) # 第二次创建 第二次创建
print(single1 is single2) # True









# ---------------------类的继承---------------
# 父类里定义的属性，子类可以直接调用
# 父类里定义的方法，子类的实例对象可以直接嗲用
# 调用方法时，从子类-》父类-》父类的父类-》object这个顺序去查找

# python内支持多继承
# 多个父类有同名的方法时,按照声明继承父类的先后顺序执行前面的
#       object->A(foo)->B->X  
#       object->C->D(foo)->X  
#       X(B,D) 
#       x=X() x.foo() 
#       输出：打印A类里的foo
#       X(B,D)的话 顺序：B->A->D->C
#       X(D,B)的话 顺序：D->C->B->A
class Animal(object):
    def __init__(self, name) -> None:
        self.name = name
    
    def run(self):
        print(self.name+'奔跑')
        
    def play(self):
        print('动物玩耍')
        
class Pet(object):
    def __init__(self, action) -> None:
        self.action = action
    
    def play(self):
        print('宠物玩耍')

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
        
    def eat_shit(self):
        print(self.name+'吃屎')
    
class Cat(Animal, Pet):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def sleep(self):
        print(self.name+'睡懒觉')

dog = Dog('安娜')
dog.run()
dog.eat_shit()

cat = Cat('荔枝')
cat.run()
cat.sleep()
cat.play() # 动物玩耍  


# ------继承的情况下 私有变量和私有方法的访问--------

class Animal222(object):
    def __init__(self, name) -> None:
        self.name = name
        self.__fav = '父类私有变量'
    
    def __fatherMethod(self):
        print(self.name+'奔跑')
        
        
class Dog222(Animal222):
    def __init__(self, name) -> None:
        super().__init__(name)
        
anim111 = Animal222('动物类')
dog111 = Dog222('狗狗狗狗')

# 1.子类访问父类的 私有变量（格式：实例对象._父类名__私有变量）
# print(dog111._Dog222__fav)   # 会报错
print(dog111._Animal222__fav)  # 输出：父类私有变量

# 2.子类访问父类的 私有方法（格式：实例对象._父类名__私有方法）
# dog111._Dog222__fatherMethod()   # 会报错
dog111._Animal222__fatherMethod()  # 输出：狗狗狗狗奔跑

