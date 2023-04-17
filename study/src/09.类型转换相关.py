import json

# 数组==》元组
nums = [1, 2, 3, 4]
listToTuple = tuple(nums)
print('tempTuple: ', listToTuple)  # 结果：tempTuple:  (1, 2, 3, 4)


# 数组==》集合
listToSet = set(nums)
print('tempSet: ', listToSet)  # 结果：tempSet:  {1, 2, 3, 4}

# 字典==》数组(只保留key)
dict1 = {'name': '牛牛', 'age': 18, 'gender': '男'}
dictToList = list(dict1)
print('dictToList: ', dictToList)  # 结果：dictToList:  ['name', 'age', 'gender']


# 内置函数eval:可以执行字符串内的代码
# eval('print(1+4)')
# eval('input("请输入您的用户名：")')



# 对象==》jsonstring
dict111 = {'name': '牛牛', 'age': 18, 'gender': '男'}
xx = json.dumps(dict111)  # 字典转换成jsonstring
print(type(xx)) # <class 'str'>
print('xx: ', xx)  # 结果：xx:  {"name": "\u725b\u725b", "age": 18, "gender": "\u7537"}


# jsonstring==》对象
jsonStr111 = '{"name": "\u725b\u725b", "age": 18, "gender": "\u7537"}'
# 方式1：使用eval
fff = eval(jsonStr111)
print(type(fff))  # <class 'dict'>
print('fff: ', fff)  # fff:  {'name': '牛牛', 'age': 18, 'gender': '男'}
# 方式2：使用json.loads()函数
eee = json.loads(jsonStr111)
print(type(eee))
print('eee: ', eee)
