a = "牛青山"
print(a)

b = 673
print(b)

c = True
print(c)

# ---------变量的类型--------
# 数字类型： int整数类型  float类型 long类型 complex复数类型(print((-1)**0.5)  负一的0.5次方)
# 布尔类型 True Flase
# String类型  (一对单引号或者双引号)
# List类型  names = ["牛","青","山"]
# Dictionary字典类型  person = {"name":"牛轻松","addr":"龙柏易居"}
# Tuple 元组类型  nums = (1,3,4,2,7)
# 集合类型  xxx = {9,"hello","niu",35}


# 打印变量的类型
print(type("牛青山"))
print(type(34))
print(type(True))

# 打印的特殊用法
# print(value, ..., sep=" ", end="\n", file=sys.stdout, flush=False)
# sep 参数表示输出时，每个值之间要使用哪个字符作为分隔符。默认使用空格作为分隔符
# end 表示当执行完print语句后，记下来要输出的字符。默认\n表示换行
print("牛", "青", "山", sep="+", end="------")
print("123456")
# 牛+青+山------123456


# input 输入函数(注意：保存的结果都是字符串类型)
password = input("请输入您的银行卡密码：")
print("已输入密码：" + password)



# 声明类型 单个或多个类型（挡不住强行赋值，就有个提示的作用）

nqs: str = "lkjkl"

para: str | int | float
para = "sdkjlk"
para = 33
para = 5.5
para = [33, 22]  # 没卵用，还是会赋值成功
print(para)