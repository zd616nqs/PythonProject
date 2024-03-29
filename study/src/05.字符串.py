# ----------------字符串的基本表达方式和注意点------------------
# python 中字符串的书写格式
# 四种方式:  '你好'    "你好"    """你好"""    '''你好'''
# 多重包裹时可以区分出来，例如：
word1 = '小明说:"我是男生"'
word2 = """小红说:"我是女生" """
print(word1, "  ", word2)  # 结果：小明说:"我是男生"    小红说:"我是女生" 

# 使用转义字符
# \' 和  \"  和  \\
word3 = 'I\'m Niuqingshan'
word4 = "I am:\"linlin\""
word5 = "good mor\\ning"
print(word3, "  ", word4)  # 结果：I'm Niuqingshan    I am:"linlin"
print(word5)              # 结果：good mor\ning





# ----------------字符串的索引和切片------------------
# 字符串是不可变数据源，操作下标不能改变字符串
name = 'niuqingshan'

# 切片：从字符串里复制一段指定的内容，生成一个一个新的字符串
# 语法：name[start:end:step]  
# 取值区间：包含start，不包含end。
# 如果不写end则会截取到最后。  如果不设置start，会从头截取
# step：截取的步长，默认1依次取（等于0时报错，小于0时表示从右往左获取）
print(name[3])       # 结果：q
# name[3] = 'm'      # 操作不可变数据源，会报错
print(name[3:7])     # 结果：qing         取值范围[3,7)（步长step默认为1）
print(name[3:7:2])   # 结果：qn           取值范围[3,7)（步长step为2）

print(name[3:])      # 结果：qingshan     取值范围[3,end]（从第3位截取到最后）
print(name[-3:])     # 结果：han          取值范围[len-3,end]（从倒数第3位截取到最后）

print(name[:3])      # 结果：niu          取值范围[0,3)（从头截取到第三位）
print(name[:-3])     # 结果：niuqings     取值范围[0,len-3)（从头截取到倒数第三位）

print(name[::])      # 结果：niuqingshan （从头到尾复制）
print(name[::-1])    # 结果：nahsgniquin （倒序）


print(name[-8:-4])       # 结果：qing   取值范围[len-8,len-4)（从左至右打印）
print(name[-8:-4:1])     # 结果：qing   取值范围[len-8,len-4)（从左至右打印）
print(name[-8:-4:-1])    # 结果：空，错误写法

print(name[-4:-8])       # 结果：空，错误写法
print(name[-4:-8:1])     # 结果：空，错误写法
print(name[-4:-8:-1])    # 结果：sgni 取值范围(len-8,len-4]的字符串反向打印





# ----------------字符串查找操作------------------
# 常见的方法： find、index、rfind、rindex
# rfind rindex 查找顺序从右向左(起始index从0开始，匹配字符串的首字母的index)
# 参数：s.index(x, start, end)
name222 = 'niuqingqingshan'
print(name222.find("qi"))      # 结果：3('q'从左往右数index为3)
print(name222.index("qi"))     # 结果：3('q'从左往右数index为3)

print(name222.find("mama"))    # 结果：-1
# print(name222.index("mama")) # 结果：没有找到，会报错

print(name222.rfind("qi"))     # 结果：7('q'从右往左数index为7)
print(name222.rindex("qi"))    # 结果：7('q'从右往左数index为7)



# ----------------字符串判断相关------------------
# isalpha 是否纯字母
# isdigit 是否纯数字
# isalnum 是否只有数字+字母(不能有其他类型的字符)
# isspace 是否全部由空格组成
# count 关键字出现了几次
# startswith 是否以某关键字开始
# endswith   是否以某关键字结束
name333 = 'niuqingshan'
print(name333.startswith('niu'))  # 结果：True
print(name333.endswith('shan'))   # 结果：True
print('ni2u'.isalpha())   # 结果：False
print('ni2u'.isdigit())   # 结果：False
print('ni2u'.isalnum())   # 结果：True
print('ni2u-'.isalnum())  # 结果：False  不能有其他类型的字符
print('    '.isspace())   # 结果：True
print('牛牛牛'.count('牛'))  # 结果：3


# ----------------字符串替换------------------
name444 = 'niuqingshan'
print(name444.replace('qing', 'xxx'))  # 结果：niuxxxshan



# ----------------字符串修改大小写----------------------
# caitalize 首字母大写,其余字母都变成小写
# upper 所有字母大写
# lower 所有字母小写
# title 每个单词的首字母大写，其他字母变小写
name555 = 'niu qing SHAN'
print(name555.capitalize())  # 结果：Niu qing shan
print(name555.upper())       # 结果：NIU QING SHAN
print(name555.lower())       # 结果：niu qing shan
print(name555.title())       # 结果：Niu Qing Shan


# ----------------字符串用0填充----------------------
# s.zfill(x) 用字符0填充到s的左边，直到字符串长度达到x
name1992 = "niu".zfill(10)
print(f'name1992:{name1992}')  # name1992:0000000niu

name1993 = "+$#!niu".zfill(10)
print(f'name1993:{name1993}') # name1993:+000$#!niu

name1994 = "+$#!niu".zfill(2)
print(f'name1994:{name1994}') # name1994:+$#!niu


# ----------------字符串删除前缀后缀----------------------
nqs1992 = "www.baidu.com"
nqs1993 = nqs1992.removeprefix("www")
nqs1994 = nqs1993.removesuffix("com")
print('nqs1994: ', nqs1994)  # .baidu.



# ----------------字符串空格处理----------------------
# ljust(length,fillchar)  让字符以指定长度显示(左对齐)，如果长度不够用填充字符(默认空格)补充，如果长度太短就打印原本的字符串
# center(length,fillchar) 让字符以指定长度显示(居中对齐)，如果长度不够用填充字符(默认空格)补充，如果长度太短就打印原本的字符串
# lstrip 删除左边的空格(匹配从左到右的第一段空格)
# rstrip 删除右边的空格(匹配从右到左的第一段空格)
name666 = 'niuqingshan'
print("start"+name666.ljust(30)+"end")       # 结果：startniuqingshan                   end
print("start"+name666.ljust(30, '-')+"end")  # 结果：startniuqingshan-------------------end
print("start"+name666.ljust(5)+"end")        # 结果：startniuqingshanend

print("start"+name666.rjust(30)+"end")       # 结果：start                   niuqingshanend
print("start"+name666.rjust(30, '-')+"end")  # 结果：start-------------------niuqingshanend
print("start"+name666.rjust(5)+"end")        # 结果：startniuqingshanend

print(name666.center(30, '-'))        # 结果：---------niuqingshan----------
print(name666.center(5, '-'))         # 结果：niuqingshan

name777 = "    niu  qing  shan   "
print("mark"+name777.lstrip()+"mark")  # 结果：markniu  qing  shan   mark
print("mark"+name777.rstrip()+"mark")  # 结果：mark    niu  qing  shanmark


# --------------------字符串分割----------------------
# 常见方法：split  rsplit splitlines partition rpartition
demo = 'niu-qing-shan-dao-ci-yi-you'


# ----split----
# 分割后返回一个列表（从左到右执行）
# 参数1：标识分割的字符串 参数2：分割的次数
# rsplit(从右向左执行)
print(demo.split('-'))      # 结果：['niu', 'qing', 'shan', 'dao', 'ci', 'yi', 'you']
print(demo.split('-', 2))   # 结果：['niu', 'qing', 'shan-dao-ci-yi-you']
print(demo.rsplit('-', 2))  # 结果：['niu-qing-shan-dao-ci', 'yi', 'you']
# 额外：列表转换车字符串
print('!'.join(demo.split('-')))  # 结果：niu!qing!shan!dao!ci!yi!you


# ----splitlines-----
# 按照行分割，返回一个各行作为元素的列表
mydemo = "hello \nworld \nniuniu"
print(mydemo.splitlines()) # 结果：['hello ', 'world ', 'niuniu']


# ----partition-----
# 把字符串以关键词进行分割，关键词前+关键词+关键词后，返回一个元组tuple （从左到右执行）
# partition(匹配关键词从左向右执行，分割从左往右)
# rpartition(匹配关键词从右向左执行，但是分割还是从左往右)
mydemo2 = "牛青山到此山一游"
print(mydemo2.partition("山"))      # 结果：('牛青', '山', '到此山一游')
print(mydemo2.rpartition("山"))     # 结果：('牛青山到此', '山', '一游')

print(mydemo2.partition("到此山"))   # 结果：('牛青山', '到此山', '一游')
print(mydemo2.rpartition("到此山"))  # 结果：('牛青山', '到此山', '一游')

print(mydemo2.partition("牛青山"))   # 结果：('', '牛青山', '到此山一游')
print(mydemo2.rpartition("牛青山"))  # 结果：('', '牛青山', '到此山一游')

print(mydemo2.partition("一游"))    # 结果：('牛青山到此山', '一游', '')
print(mydemo2.rpartition("一游"))   # 结果：('牛青山到此山', '一游', '')



# ------------------字符串的格式化打印----------------------
# %s  字符串
# %d  整型
# %nd 整型，显示n位，不够的话前面使用空格补齐
# %f  浮点型，进行四舍五入
# %x 打印内存地址
# ----方式1----
name888 = "张三"
age111 = 22
money = 999.987
print('大家好，我叫%s，今年%d岁了，挣了%.2f钱' % (name888, age111, money))
# 结果：大家好，我叫张三，今年22岁了，挣了999.99钱
print('当前时间:%02d:%02d:%02d' % (13, 8, 55))
# 当前时间:13:08:55

# ----方式2----
# 使用{}占位，就可以不考虑变量的类型
print('大家好，我叫{}，今年{}岁了，挣了{}钱'.format(name888, age111, money)) 
# 结果：大家好，我叫张三，今年22岁了，挣了999.987钱

# ----方式3----
print('大家好，我叫{nameTag}，今年{ageTag}岁了，挣了{moneyTag}钱'.format(nameTag=name888, ageTag=age111, moneyTag=money))  
# 结果：大家好，我叫李四，今年8岁了，挣了8888.88钱

# ----方式4----
# 使用下标的方式标识（以下4种写法输出相同）
# 结果：大家好，我叫李四，今年8岁了，挣了8888.88钱
print('大家好，我叫{0}，今年{1}岁了，挣了{2}钱'.format('李四', 8, 8888.88))  
print('大家好，我叫{2}，今年{1}岁了，挣了{0}钱'.format(8888.88, 8, '李四'))  
print('大家好，我叫{nameTag}，今年{1}岁了，挣了{0}钱'.format(8888.88, 8, nameTag='李四'))  
# print('大家好，我叫{name673}，今年{2}岁了，挣了{1}钱'.format('占位啦啦啦', 8888.88, 8, name673='李四'))  下标不对应，会报错

# ----方式5-----
# 使用  *listData  的方式遍历 数组 (以下2种写法输出相同)
listData = ["牛牛", 18, 20000]
print('大家好，我叫{}，今年{}岁了，挣了{}钱'.format(listData[0], listData[1], listData[2])) 
print('大家好，我叫{}，今年{}岁了，挣了{}钱'.format(*listData)) 
# 使用  **dictData  的方式遍历 字典 (以下2种写法输出相同)
dictData = {"name": "青青", "age": 22, "money": 66666}
print('大家好，我叫{}，今年{}岁了，挣了{}钱'.format(dictData['name'], dictData['age'], dictData['money'])) 
print('大家好，我叫{name}，今年{age}岁了，挣了{money}钱'.format(**dictData)) # 占位的key必须跟dict内的key名称一致，否则会报错
# 使用format_map 遍历字典
print('大家好，我叫{name}，今年{age}岁了，挣了{money}钱'.format_map(dictData)) 

# ----方式6------
# 在字符串前面加r，在python里表示的是原生字符串，防止字符串内有转义字符的情况
# 注意：大小写R\r都可以
word6 = "good af\ternoon"  # 结果：good af ernoon 
word7 = r"good af\ternoon" # 结果：good af\ternoon
print(word6)
print(word7)

# 在字符串前面加f或者F，可以直接使用变量名
testStr1 = '牛牛'
testStr2 = '泰山'
print(f'姓名:{testStr1},去{testStr2}旅游') # 姓名:牛牛,去泰山旅游

# rf或者fr混合使用，等效
print(rf'good af\ternoon 姓名：{testStr1},去{testStr2}旅游') 
print(fr'good af\ternoon 姓名：{testStr1},去{testStr2}旅游') 
# good af\ternoon 姓名：牛牛,去泰山旅游
# good af\ternoon 姓名：牛牛,去泰山旅游