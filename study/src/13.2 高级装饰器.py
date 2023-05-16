
# 装饰器带参数的情况
def can_play(play_age: int, play_clock: int):
    print('--年龄:{},时间:{}'.format(play_age, play_clock), end="-- ")
    
    def handle_action(fn):
        def do_action(user_name, game_name):
            
            fn(user_name, game_name)
            
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
