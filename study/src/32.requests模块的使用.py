# requests模块是第三方模块，可以用来发送网络连接
# pipenv install requests

import requests


response = requests.get('https://www.baidu.com') # 返回值是一个response对象
print(response)  # <Response [200]>

# content
print(response.content.decode('utf8')) 

# text
print(response.text)