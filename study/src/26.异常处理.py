

def div(a, b):
    return a / b



# ------------常规处理方式--------------------
# 使用try...except语句处理异常，出现异常立马跳转到except内
# Exception是所有异常类型的父类，可以统一进行捕获
try:
    result = div(5, 0)
    print('此行看看打不打印')  # 没有执行这行
except Exception as e:
    print('程序出错了,原因：', e)  # 程序出错了,原因： division by zero
else:
    print('计算结果是：', result)





# ---------------只处理 指定类型的错误--------------------
try:
    result22 = div(6, 0)   # 能正确捕获崩溃
    open('不存在的文件.txt') # 能正常捕获崩溃
    
    map = {'name': 'zhangsan'}
    print(map['age'])      # 会崩溃，没有指定此种崩溃类型的捕获
    
except (ZeroDivisionError, FileNotFoundError) as e:
    print('出错了:', e)  
    # 出错了: division by zero
    # 出错了: [Errno 2] No such file or directory: '不存在的文件.txt'
