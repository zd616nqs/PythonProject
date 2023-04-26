# ------------模块导入的方式介绍-----------
# python为了方便开发，提供了很多内置模块，导入模块后，就可以使用这个模块内的func和var了
# 
# import time                           # 1.导入一整个模块
# import datetime as nqs_dt             # 2.导入一个模块并起个别名
# from random import randint            # 3.导入一个模块内的方法或者变量
# from copy import deepcopy as nqs_dp   # 4.导入一个模块内的方法或者变量并起个别名
# from math import *                    # 5.导入一个模块内的所有方法和变量


# random.randint(0,4)  #会报错，没有导入random模块
# randint(0, 4)  # 生成0-4的随机数

# print(pi)  # 3.141592653589793

# nqs_dp([1, 2, 3])
