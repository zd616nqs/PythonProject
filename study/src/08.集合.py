# --------------集合的基本使用----------------
# 集合特点：无序、元素不重复
# 集合跟字典书写方式区分：字典：键值对  集合：单个元素
testSet = {'niu', 'qing', 'shan'}
print('testSet: ', testSet)  # 每次打印顺序是随机的

tuple111 = (1, 2, 3, 4)
tuple222 = (3, 4, 5, 6)
total = set(tuple111 + tuple222)
print('total: ', total)  # 结果：total:  {1, 2, 3, 4, 5, 6}



# 添加一个元素
testSet.add('哈哈哈')
print('testSet: ', testSet) # testSet:  {'niu', 'qing', 'shan'}

# 删除一个元素 pop、remove、discard
# 1.pop     随机删掉一个元素
# 2.remove  删除一个指定的元素(元素不存在时会报错)
# 3.discard 删除一个指定元素(元素不存在不会报错)
testSet.pop()         
print('testSet111: ', testSet) # testSet111:  {'qing', '哈哈哈', 'shan'}

# testSet.remove('66666') 

testSet.discard('哈哈哈')
print('testSet333: ', testSet) # testSet333:  {'qing', 'shan'}




# ---union：a.union(b) 将集合a和b取并集，返回一个新的集合
aaa = {'111', '222'}
bbb = {'222', '777', '888'}
xxx = aaa.union(bbb)
print(f'aaa:{aaa} bbb:{bbb} xxx:{xxx}') 
# 结果：aaa:{'222', '111'} bbb:{'222', '888', '777'} xxx:{'111', '888', '777', '222'}
print('aaa:%x bbb:%x xxx:%x' % (id(aaa), id(bbb), id(xxx))) 
# 结果：aaa:105d925e0 bbb:105d92dc0 xxx:105d92ea0


# ---update:a.update(b) 将集合b拼进集合a内
aaa.update(bbb)
print('aaa:{}, bbb:{}'.format(aaa, bbb))  
# 结果：aaa:{'111', '888', '777', '222'}, bbb:{'888', '777', '222'}
print('aaa:%x bbb:%x' % (id(aaa), id(bbb))) 
# 结果：aaa:104f725e0 bbb:104f72dc0


# 清空集合
testSet.clear()
print(testSet)  # 结果：set()   注意：空的集合不是{},而是 set()


# --------------集合的高级使用----------------
# set 支持很多算数运算符

# 不支持加号+

# -：减法  (作为减数的集合，去除共有项)
# 备注：ccc和ddd的值没有发生变化
ccc = {'111', '222'}
ddd = {'222', '777', '888'}
print(ccc - ddd)  # 结果：{'111'}
print(ddd - ccc)  # 结果：{'777', '888'}

# &:求交集
print(ccc & ddd)  # 结果：{'222'}

# |：求并集
print(ccc | ddd)  # 结果：{'222', '888', '111', '777'}

# ^：异或(并集去除交集部分)
print(ccc ^ ddd)  # 结果：{'888', '111', '777'}


# ------------集合的推导式---------
ss1 = {i * 11 for i in range(1, 6)}
print(ss1) # {33, 11, 44, 22, 55}

names = ['张三', '李四', '王五', '赵六']
ss2 = {name[0] for name in names}
print(ss2) # {'李', '张', '赵', '王'}