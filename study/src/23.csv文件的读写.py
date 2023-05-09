import csv  # 系统内置工具

tempFile = open('src/23.test_csv.csv', 'w+')
write_tool = csv.writer(tempFile)

# 写入单行数据
write_tool.writerow(['name', 'age', 'city', 'scroe'])
write_tool.writerow(['张三', '18', '郑州', '99'])
write_tool.writerow(['李四', '22', '北京', '89'])
write_tool.writerow(['王五', '15', '上海', '95'])

# 写入多行数据
write_tool.writerows([
    ['牛牛', '18', '杭州', '92'],
    ['琳琳', '35', '苏州', '35'],
    ['荔枝', '25', '无锡', '65']
    ])




tempFile.seek(0, 0) # 光标手动重置到起始位置
read_tool = csv.reader(tempFile)
for rowData in read_tool:
    print(rowData)
''' 
['name', 'age', 'city', 'scroe']
['张三', '18', '郑州', '99']
['李四', '22', '北京', '89']
['王五', '15', '上海', '95']
['牛牛', '18', '杭州', '92']
['琳琳', '35', '苏州', '35']
['荔枝', '25', '无锡', '65']
'''




tempFile.close()