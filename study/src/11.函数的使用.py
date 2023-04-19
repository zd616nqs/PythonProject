# -------------递归调用------------
print('-----递归调用--------')
count = 0
def tell_story():
    global count
    count += 1
    print('从前有个山，山里有个庙，庙里有个老和尚', count)
    if count < 5:
        tell_story()
tell_story()
# 从前有个山，山里有个庙，庙里有个老和尚 1
# 从前有个山，山里有个庙，庙里有个老和尚 2
# 从前有个山，山里有个庙，庙里有个老和尚 3
# 从前有个山，山里有个庙，庙里有个老和尚 4
# 从前有个山，山里有个庙，庙里有个老和尚 5

# 练习：斐波那契数列
targetMaxIndex = 10
currentNum = 0
print('斐波那契数列：', end='')
def fibonacci_func(index, lastNum):
    global targetMaxIndex
    global currentNum
    if index == 0:
        currentNum = 1
        print(currentNum, end=' ')
        fibonacci_func(1, currentNum)
    elif index == targetMaxIndex:
        currentNum = currentNum + lastNum
        print(currentNum, end=' ')
        print('结束')
    else:
        temp = currentNum
        currentNum = lastNum + currentNum
        lastNum = temp
        
        print(currentNum, end=' ')
        fibonacci_func(index + 1, lastNum)
fibonacci_func(0, currentNum)

print('\n')



# -------------匿名函数------------
print('-----匿名函数--------')
# 使用lambda关键词能创建小型匿名函数，省略了def声明函数的标准步骤
# 标准格式： funcName = lambda 参数列表: 运算表达式
# sum = lambda arg1, arg2: arg1 + arg2
# print('计算和：{}'.format(sum(arg1=1, arg2=2)))  # 结果：3

# 注意：lambda函数不推荐赋值给一个变量，这样跟def的作用一样了，而且还容易混淆
# 推荐的lambda使用场景，比如作为函数的实参时使用，例如下列：
# exampleFunc(playerNames, key=lambda player: player.lastYearRank+player.thisYearRank) 



print('\n')