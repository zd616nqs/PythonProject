
# try...finally的使用

# ------如果在代码最外层有finally的情况 ----------
# 在程序执行的最后一定会执行finally内的内容
try:
    num = 0
    while num < 55555:
        print(num)
        num += 1
finally: # 最终都会执行的代码
    print('全部执行结束111')
''' 
1
2
3
4
...
全部执行结束111
'''


# ------如果函数内有finally的情况------
# finally的返回值会覆盖之前的返回值
def demoFunc(a, b):
    try:
        result = a / b
    except Exception as e:
        print('程序出错了,原因：', e)  
        return '错误了'
    else:
        print('计算结果是：', result)
        return result
    finally:
        return 'nqs'
    
xx = demoFunc(5, 0)
print('xx: ', xx) 

# 程序出错了,原因： division by zero
# xx:  nqs

