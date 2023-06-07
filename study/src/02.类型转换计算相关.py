
# --------------------进制相关-----------------
# 不同进制表示
aa = 673         # 十进制
ab = 0b00101010  # 二进制 0b开头
ac = 0o34        # 八进制 0o开头
ad = 0xffffff    # 十六进制 0x开头
print(aa, ab, ac, ad)  # 673 42 28 16777215

# 进制转换
ba = 12
print(bin(ba))  # 十进制转二进制
print(oct(ba))  # 十进制转八进制
print(hex(ba))  # 十进制转十六进制


# -------------------数据类型相关-------------------
# ------string转int------
age = "18"
new_age = int(age)
print(new_age+2) # 结果：20

# ------string转int 16进制转10进制------
cc = "1a2c"
cd = int(cc, 16) # 把字符串1a2c当做十六进制转换成整数
print(cd)  # 结果：2700

# ------string转int 8进制转10进制------
cn = "12"
cm = int(cn, 8) # 把字符串12当做八进制转换成整数
print(cm)  # 结果：10


# ------string转float------
da = "13.14"
db = float(da)
dc = 108
dd = float(dc)
print(db, dc)  # 结果：13.14  108

# ------int转string------
ee = 66
ef = str(ee)
print(ef, type(ef)) # 66 <class 'str'>

# ------int转bool------
print(bool(100))  # True
print(bool(-5))   # True
print(bool(0))    # False

# ------string转bool------
# 只有空字符串和None转换为bool才会为False
print(bool("hello"))      # True
print(bool("False"))      # True
print(bool(""), bool('')) # False False
print(bool(None))         # False
# 判断是否为None必须使用is None或 is not None，不能使用 == None或 != None

# ------bool转其他类型------
print("---------")
print(str(True) == "True")   # True
print(str(False) == "False") # True
print(int(True))    # 1
print(int(False))   # 0
print(float(True))  # 1.0
print(float(False)) # 0.0
print(10 + True)    # 11
print(10 + False)   # 10
print(10 * True)    # 10
print(10 * False)   # 0