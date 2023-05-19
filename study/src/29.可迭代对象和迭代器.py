
# 系统内置的可迭代对象有很多：list/tuple/dict/set/str/range/filter/map
from collections.abc import Iterable


class Demo11(object):
    def __init__(self, xx) -> None:
        self.xx = xx

# isinstance用来判断一个实例对象是否是指定的类创建出来的
friends = ['zhangsan', 'lisi']
print(isinstance(friends, Iterable))  # True

d1 = Demo11(10)
print(isinstance(d1, Iterable))  # False






# for..in循环的实质就是调用__iter__方法，获取这个方法的返回值,这个返回值必须是一个迭代器类型的对象，再次调用__iter__方法，循环下去
# 相当于：nqstest.__iter__().__next__()
class SingleIterClass(object):
    def __init__(self, maxCount) -> None:
        self.maxCount = maxCount
        self.countNum = 0
        
    def __next__(self):
        self.countNum += 1
        if self.countNum > self.maxCount:
            raise StopIteration # 让迭代器停止
        else:
            return 100 + self.countNum

class CustomIterClass(object):
    def __init__(self, nqs_range) -> None:
        self.nqs_range = nqs_range
        
    # 重写__iter__方法，就是可迭代对象了
    def __iter__(self): 
        tempIter = SingleIterClass(self.nqs_range)
        return tempIter



nqstest = CustomIterClass(5)
print(isinstance(nqstest, Iterable))  # True

for tempValue in nqstest:
    print(tempValue)  # 连续打印101 102 103 104 105 然后结束



# 既然有列表了，为什么还要有生成器？
# 答案:数据量特别大时适合用生成器，时间换空间，不占用内存，需要的时候再去生成。