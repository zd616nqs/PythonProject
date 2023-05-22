

# with是上下文管理器，用于很多需要手动关闭连接的场景
# 比如：文件连接，socket连接，数据库连接
# with关键字后面跟的对象，需要有__enter__和__exit__方法的实现   比如open继承自IOBase类里有实现
# 备注：python中系统允许打开的文件数量是有上限的


try:
    with open('src/不存在的文件.txt', 'r', encoding='utf8') as tempFile:
        tempFile.read()
        # tempFile.close() # 使用了with关键字之后会自动的关闭文件
except FileNotFoundError:
    print('文件不存在')



# 自定义一个实现enter和exit的类

class People(object):
    def __enter__(self):
        print('__enter__方法被调用了')
        return '进入people'
    
    def __exit__(sel, exc_type, exc_val, exc_tb):
        print('__exit__方法被调用了')
        return '退出people'
    
def create_func():
    nqs = People()
    return nqs


# 相当于：temp = create_func().__enter__()
with create_func() as temp:
    print(temp)
    
# __enter__方法被调用了
# 进入people
# __exit__方法被调用了
