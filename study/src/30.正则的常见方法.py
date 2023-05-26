# 参考链接：https://blog.csdn.net/m0_46926492/article/details/124412426
# 用来处理字符串，进行检索和替换
import re
from collections.abc import Iterator


# 如果想要匹配一个\,需要使用\\\\
# 还可以在匹配的字符串前面加r，纯字符串进行对比
teststr = 'niuqingshan\hello'
result11 = re.search('qing', teststr)
result12 = re.search(r'qing', teststr)
print(result11) # <re.Match object; span=(3, 7), match='qing'>
print(result12) # <re.Match object; span=(3, 7), match='qing'>

result21 = re.search('\\\\', teststr)
result22 = re.search(r'\\', teststr)
print(result21) # <re.Match object; span=(11, 12), match='\\'>
print(result22) # <re.Match object; span=(11, 12), match='\\'>




# ----------------------re模块下的方法介绍-----------------

# -----------match和search：--------------
#    共同点：1.只对字符串查询一次 2.返回值都是一个re.Match对象
#    不通点：1.match从头到尾匹配，一旦第一个字符匹配失败，就返回None 2.seach会对整个字符串进行匹配
demoStr1 = 'niuqingshan\hello'
res11 = re.search('niu', demoStr1)
res12 = re.match('niu', demoStr1)
res21 = re.search('qing', demoStr1)
res22 = re.match('qing', demoStr1)
print('res11: ', res11)  # res11:  <re.Match object; span=(0, 3), match='niu'>
print('res12: ', res12)  # res12:  <re.Match object; span=(0, 3), match='niu'>
print('res21: ', res21)  # res21:  <re.Match object; span=(3, 7), match='qing'>
print('res22: ', res22)  # res22:  None


# ---------finditer: 匹配所有的匹配项，返回一个可迭代对象----------------
res33 = re.finditer(r'2', 'lkjiowj2xiojioj2xojx2o')
print('res33: ', res33) # res33:  <callable_iterator object at 0x1045a7f10>
print(isinstance(res33, Iterator)) # True
for temp in res33:
    print(temp)
# <re.Match object; span=(7, 8), match='2'>
# <re.Match object; span=(15, 16), match='2'>
# <re.Match object; span=(20, 21), match='2'>


# ---------findall:  匹配所有的匹配项,放到一个列表里返回---------
res44 = re.findall(r'3', 'kjoijo3ojiohbn3oji3')
print('res44: ', res44) # res44:  ['3', '3', '3']

res55 = re.findall(r'3\d+', 'kjoijo332ojiohbn32oji3') # 正则匹配3后面带数字的匹配项
print('res55: ', res55) # res55:  ['332', '32']



# ---------fullmatch:完整匹配，需要字符串完全满足规则才有结果----------
res66 = re.fullmatch(r'hello world', 'hello world')
res77 = re.fullmatch(r'hello', 'hello world')
res88 = re.fullmatch(r'h.*d', 'hello world')  # 正则匹配 .任意字符(除了\以外)  *任意次数
print('res66: ', res66) # res66:  <re.Match object; span=(0, 11), match='hello world'>
print('res77: ', res77) # res77:  None
print('res88: ', res88) # res88:  <re.Match object; span=(0, 11), match='hello world'>






# ----------------------------re.Match类介绍--------------------
result = re.search(r'q.*h', 'niuqingshan')
print('result: ', result) # result:  <re.Match object; span=(3, 9), match='qingsh'>

# pos、endpos 进行搜索匹配的位置区间
print(result.pos, result.endpos) # 0 11
# span 匹配到的字符串开始和结束下标,返回元组
print(result.span())  # (3, 9)


# group 匹配到的字符串
print(result.group()) # qingsh
# group后面跟下标的话，表示正则表达式的分组
#   1.在正则表达式里，()表示一个分组
#   2.如果没有分组，默认只有一组
#   3.分组的下标从0开始
test11 = re.search(r'9.*5.*2.*8', 'kjio9iwe5niw2wvy8wvw')
print('test11: ', test11) # test11:  <re.Match object; span=(4, 17), match='9iwe5niw2wvy8'>
test22 = re.search(r'(9.*)(5.*)(2.*8)', 'kjio9iwe5niw2wvy8wvw')
print('test22: ', test22) # test22:  <re.Match object; span=(4, 17), match='9iwe5niw2wvy8'>
# 分析上面的正则表达式有4个分组
#   分组0：(9.*)(5.*)(2.*8)
#   分组1：(9.*)
#   分组2：(5.*)
#   分组3：(2.*8)
print(test22.group(0)) # 9iwe5niw2wvy8
print(test22.group(1)) # 9iwe
print(test22.group(2)) # 5niw
print(test22.group(3)) # 2wvy8


# groups把正则表达的所有分组放到一个元组内
print(test22.groups()) # ('9iwe', '5niw', '2wvy8')

# span查看表达式不同分组的开始结束范围，默认第0组
print(test22.span(0)) # (4, 17)
print(test22.span(1)) # (4, 8)
print(test22.span(2)) # (8, 12)
print(test22.span(3)) # (12, 17)


# groupdict作用是获取到分组组成的字典
# 格式：(?P<nickname>表达式) 可以给分组起名字
# 起别名，不影响group(n)取值
test33 = re.search(r'(9.*)(?P<nqs>5.*)(2.*8)', 'kjio9iwe5niw2wvy8wvw')
print(test33.groupdict()) # {'nqs': '5niw'}









# ----------------------------re.compile方法的使用--------------------
# 先得到一个compile对象，再进行匹配
# 跟re.search相比，更多的使用场景：一个通用的正则表达式，批量匹配多个字符串

nnn = re.search(r'q.*g', 'niuqingshan')
# 等效于以下:
regexFormat = re.compile(r'q.*g')
tempResult1 = regexFormat.search(r'niuqingshan')
tempResult2 = regexFormat.search(r'shanqingniu')
tempResult3 = regexFormat.search(r'niuniuqingshanshan')
print(regexFormat)                  # re.compile('q.*g')
print('tempResult1: ', tempResult1) # tempResult1:  <re.Match object; span=(3, 7), match='qing'>
print('tempResult2: ', tempResult2) # tempResult2:  <re.Match object; span=(4, 8), match='qing'>
print('tempResult3: ', tempResult3) # tempResult3:  <re.Match object; span=(6, 10), match='qing'>



# ----------------------------正则修正符flag--------------------
# class RegexFlag:
#     NOFLAG = 0
#     ASCII = A = _compiler.SRE_FLAG_ASCII # assume ascii "locale"
#     IGNORECASE = I = _compiler.SRE_FLAG_IGNORECASE # ignore case
#     LOCALE = L = _compiler.SRE_FLAG_LOCALE # assume current 8-bit locale
#     UNICODE = U = _compiler.SRE_FLAG_UNICODE # assume unicode "locale"
#     MULTILINE = M = _compiler.SRE_FLAG_MULTILINE # make anchors look for newline
#     DOTALL = S = _compiler.SRE_FLAG_DOTALL # make dot match newline
#     VERBOSE = X = _compiler.SRE_FLAG_VERBOSE # ignore whitespace and comments

# re.S 使.匹配，包括换行符\在内的所有字符
print(re.search(r'1.*5', 'nqs1wev\ne5jj'))        # None
print(re.search(r'1.*5', 'nqs1wev\ne5jj', re.S))  # <re.Match object; span=(2, 13), match='s1wev\\we5jj'>
# re.I 匹配忽略大小写
print(re.search(r'q', 'niuQingshan'))        # None
print(re.search(r'q', 'niuQingshan', re.I))  # <re.Match object; span=(3, 4), match='Q'>
# re.M 多行匹配
mmmm = '''  
niu
qing
shan
'''
print(re.search(r'^qi', mmmm))        # None
print(re.search(r'^qi', mmmm, re.M))

