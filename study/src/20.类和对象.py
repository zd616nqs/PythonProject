
# ----------------------类属性和实例属性---------------------
class Lizhi(object):
    type = '猫咪'
    
    def __init__(self, name, age) -> None:
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

Lizhi.type = '猴子'
print(lizhi222.type) # 猴子


# --------------------私有变量和私有属性---------------------
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

# -------私有属性调用------
# 0.常规获取方式，会报错，获取不到私有变量
# print(coco111.__height)  
# 1. 使用 对象._类名__私有变量名的方式可以获取到
print(coco111._Coco__height)      # 10.5斤   
# 2.自定义set和get方法手动获取
print(coco111.get_height_func())  # 10.5斤   
coco111.set_height_func('9斤')
print(coco111.get_height_func())  # 9斤
# 3.使用property调用 todo:niu 待补充

# -------私有方法调用------
# 0.常规方式调用，会报错
# coco111.__demo()  
# 1. 使用 对象._类名__私有方法名的方式可行
coco111._Coco__demo()  # 我是私有函数__demo







# --------------------类或实例对象调用：实例方法、静态方法、类方法 ---------------------
class Dog(object):
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        
    # 1.实例方法，类调用和实例对象 都可以调用，实例对象调用时不用传self
    def eat(self, food):
        print(self.name + '在吃' + food)
        
    # 2.一个方法没有用到任何实例对象(即self),可以使用staticmethod定义为静态方法
    @staticmethod
    def run():
        print('这是一个狗狗')
    
    # 3.一个方法只用到了类cls属性，使用clsasmethod定义，不用手动传入cls(类比不用手动传入self)
    @classmethod
    def jump(cls):
        print(cls,)


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