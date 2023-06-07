
# 继承的特点：如果类B继承自类A，那么由类B创建的实例对象都可以直接调用类A的方法


# ------子类重写父类方法--------
class Person(object):
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def sleep(self) -> None:
        print("正在睡觉")
        
class Student(Person):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)
    
    def sleep(self) -> None:
        # 重写方式1：父类名.父类方法(self,参数列表)
        # Person.sleep(self)
        
        # 重写方式2：super().父类方法()
        # super().sleep()
        print('同时也在打呼噜')
        
        

ss = Student('牛牛', 20)
ss.sleep()
# 牛牛正在睡觉
# 同时也在打呼噜

# 如果子类重写了父类方法，强制调用父类的方法
# 方式1：cls.__base__.obj_method(obj, 参数)
# 方式2：super(cls, obj).obj_method(参数)




# -----多态的使用-------
class Dog(object):
    def work(self):
        print('狗狗工作')
        


class BlindDog(Dog):
    def work(self):
        print('导盲犬正在工作')
        
class PoliceDog(Dog):
    def work(self):
        print('警犬正在工作')
        
class DrugDog(Dog):
    def work(self):
        print('缉毒犬正在工作')
        
class Police(object):
    def __init__(self, name) -> None:
        self.name = name
        self.dog = None
    
    def work_with_dog(self):
        if (self.dog is not None) and (isinstance(self.dog, Dog)):
            self.dog.work()
        
police = Police('张三')

dog1 = BlindDog()
dog2 = PoliceDog()
dog3 = DrugDog()

police.dog = dog1
police.work_with_dog() # 导盲犬正在工作

police.dog = dog2
police.work_with_dog() # 警犬正在工作

police.dog = dog3
police.work_with_dog() # 缉毒犬正在工作





# --------------多继承(容易出错，尽量不使用)---------
class Camera:
    def take_photo(self):
        print('拍照片')
        
class Player:
    def play_movie(self):
        print('放电影')

class Phone(Camera, Player):
    pass

nnPhone = Phone()
nnPhone.take_photo() # 拍照片
nnPhone.play_movie() # 放电影