
# 装饰器带参数的情况
def can_play(play_age: int, play_clock: int):
    print('--年龄:{},时间:{}'.format(play_age, play_clock), end="-- ")
    
    def handle_action(temp_func):            # play_game函数的函数体  在这里
        def do_action(temp_name, temp_game): # play_game函数的参数    在这里
            
            temp_func(temp_name, temp_game)  # 真正的函数执行处：play_game('张三', '英雄联盟')
            
            if play_age is None:
                print('非法！！请输入用户年龄！')
            elif play_clock is None:
                print('非法！！请输入游戏时间！')
            elif play_age > 18:
                print('已成年', end=' ')
                if play_clock > 22:
                    print('太晚了，睡觉把')
                else:
                    print('时间合理，可以进行游戏')
            else:
                print('未成年，不能游戏')
        return do_action
    return handle_action


@can_play(play_age=15, play_clock=23) # 装饰器带参数
def play_game(name, game):
    print('--{}想玩{}--'.format(name, game), end="  ")


play_game('张三', '英雄联盟') # --年龄:15,时间:23-- --张三想玩英雄联盟--  未成年，不能游戏







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



