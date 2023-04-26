import os



# -----------------------__file__ 和 __name__介绍------------------
# 参考链接：https://blog.csdn.net/Reid_Lv/article/details/87634388/
'''__file__是Python中内置的变量，它表示当前文件的文件名
    由系统决定是否是全名:
    - 若显示执行Python，会得到绝对路径; 例如：$ python -u 'xxxpath/xxx.py'  
    - 若按相对路径来直接执行脚本./demo.py，会得到相对路径。
    参考链接：
    http://www.python66.com/bbs/215.html
    https://www.jianshu.com/p/bfa29141437e
    https://blog.csdn.net/leorx01/article/details/71141643
'''


#######################################################################
# 讨论："python xxx.py"显示调用的前提下，存在引用依赖和不存在引用依赖的值是否一样
#######################################################################
# --------情况1：运行单独文件，没有引用关系的情况-------
# 1.目录结构：
''' 
.
└── singleFileTest.py
'''
# 2.文件内容
''' 
cat singleFileTest.py
    print("运行单独文件，__name__打印值：",__name__)  
    print("运行单独文件，__file__打印值：",__file__)  
'''
# 3.执行脚本'python3 singleFileTest.py'结果：
'''
运行单独文件，__name__打印值： __main__
运行单独文件，__file__打印值： /Users/jeason/Desktop/testProject/singleFileTest.py
'''


# ---------情况2：文件存在依赖引用的情况----------
# 1.目录结构：
''' 
.
├── dependFileTest.py
└── sub
    ├── __init__.py
    └── nqs.py
'''
# 2.文件内容
''' 
cat dependFileTest.py
    import os
    print("存在文件引用，dependFileTest文件：__name__打印值：",__name__)  
    print("存在文件引用，dependFileTest文件：__file__打印值：",__file__) 
    print()
    from sub import nqs
cat sub/nqs.py
    import os
    print("存在文件引用，nqs文件：__name__打印值：",__name__)  
    print("存在文件引用，nqs文件：__file__打印值：",__file__) 
    print()
'''
# 3.执行脚本'python3 dependFileTest.py'结果：
'''
存在文件引用，dependFileTest文件：__name__打印值： __main__
存在文件引用，nqs文件：           __name__打印值： sub.nqs
存在文件引用，__init__文件：      __name__打印值： sub

存在文件引用，dependFileTest文件：__file__打印值： /Users/jeason/Desktop/testProject/dependFileTest.py
存在文件引用，nqs文件：           __file__打印值： /Users/jeason/Desktop/testProject/sub/nqs.py
存在文件引用，__init__文件：      __file__打印值： /Users/jeason/Desktop/testProject/sub/__init__.py
'''

# ----------结论---------
''' 
"python xxx.py"显示调用的前提下：
__name__
    1.单独执行一个文件，没有引用的情况：
     * 结果就是'__main__'
    2.文件存在相互引用的情况
     * 执行文件：         打印：__main__
     * 被引用普通文件：    打印：祖父包名.父包名.被导入文件名(不带扩展名)
     * 被引用__init文件： 打印：祖父包名.父包名
__file__
    1.单独执行一个文件，没有引用的情况：
     * 打印执行文件的绝对路径(带扩展名)
    2.文件存在相互引用的情况
     * 执行文件：         打印：执行文件        的绝对路径(带扩展名)
     * 被引用普通文件：    打印：被引用普通文件   的绝对路径(带扩展名)
     * 被引用__init文件： 打印：被引用__init文件 的绝对路径(带扩展名)
'''








# -----------常见的系统内置模块----------

# ---os模块----
# 调用操作系统里的方法 
# 官方文档：https://docs.python.org/zh-cn/3.11/library/os.path.html

# 1.系统名字：  window系统：nt 非window系统：posix  
print('os.name: ', os.name)  # os.name:  posix    
# 2.路径的分隔符：winddos:\   非windows:/
print('os.sep: ', os.sep)  # os.sep:  /    

# 3.获取当前项目根目录文件夹名(不一定是文件所在文件夹)
print('os.getcwd(): ', os.getcwd())  # /Users/jeason/Downloads/project/Study/PythonProject/study
print()

# TODO:以下打印结果都是IDE环境执行结果  ./demo.py方式不通用
# 4..绝对路径和相对路径
print(os.path.abspath(__file__))                           # /Users/jeason/Downloads/project/Study/PythonProject/study/src/14.模块的使用.py
print(os.path.realpath(__file__))                          # /Users/jeason/Downloads/project/Study/PythonProject/study/src/14.模块的使用.py
print(os.path.dirname(os.path.abspath(__file__)))          # /Users/jeason/Downloads/project/Study/PythonProject/study/src
print(os.path.dirname(os.path.realpath(__file__)))         # /Users/jeason/Downloads/project/Study/PythonProject/study/src
# ！！避免直接传入文件名，打印出来的path中间会缺少一级的情况，有问题
# print(os.path.abspath('14.模块的使用.py'))                   # /Users/jeason/Downloads/project/Study/PythonProject/study/14.模块的使用.py
# print(os.path.realpath('14.模块的使用.py'))                  # /Users/jeason/Downloads/project/Study/PythonProject/study/14.模块的使用.py
# print(os.path.dirname(os.path.abspath('14.模块的使用.py')))  # /Users/jeason/Downloads/project/Study/PythonProject/study
# print(os.path.dirname(os.path.realpath('14.模块的使用.py'))) # /Users/jeason/Downloads/project/Study/PythonProject/study
print()

# 5.路径是否是文件夹
# 解释：https://docs.python.org/zh-cn/3.11/library/os.path.html#os.path.isdir
print('os.path.isdir: ', os.path.isdir(__file__))     # False
print('os.path.isdir: ', os.path.isdir('src'))        # True
# 6.路径是否是文件
# 解释：https://docs.python.org/zh-cn/3.11/library/os.path.html#os.path.isfile
# print('os.path.isfile: ', os.path.isfile(__file__))   # True
print('os.path.isfile: ', os.path.isfile('src'))      # False
# print('os.stat(tempFilePath): ', os.stat(tempFilePath))
print()

# 7.文件或文件夹是否存在
# 解释：https://docs.python.org/zh-cn/3.11/library/os.path.html#os.path.exists
print('os.path.exists: ', os.path.exists(__file__))                  # True
print('os.path.exists: ', os.path.exists(os.path.dirname(__file__))) # True
print('os.path.exists: ', os.path.exists('14.模块的使用.py'))          # False

# 8.分隔路径
# 将路径名称 path 拆分为 (root, ext)
# 解释：https://docs.python.org/zh-cn/3.11/library/os.path.html#os.path.splitext
testFileName = 'nqstest.py' 
print('os.path.splitext: ', os.path.splitext(testFileName))  # os.path.splitext:  ('nqstest', '.py')
print()

# 9.分隔路径
# 将文件路径名称分成头和尾一对，生成二元元组。（文件目录，文件名）
# 解释：https://docs.python.org/zh-cn/3.11/library/os.path.html#os.path.split
print('os.path.split: ', os.path.split(testFileName))        # os.path.split:     ('', 'nqstest.py')
print()

# 10.另外一些常用的命令
# os.chdir('testDir')      # 改变当前脚本执行目录，相当月shell下的cd命令
# os.chdir('../')
# os.rename("demo.txt", "demo_final.txt")  # 文件重命名
# os.remove("demo.txt")    # 删除文件
# os.rmdir("demoDir")      # 删除空文件夹
# os.removedirs("projectDir/demoDir/demo.txt")  # 从内向外递归删除文件夹
# os.mkdir('newDemoDir')   # 创建文件夹
# os.listdir("/Users/jeason/Downloads/project/Study/PythonProject/study") # 列出指定目录里的所有文件和文件夹
# os.environ['HOME']       # 获取到环境配置(macOS设置 environ 可能导致内存泄漏)
# os.putenv("PATH")        # 获取指定的环境变量(macOS设置 environ 可能导致内存泄漏)

# 设置系统环境变量
#   os.environ[‘环境变量名称’]=‘环境变量值’ #其中key和value均为string类型
#   os.putenv(‘环境变量名称’, ‘环境变量值’)
# 获取系统环境变量
#   os.environ[‘环境变量名称’]
#   os.getenv(‘环境变量名称’)





