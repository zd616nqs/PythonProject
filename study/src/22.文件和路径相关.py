
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
file操作时mode参数的说明
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
'''



filePath = '/Users/jeason/Downloads/project/Study/PythonProject/study/src/00.demo.py'
# file = open(filePath)
file = open(filePath, encoding='utf8')
print(file.read()) # 文件内的文本打印一遍
file.close()  # 操作完后，记得关闭文件





# 绝对路径：从电脑根目录开始的路径
# 相对路径：当前文件所在的文件夹开始的路径
# ../ 表示上一级文件夹
# ./  表示当前文件夹，可以省略不写


# -----文件mode一般不用w+，挺麻烦的，实例：----
# file.open('xxxx.txt', 'w+')
# file.write('牛青山')
# print(file.read('xxx.txt')) # 输出：空，因为当前光标在最后，后面没东西
# file.seek(0, 0)  # 手动将光标seek到最开始
# print(file.read('xxx.txt')) # 输出：牛青山
# file.close()


# 在字符串前面加r，在python里表示的是原生字符串，防止字符串内有转义字符的情况
# 注意：大小写R\r都可以
# word6 = "good af\ternoon"  # 结果：good af ernoon 
# word7 = r"good af\ternoon" # 结果：good af\ternoon
# print(word6, "\n", word7)


