import threading


# ----------------客户端---------------------

def singing():
    for i in range(50):
        print('正在唱歌')
    
def dancing():
    for i in range(50):
        print('正在跳舞')
    
# target需要的是一个函数，用来执行线程需要执行的任务
target1 = threading.Thread(target=singing)
target2 = threading.Thread(target=dancing)

# 启动线程
target1.start()
target2.start()



# ----------------服务端---------------------