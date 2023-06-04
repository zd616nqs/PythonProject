# --------------字典的基本使用----------------
person = {
    'name': '牛轻松',
    'age': 18,
    'height': 176,
    'gender': 'male',
    'hobbies': ['唱', '跳', '篮球', 'rap'],
    666: 'good',  # python内key值必须是不可变数据，所以int、元组也可以当key
    ('1', '2', '3'): 'hello',
}
print(person)  # 结果：{'name': '牛轻松', 'age': 18, 'height': 176, 'gender': 'male', 'hobbies': ['唱', '跳', '篮球', 'rap'], 666: 'good', ('1', '2', '3'): 'hello'}


# ---------------字典的增删改查---------------

# ----查询----
print(person['name'])           # 结果：牛轻松
print(person[666])              # 结果：good
print(person[('1', '2', '3')])  # 结果：hello
# print(person['啦啦啦啦'])      # 不存在的key，会报错

# 防止不存在的key报错，使用.get(keyname),不存在时不会报错，会默认返回None
print(person.get('啦啦啦啦'))                   # 结果：None
print(person.get('啦啦啦啦', '找不到对应的key'))  # 结果：找不到对应的key


# ----增删改-----
person222 = {'name': '你牛', 'age': 18}
# 1.增加数据
person222['gender'] = '男'
print('person222: ', person222)  
# 结果：person222:  {'name': '你牛', 'age': 18, 'gender': '男'}

# 2.修改数据
person222['gender'] = '女'
print('person222: ', person222)  
# 结果：person222:  {'name': '你牛', 'age': 18, 'gender': '女'}

# 3.删除
# pop 删除指定的一个key
person222.pop('name') 
print('person222: ', person222)  # 结果：person222:  {'age': 18, 'gender': '女'}

# popitem 随机删除一个key，并且以元组的形式返回删除的key/value键值对
xxx = person222.popitem()   
print('xxx: ', xxx)  # 结果：xxx:  ('gender', '女')

# 使用del关键词删除
del person222['age']
print('person222: ', person222)  # 结果：person222:  {}

# clear 清空
print(person222.clear())


# 4.合并两个字典update  (类似于列表合并使用的extend)
person333 = {'name': '牛牛'}
person444 = {'age': 18}
person333.update(person444)
print('person333: ', person333)  # 结果：person333:  {'name': '牛牛', 'age': 18}


# ---------------字典的遍历---------------
# 使用for in进行循环，获取到的是key
person555 = {'name': '牛牛', 'age': 18, 'gender': '男'}
# 常用方式
for temp in person555:
    print('x=%s' % temp)  # 依次打印三个key：name、age、gender
# 拿到所有的key
for temp in person555.keys():
    print('x=%s' % temp)  # 依次打印三个key：name、age、gender
# 拿到所有的value
for temp in person555.values():
    print('x=%s' % temp)  # 依次打印三个value：牛牛、18、男
    
# 拿到所有的键值对(键值对以元组形式表示)
for temp in person555.items():
    print('x={}'.format(temp))                         
    # 依次打印：('name', '牛牛')     ('age', 18)        ('gender', '男')
    print('key={},value={}'.format(temp[0], temp[1]))  
    # 依次打出：key=age,value=18    key=age,value=18   key=gender,value=男

# items取元组的另外一种写法
for (xxx, yyy) in person555.items():
    print('key={},value={}'.format(xxx, yyy))          # 依次打出：key=age,value=18    key=age,value=18   key=gender,value=男



# ------------------列表的推导式------------------
# 举例：将字典内的key和value兑换位置
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {}
for (m, n) in dict1.items():
    dict2[n] = m
print('dict2: ', dict2)  # 结果：dict2:  {1: 'a', 2: 'b', 3: 'c'}

# 字典的推导式表示
dict3 = {m: n for n, m in dict1.items()}
print('dict3: ', dict3)  # 结果：dict3:  {1: 'a', 2: 'b', 3: 'c'}
