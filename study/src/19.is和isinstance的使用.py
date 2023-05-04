
class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)



# 使用is相当于比较两个实例对象的内存地址是否相同 id(p1) == id(p2)
p1 = Person('1号人', 30)
p2 = Person('2号人', 31)
print(p1 is p2)  # False



ss = Student('牛牛', 22)
# 使用type()无法对父类进行判断
print(type(ss) == Student)  # True
print(type(ss) == Person)   # False


# 使用isinstance，用来判断一个对象是否有指定的类(或子类)实例化出来的
print(isinstance(ss, Student)) # True
print(isinstance(ss, Person))  # True


# isinstance也可以放一个元组进去匹配类，只要有一个匹配上就true
class XXX:
    def __init__(self) -> None:
        pass
    
print(isinstance(ss, (Person, XXX)))  # True



# issubclass 判断是否是子类
print(issubclass(Student, Person)) # True
print(issubclass(Person, Student)) # False
print(issubclass(XXX, Person))     # False