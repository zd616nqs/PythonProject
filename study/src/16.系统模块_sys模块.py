import sys

# ----------sys系统模块-------
# 官方文档：https://docs.python.org/zh-cn/3.11/library/sys.html



# sys.path  系统查找模块时，进行查询索引的所有查询目录
print('sys.path: ', sys.path)
# [
# '/Users/jeason/Downloads/project/Study/PythonProject/study/src', 
# '/Users/jeason/.pyenv/versions/3.11.0/lib/python311.zip', 
# '/Users/jeason/.pyenv/versions/3.11.0/lib/python3.11', 
# '/Users/jeason/.pyenv/versions/3.11.0/lib/python3.11/lib-dynload', 
# '/Users/jeason/Downloads/project/Study/PythonProject/study/.venv/lib/python3.11/site-packages'
# ]

# sys.stdin   可以像input一样，接收用户的输入,也可多接收多次输入的总数据
# sys.stdout  可以改变默认输出位置
# sys.stderr  可以改变错误输出的默认位置
print('请输入用户名')
name = sys.stdin.readline()
print('输入的是：', name)


# sys.path[0] （绝对路径或相对路径）
#  获取文件当前工作目录路径
#  sys.argv[0]|获得模块所在的路径（由系统决定是否是全名）
#   -  若显示调用python指令，如python demo.py，会得到绝对路径
#   -  若直接执行脚本，如./demo.py，会得到相对路径。
print(sys.path[0])  # /Users/jeason/Downloads/project/Study/PythonProject/study/src


# sys.exit()  # 退出程序