import time


# -------------闭包的概念-------------
# 在一个内部函数里，调用了一个外部作用域的变量(但不是全局作用域的变量)，那么这个内部函数就被认为是闭包
# innerFunc222函数就是一个闭包
def outerFunc222():
    xx = 10
    
    def innerFunc222():
        yy = xx + 10
        return yy
    return innerFunc222
outerFunc222()()


# -------------计算函数执行的耗时------------
# time.time() 表示从1970年0点0分到目前的描述

# ------正常的耗时计算-----
print("----正常的耗时计算----")
x = 0
startTimeStamp = time.time()
for i in range(0, 30000000):
    x += i

endTimeStamp = time.time()
print('耗时：%.2f秒' % (endTimeStamp-startTimeStamp))  # 耗时：3.06秒



# ------抽象一层的的耗时计算-----
print("----抽象一层的的耗时计算----")
def calTimeFunc(func):
    startTime = time.time()
    func()
    endTime = time.time()
    print('耗时：%.2f秒' % (endTime-startTime)) 
    
def testConsumingFunc():
    x = 0
    for i in range(0, 30000000):
        x += i
    print('耗时操作结束')
    
calTimeFunc(testConsumingFunc)  # 耗时：1.91秒




# --------使用装饰器统计耗时---------
# 装饰器 带参数 和 不带参数 两种情况调用逻辑是不同的，切记！！！！
print("----使用装饰器统计耗时----")
''' 
    @cal_time发生了什么？
    1.调用cal_time
    2.把被修饰的函数当做参数传给cal_time
    3.在最后调用demo()时，实际调用的是cal_time的返回值innerFunc函数了
    4.demo()已经指向了cal_time的返回值了
    
    装饰器是python内部实现的一种语法糖，固定这样调用
    装饰器内部的函数需要定义返回值，因为不确定修饰的函数是否有返回值
'''
def cal_time(func):
    print('耗时计算方法被调用了！！')
    print('func={}'.format(func))  # func=<function demo at 0x107988720>
    
    # 入参需要占位写上，传入的func如果有入参时有用
    def innerFunc(*nqs_args):
        startTime = time.time()
        nqsResult = func(*nqs_args)  # 返回值看传入的func是否定义的有return值，没有也没啥影响
        endTime = time.time()
        print('耗时：%.2f秒' % (endTime-startTime)) 
        return nqsResult
        # return nqsResult, startTime, endTime  多个返回值以元组形式返回
    return innerFunc



# ---1.1 无入参无返回场景
@cal_time
def demo11():
    x = 0
    for i in range(0, 30000000):
        x += i
    print('耗时操作结束')
    
demo11()  # 耗时：1.95秒
print('装饰后的demo11函数：{}'.format(demo11))  # 装饰后的demo11函数：<function cal_time.<locals>.innerFunc at 0x103f88180>

# ---1.2 无入参无返回场景
@cal_time
def demo22():
    time.sleep(2)
demo22()   # 耗时：2.00秒

# ---2.无入参有返回场景
@cal_time
def demo33():
    time.sleep(1)
    return 99999
result33 = demo33()   # 耗时：1.01秒
print('返回值result33={}'.format(result33))  # 返回值result33=99999

# ---3.1 有单入参有返回场景
@cal_time
def demo44(param):
    return param*100
result44 = demo44(888)  # 耗时：0.00秒
print('返回值result44={}'.format(result44))  # 返回值result44=88800








# 最复杂场景：多个入参、多个返回
def can_play(temp_func):
    def inner(temp_name, temp_game, *args, **krargs):
        temp_func(temp_name, temp_game)
        
        age = -1
        game_time = -1
        age = krargs.get('age')
        game_time = krargs.get('clock')
        print('年龄:{}, 时间:{}'.format(age, game_time), end="-- ")
        
        if age is None:
            print('非法！！请输入用户年龄！')
        elif game_time is None:
            print('非法！！请输入游戏时间！')
        elif age > 18:
            print('已成年', end=' ')
            if game_time > 22:
                print('太晚了，睡觉把')
            else:
                print('时间合理，可以进行游戏')
        else:
            print('未成年，不能游戏')
        
        return age, game_time
    return inner
        
    

@can_play
def play_game(name, game):
    print('--{}想玩{}--'.format(name, game), end="  ")



play_game('张三', '英雄联盟')
play_game('李四', '英雄联盟', age=15)
play_game('王五', '英雄联盟', clock=21)
play_game('赵六', '英雄联盟', age=11, clock=21)
play_game('孙七', '英雄联盟', age=20, clock=23)
finalResult = play_game('周八', '英雄联盟', age=30, clock=15)
print(finalResult)  # (30, 15)

# --张三想玩英雄联盟--  年龄:None, 时间:None-- 非法！！请输入用户年龄！
# --李四想玩英雄联盟--  年龄:15, 时间:None-- 非法！！请输入游戏时间！
# --王五想玩英雄联盟--  年龄:None, 时间:21-- 非法！！请输入用户年龄！
# --赵六想玩英雄联盟--  年龄:11, 时间:21-- 未成年，不能游戏
# --孙七想玩英雄联盟--  年龄:20, 时间:23-- 已成年 太晚了，睡觉把
# --周八想玩英雄联盟--  年龄:30, 时间:15-- 已成年 时间合理，可以进行游戏