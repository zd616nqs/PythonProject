import json
import pickle


# -----------json和pickle的区别-----------
# pickle用来将数据原封不动的转换成二进制，但是这个二进制数据只有python能识别
# json只能保存一部分信息，能够在不同的平台里通用。里面存的都是基本的数据类型




# --------------------json序列化----------------
tempFilePath1 = 'src/25.test_json1.txt'
tempFilePath2 = 'src/25.test_json2.txt'
file1 = open(tempFilePath1, 'w', encoding='utf8')
file2 = open(tempFilePath2, 'w', encoding='utf8')

# 1.1 json.dumps 将数据转换成json字符串，不会将数据保存到文件里
friends = ['jeason', 'lynn', 'lizhi']
jsonStr = json.dumps(friends)
print('jsonStr: ', jsonStr) # jsonStr:  ["jeason", "lynn", "lizhi"]
file1.write(jsonStr)

# 1.2 json.dump  将数据转换成json字符串，并且写入到指定的文件
mapData = {'name': 'niuniu', 'age': 18}
json.dump(mapData, file2)


file1.close()
file2.close()




# --------------------json反序列化----------------
# json.loads 将json字符串，并加载成为一个对象
# json.load  读取文件，并加载成一个对象

example_json_str = '{"name":"niuniu", "age":18}'
result1 = json.loads(example_json_str)
print('result1: ', result1)  # {'name': 'niuniu', 'age': 18}
print(result1['name'])       # niuniu


tempJsonFile = open(tempFilePath2, 'r', encoding='utf8')
fileLoadResult = json.load(tempJsonFile)
print('fileLoadResult: ', fileLoadResult) # fileLoadResult:  {'name': 'niuniu', 'age': 18}
print(fileLoadResult['name'])             # niuniu
tempJsonFile.close()






# --------------------pickle序列化和反序列化python对象--------------
# dumps：将python数据转化成二进制
# dump： 将python数据转换成二进制，并保存到指定的文件
# loads：将二进制数据加载成python数据
# load： 读取文件，并将文件内容加载成二进制


# jsonData = '{"name":"niuniu", "age":18}'
# pickle.loads(jsonData)
# pickle.load(tempFile)

# mapData = {'name': 'niuniu', 'age': 18}
# pickle.dumps(mapData)
# pickle.dump(mapData,tempFile2)


# 写入并读取一个class
class Dog:
    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color
        
dogFile = 'src/25.test_pickle.txt'
myDog = Dog('lizhi', 'yellow')
pickle.dump(myDog, open(dogFile, 'wb'))    # 二进制形式保存
readDog = pickle.load(open(dogFile, 'rb')) # 二进制形式读取
print(readDog.name, readDog.color) # lizhi yellow