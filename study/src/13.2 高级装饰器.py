import inspect




# # 装饰器带参数的情况
# def can_play(play_age: int, play_clock: int):
#     print('--年龄:{},时间:{}'.format(play_age, play_clock), end="-- ")
    
#     def handle_action(temp_func):            # play_game函数的函数体  在这里
#         def do_action(temp_name, temp_game): # play_game函数的参数    在这里
            
#             temp_func(temp_name, temp_game)  # 真正的函数执行处：play_game('张三', '英雄联盟')
            
#             if play_age is None:
#                 print('非法！！请输入用户年龄！')
#             elif play_clock is None:
#                 print('非法！！请输入游戏时间！')
#             elif play_age > 18:
#                 print('已成年', end=' ')
#                 if play_clock > 22:
#                     print('太晚了，睡觉把')
#                 else:
#                     print('时间合理，可以进行游戏')
#             else:
#                 print('未成年，不能游戏')
#         return do_action
#     return handle_action


# @can_play(play_age=15, play_clock=23) # 装饰器带参数
# def play_game(name, game):
#     print('--{}想玩{}--'.format(name, game), end="  ")


# play_game('张三', '英雄联盟') 
# # --年龄:15,时间:23-- --张三想玩英雄联盟--  未成年，不能游戏





def can_play(limit_age: int, limit_clock: int):
    # 注意：此处只会再第一次调用temp_func(即play_game)函数时才会执行，后面再多次调用是不会走的
    print('测试代码，验证此处会执行几遍')
    
    # play_game函数的函数体,在handle_action处
    def handle_action(temp_func):       
        # play_game函数的参数，在do_action处   
        def do_action(temp_name, temp_game, now_age, now_clock):
            
            print('限制年龄:{}岁,限制时段:{}点'.format(limit_age, limit_clock), end="   ")
            
            print('申请人:', end='')
            print(f'姓名:{temp_name},年龄:{now_age}岁,游玩时段{now_clock}点', end="   ")
            print('审核结果:', end="")
            
            if now_age is None:
                print('非法！！请输入用户年龄！')
            elif limit_age is None:
                print('非法！！请输入限制年龄！')
            elif now_clock is None:
                print('非法！！请输入游戏时间！')
            elif limit_clock is None:
                print('非法！！请输入限制时间！')
            elif now_age >= limit_age:
                if now_clock < limit_age:
                    print('通过！！', end='')
                    # 真正的函数执行处：play_game('张三', '英雄联盟')
                    temp_func(temp_name, temp_game, now_age, now_clock) 
                else:
                    print('太晚了，睡觉把')
            else:
                print('未成年，不能游戏')
        return do_action
    return handle_action


# 装饰器带参数
@can_play(limit_age=18, limit_clock=23) 
def play_game(name, game, now_age, now_clock):
    print('{}正在开心的玩{}'.format(name, game))


play_game('张三', '英雄联盟', now_age=13, now_clock=21)
play_game('李四', '守望先锋', now_age=19, now_clock=15)
play_game('王五', '星穹铁道', now_age=30, now_clock=24)

'''  
测试代码，验证此处会执行几遍
限制年龄:18岁,限制时段:23点   申请人:姓名:张三,年龄:13岁,游玩时段21点   审核结果:未成年，不能游戏
限制年龄:18岁,限制时段:23点   申请人:姓名:李四,年龄:19岁,游玩时段15点   审核结果:通过！！李四正在开心的玩守望先锋
限制年龄:18岁,限制时段:23点   申请人:姓名:王五,年龄:30岁,游玩时段24点   审核结果:太晚了，睡觉把
'''









# 练习：检查权限(使用二进制按位与判断)

user_permission = 11 # 1011

DEL_PERMISSION = 8   # 1000
READ_PERMISSION = 4  # 0100
WRITE_PERMISSION = 2 # 0010
EXEC_PERMISSION = 1  # 0001

def check_permission(x, y):
    def handle_action(func):
        def do_action():
            if x & y != 0:
                func()
            else:
                print('对不起，您没有相应的权限')
        return do_action
    return handle_action

@check_permission(user_permission, DEL_PERMISSION)
def delete_file():
    print('我正在删除文件')
    
@check_permission(user_permission, READ_PERMISSION)
def read_file():
    print('我正在读取文件')
    
@check_permission(user_permission, WRITE_PERMISSION)
def write_file():
    print('我正在写入文件')
    
@check_permission(user_permission, EXEC_PERMISSION)
def exec_file():
    print('我正在执行文件')
    

delete_file()  # 我正在删除文件
read_file()    # 对不起，您没有相应的权限
write_file()   # 我正在写入文件
exec_file()    # 我正在执行文件












# -------网上找的一个例子：函数参数类型强制校验，使用inspect------
# https://blog.csdn.net/qq_39246147/article/details/129157112

def type_validate(func):
    def inner(*args, **kwargs):
        full_args_spec = inspect.getfullargspec(func)
        if args:
            new_func_args = full_args_spec.args
            if len(full_args_spec.args) != len(full_args_spec.annotations.keys()):
                args = args[1:]
                new_func_args = full_args_spec.args[1:]
            for i, v in enumerate(args):
                if not isinstance(v, full_args_spec.annotations[new_func_args[i]]):
                    raise TypeError(f"{v}不是{full_args_spec.annotations[new_func_args[i]]}")
        if kwargs:
            for k, v in kwargs.items():
                if not isinstance(v, full_args_spec.annotations[k]):
                    raise TypeError(f"{v}不是{full_args_spec.annotations[k]}")
        func(*args, **kwargs)
    return inner


@type_validate
def f(a: int, b: int):
    ...

f(1, "673")


'''  
发生异常: TypeError
673不是<class 'int'>
    File "/Users/jeason/Downloads/project/Study/PythonProject/study/src/13.2 高级装饰器.py", line 109, in inner
    raise TypeError(f"{v}不是{full_args_spec.annotations[new_func_args[i]]}")
    File "/Users/jeason/Downloads/project/Study/PythonProject/study/src/13.2 高级装饰器.py", line 122, in <module>
    f(1, "673")
TypeError: 673不是<class 'int'>
'''