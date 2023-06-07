

def div(a, b):
    return a / b

# 执行逻辑：
# try->有异常？->无->else->finally
#             ->有->except->finally

# ------------常规系统异常处理方式--------------------
# 使用try...except语句处理异常，出现异常立马跳转到except内
# Exception是所有异常类型的父类，可以统一进行捕获
try:
    result = div(5, 0)
    print('此行看看打不打印')  # 没有执行这行
except Exception as e:
    print('程序出错了,原因：', e)  # 程序出错了,原因： division by zero
else:
    print('计算结果是：', result)
finally:
    print('结束111')

''' 
情况：div(5, 0)
    程序出错了,原因： division by zero
    结束111
情况：div(5, 2)
    此行看看打不打印
    计算结果是： 2.5
    结束111
'''






# ---------------指定异常类型 处理--------------------
try:
    result22 = div(6, 0)   # 能正确捕获崩溃
    open('不存在的文件.txt') # 能正常捕获崩溃
    
    map = {'name': 'zhangsan'}
    print(map['age'])      # 会崩溃，没有指定此种崩溃类型的捕获
    
except (ZeroDivisionError, FileNotFoundError) as e:
    print('出错了:', e)  
    # 出错了: division by zero
    # 出错了: [Errno 2] No such file or directory: '不存在的文件.txt'



# except可以分开多个写
'''  
try:
    a > b
except ZeroDivisionError:
    pass
except FileNotFoundError:
    pass
except:
    print('其他的所有类型异常')
finally:
    pass
'''





# ---------------自定义异常类型--------------------
# -----抛出一个系统内置的异常-----
# password = 673
# if password > 100:
#     raise ValueError('啦啦啦错了')
# else:
#     print('没问题')



# -----抛出一个自定义类型的异常-----
# 懒得自定义error,就使用 raise ValueError("此处错误，不能xxxxx")
class NQSError(Exception):
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def __str__(self) -> str: # 打印时执行此方法
        return '长度必须要在{}至{}之间'.format(self.x, self.y)

tempLength11 = 100
tempLength22 = 200 
if 2 > 1:
    raise NQSError(tempLength11, tempLength22)  # NQSError: 长度必须要在100至200之间