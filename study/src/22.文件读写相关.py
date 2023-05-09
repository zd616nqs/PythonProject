import os
import sys
# 绝对路径：从电脑根目录开始的路径
# 相对路径：当前文件所在的文件夹开始的路径
# ../ 表示上一级文件夹
# ./  表示当前文件夹，可以省略不写



# 在字符串前面加r，在python里表示的是原生字符串，防止字符串内有转义字符的情况
# 注意：大小写R\r都可以
# word6 = "good af\ternoon"  # 结果：good af ernoon 
# word7 = r"good af\ternoon" # 结果：good af\ternoon
# print(word6, "\n", word7)




# python使用内置函数open来打开并操作一个文件
''' 
def open(
    file: FileDescriptorOrPath,  文件路径
    mode: OpenTextMode = "r",    打开的模式: 默认r表示只读  
    buffering: int = -1,
    encoding: str | None = None,  打开时的编码方式
    errors: str | None = None,
    newline: str | None = None,
    closefd: bool = True,
    opener: _Opener | None = None
) -> TextIOWrapper: ...
'''

''' 
mode参数的说明
'r'	    读取模式，默认。只读打开文件，如果文件不存在则报错
'w'	    写入模式。打开文件进行写入，如果文件不存在则创建文件，如果文件已存在则覆盖原有内容
'x'	    独占写入模式。创建文件并进行写入，如果文件已存在则报错
'a'	    追加模式。打开文件进行写入，如果文件不存在则创建文件，写入内容追加到文件末尾
'b'	    二进制模式。以二进制模式打开文件，用于处理非文本文件，如图片、视频等
't'	    文本模式，默认。以文本模式打开文件，用于处理文本文件
'+'	    读写模式。打开文件进行读写操作
'U'	    通用换行模式，已经废弃
'r+'	读写模式。可读可写，文件指针位于文件开头
'w+'	读写模式。可读可写，如果文件存在则覆盖原有内容，如果文件不存在则创建文件
'x+'	独占读写模式。可读可写，创建文件并进行读写操作，如果文件已存在则报错
'a+'	追加读写模式。可读可写，如果文件不存在则创建文件，写入内容追加到文件末尾
'b+'	二进制读写模式。以二进制模式打开文件，可读可写
't+'	文本读写模式。以文本模式打开文件，可读可写
'rb'	二进制读取模式。以二进制模式打开文件，只读取文件内容，用于处理二进制文件
'wb'	二进制写入模式。以二进制模式打开文件进行写入，如果文件不存在则创建文件，如果文件已存在则覆盖原有内容
'xb'	独占二进制写入模式。创建二进制文件并进行写入，如果文件已存在则报错
'ab'	追加二进制写入模式。以二进制模式打开文件进行写入，如果文件不存在则创建文件，写入内容追加到文件末尾
'w+b'	二进制读写模式。可读可写，如果文件存在则覆盖原有内容，如果文件不存在则创建文件
'r+b' 或 'rb+'	二进制读写模式。可读可写，文件指针位于文件开头
'a+b' 或 'ab+'	追加二进制读写模式。可读可写，如果文件不存在则创建文件，写入内容追加到文件末尾
'''



filePath = '/Users/jeason/Downloads/project/Study/PythonProject/study/src/00.demo.py'
# file = open(filePath)
file = open(filePath, encoding='utf8')
print(file.read()) # 文件内的文本打印一遍
file.close()  # 操作完后，记得关闭文件



# ------文件读取的几种方式--------
# file.read()      将所有数据都读取出来
# file.read(1024)     读取指定字符长度的数据(用的比较多，可以防止文本太大内存溢出)
# file.readline()  只读取一行的数据
# file.readlines()  将所有行的数据都读取出来，保存到一个列表里



# -----文件mode一般不用w+，挺麻烦的，还需要移动光标位置，如下：----
# file.open('xxxx.txt', 'w+')
# file.write('牛青山')
# print(file.read('xxx.txt')) # 输出：空，因为当前光标在最后，后面没东西
# file.seek(0, 0)  # 手动将光标seek到最开始
# print(file.read('xxx.txt')) # 输出：牛青山
# file.close()







# ----------文件的拷贝-----------
old_file_path = '/Users/jeason/Downloads/pythonTest/old_file.txt'

if os.path.isfile(old_file_path):
    
    oleFile = open(old_file_path, encoding='utf8')
    
    # 方法1重命名文件：rpartition （从右向左匹配第一个.）
    # tempPathNames = old_file_path.rpartition('.')  # ('/Users/jeason/Downloads/pythonTest/old_file','.','txt')
    # new_file_path = tempPathNames[0] + '_new_v2' + '.' + tempPathNames[2]
    
    # 方法2重命名文件：splitext   （从右向左匹配第一个.）
    tempPathNames = os.path.splitext(old_file_path) # ('/Users/jeason/Downloads/pythonTest/old_file','.txt')
    new_file_path = tempPathNames[0] + '_new_v2' + tempPathNames[1]
    
    
    newFile = open(new_file_path, encoding='utf8')
    newFile.write(oleFile.read())
    
    oleFile.close()
    newFile.close()
else:
    print('老文件不存在')
    
    
    
    
    
# ----------sys标准输入输出(控制台的输入输出)----------
# sys.stdin  接收用户的输入，键盘输入的数据
# sys.stdout 标准输出
# sys.stderr 错误输出

s_in = sys.stdin
while True:
    content = s_in.readline().rstrip('\n') # 控制台输入的内容后面都会带\n，需要删除掉
    print('输入的是: ', content)
    if content == 'niu':
        break
# niuqingshan
# 输入的是:  niuqingshan


sys.stdout = open('src/22.test_stdout.txt', 'w', encoding='utf8')
print('控制台输出牛牛测试')
print('牛牛输出测试')

sys.stderr = open('src/22.test_stderr.txt', 'w', encoding='utf8')
print(1/0)