
from io import StringIO
from io import BytesIO

str_io = StringIO()
str_io.write('牛')
str_io.write('青')
str_io.write('山')

print(str_io.getvalue())  # 牛青山


byte_io = BytesIO()
byte_io.write('小牛仔'.encode('utf8'))
print(byte_io.getvalue())                # b'\xe5\xb0\x8f\xe7\x89\x9b\xe4\xbb\x94'
print(byte_io.getvalue().decode('utf8')) # 小牛仔