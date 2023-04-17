import copy
# ------------------列表的基本使用-------------
names111 = ['牛', '青', '山', '到', '次', '一', '游']

# ----list(可迭代对象)----
names222 = list('兰陵王')                # 放入字符串
names333 = list(('niu', 'qing', 'shan'))  # 放入元组
print(names222)  # 结果；['兰', '陵', '王']
print(names333)  # 结果：['niu', 'qing', 'shan']

# ----数组切片-----
print(names111[1:3])  # 结果：['青', '山']


# -----增删改查------
# 1.添加数组元素 append、insert、extend
names444 = ['牛', '青', '山', '到', '次', '一', '游']
# *****添加：append(字符串)*****
names444.append('append')
print(names444)  # 结果：['牛', '青', '山', '到', '次', '一', '游', 'append']

# *****插入：insert(下标, 字符串)*****
names444.insert(1, 'insert')
print(names444)  # 结果：['牛', 'insert', '青', '山', '到', '次', '一', '游', 'append']

# *****扩展：extend(可迭代对象)*****
names444.extend(['扩展1', '扩展2'])
print(names444)  # 结果：['牛', 'insert', '青', '山', '到', '次', '一', '游', 'append', '扩展1', '扩展2']



# 2.删除数组元素 pop、remove、clear
names555 = ['牛', '青', '山', '到', '次', '一', '游']
# *****pop() 删除并返回一个下标的元素(默认删除最后一个元素）*****
xx11 = names555.pop()
xx22 = names555.pop(0)
print(xx11)  # 结果：游
print(xx22)  # 结果：牛
print(names555)  # 结果：['青', '山', '到', '次', '一']

# *****remove(str) 删除一个指定的元素*****
names555.remove('山')
# names555.remove('山')  #删除不存在的元素，会报错
print(names555)  # 结果：['青', '到', '次', '一']

# *****clear()清空数组*****
names555.clear()
print(names555)  # 结果：[]

# ***** del关键词也能删除，但是不推荐使用，del有其他更复杂的作用******
names666 = ['牛', '青', '山']
del names666[1]
print(names666)  # 结果：['牛', '山']



# 3.查询数组元素 index、count、in、not in
names777 = ['牛', '青', '山', '到', '次', '一', '游']
print(names777.index('青'))  # 结果：1
print(names777.count('青'))  # 结果：1
print('山' in names777)      # 结果：True
print('山' not in names777)  # 结果：False
# 注意：取数组的最后一个元素的快捷写法
names777[-1]
print(names777[-1])  # 结果：游


# 4.修改数组元素
names888 = ['牛', '青', '山']
names888[1] = '666'
print(names888)  # 结果：['牛', '666', '山']









# ------------------列表的遍历-------------
listArr = ['牛', '青', '山', '到', '次', '一', '游']
# for in循环
for temp in listArr:
    print(temp)
    
# while循环
tempIdx = 0
while tempIdx < len(listArr):
    print(listArr[tempIdx])
    tempIdx += 1
    
    

# 练习：冒泡排序
# python内交换两个变量的值写法：  a, b = b, a
nums = [5, 2, 6, 1, 3, 8, 7]
i = 0
while i < len(nums) - 1:
    i += 1
    currentIdx = 0
    while currentIdx < (len(nums) - 1 - i):
        if nums[currentIdx] > nums[currentIdx+1]:
            nums[currentIdx], nums[currentIdx+1] = nums[currentIdx+1], nums[currentIdx]
        currentIdx += 1
print(nums)  # 结果：[1, 2, 3, 5, 6, 8, 7]


# ------------------列表的排序/反转-------------
# sort、sorted、reverse、arr[::-1]
sortArr111 = [5, 2, 6, 1, 3, 8, 7]

sortArr111.sort()
print(sortArr111)  # 结果：[1, 2, 3, 5, 6, 7, 8]

sortArr111.sort(reverse=True)
print(sortArr111)  # 结果：[8, 7, 6, 5, 3, 2, 1]

sortNewArr = sorted(sortArr111)
print('sortNewArr: ', sortNewArr)  # 结果:sortNewArr:  [1, 2, 3, 5, 6, 7, 8]

sortArr222 = [1, 2, 3]
sortArr222.reverse()
print('sortArr222: ', sortArr222)  # 结果：sortArr222:  [3, 2, 1]

sortArr333 = [1, 2, 3]
sortArr333 = sortArr333[::-1]
print('sortArr333: ', sortArr333)  # 结果：sortArr333:  [3, 2, 1]




# ------------------可变数组、不可变数组-------------
# python内定义：
# 不可变类型：字符串、数字、元组
# 可变类型：列表、字典、集合


# -----复制------
# 打印内存地址查看
aaa = 12
bbb = aaa
print('修改前：a=%x,b=%x' % (id(aaa), id(bbb)))  
# 结果：修改前：a=105246188,b=105246188
aaa = 18
print('修改后：a=%x,b=%x' % (id(aaa), id(bbb)))  
# 结果：修改后：a=105246248,b=105246188

aaaArr = [1, 2, 3, 4]
bbbArr = aaaArr
cccArr = aaaArr.copy()
# cccArr = copy.copy(aaaArr)  使用copy库的写法等效
print('地址：aaaArr=%x,bbbArr=%x,cccArr=%x' % (id(aaaArr), id(bbbArr), id(cccArr)))  
#  结果：地址：aaaArr=107372480,bbbArr=107372480,cccArr=1046546c0


# -----浅拷贝-----
# 只会拷贝最外层的数据，内层的不拷贝而是直接指向
# 注意：数组的切片也是浅拷贝 arr[::]
word1 = ['牛', '青', ['s', 'h', 'a', 'n'], '666']
word2 = copy.copy(word1)

word2[0] = '111'     # 只有word2改变了
word2[2][0] = '222'  # 都被改变了，因为是浅拷贝，word2和word1内的二级对象指向同一块内存

print(word1)  # 结果：['牛', '青', ['222', 'h', 'a', 'n'], '666']
print(word2)  # 结果：['111', '青', ['222', 'h', 'a', 'n'], '666']

# -----深拷贝-----
# 所有层次的对象递归拷贝
word111111 = ['牛', '青', ['s', 'h', 'a', 'n'], '666']
word222222 = copy.deepcopy(word111111)

word222222[0] = '111'     # 只有word2改变了
word222222[2][0] = '222'  # 只有word2改变了

print(word111111)  # 结果：['牛', '青', ['s', 'h', 'a', 'n'], '666']
print(word222222)  # 结果：['111', '青', ['222', 'h', 'a', 'n'], '666']




# 练习：删除数组里的空字符串
exampleArr = ['klj', 'wer', '', '   ', '234', '']
resultExampleArr = []
for word in exampleArr:
    if word != '':
        resultExampleArr.append(word)
print(resultExampleArr)  # 结果：['klj', 'wer', '   ', '234']



# ------------------列表的推导式------------------
# 语法糖，快捷的创建列表
# 仅适合简单的条件，如果有复杂的条件，就最好别用这种语法糖

# 基本使用
testArr = [i for i in range(10)]
print('testArr: ', testArr)  # 结果：testArr:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 类比起来类似于：
# for i in range(10):
#     testArr.append(i)

# 还能添加if继续写
testArr222 = [i for i in range(10) if i % 2 == 0]
print('testArr222: ', testArr222)  # 结果：testArr222:  [0, 2, 4, 6, 8]
# 类比起来类似于：
# for i in range(10):
#     if i % 2 == 0:
#         testArr222.append(i)

# 还能表示都是元组的数组
points = [(x, y) for x in range(1, 4) for y in range(10, 12)] 
print('points: ', points)  # 结果points:  [(1, 10), (1, 11), (2, 10), (2, 11), (3, 10), (3, 11)]

# 实现把一个列表里的所有元素3个一组变成二维数组
# 使用切片功能
demoArr888 = [i for i in range(0, 101)]
demoArr999 = [demoArr888[j: j+3] for j in range(0, 100, 3)]  # range需要设置步长3
print('demoArr999: ', demoArr999)
# demoArr999:  [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14], [15, 16, 17], [18, 19, 20], [21, 22, 23], [24, 25, 26], [27, 28, 29], [30, 31, 32], [33, 34, 35], [36, 37, 38], [39, 40, 41], [42, 43, 44], [45, 46, 47], [48, 49, 50], [51, 52, 53], [54, 55, 56], [57, 58, 59], [60, 61, 62], [63, 64, 65], [66, 67, 68], [69, 70, 71], [72, 73, 74], [75, 76, 77], [78, 79, 80], [81, 82, 83], [84, 85, 86], [87, 88, 89], [90, 91, 92], [93, 94, 95], [96, 97, 98], [99, 100]]



# ------------------元组------------------
# 元组是不可变类型、列表是可变类型
# 元组是有序的存储容器，可以通过下标取值
# 如果元组里只有一个元素，需要在最后加一个,号 num = (673,)
# 常用方法：tuple.index(2)  tuple.count()


# 列表和元组相互转换
tuple111 = (1, 2, 3, 4)
list111 = [5, 6, 7, 8]
print(list(tuple111))  # 结果：[1, 2, 3, 4]
print(tuple(list111))  # 结果：(5, 6, 7, 8)

# 元组转字符串
tuple222 = ('178', '18', '666')
list333 = '_'.join(tuple222)
print('list333: ', list333)  # 结果：list333:  178_18_666


# 元组遍历
for i in tuple222:
    print(i, end=' ')   # 结果：178 18 666