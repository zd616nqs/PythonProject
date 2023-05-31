import threading
import time

# 多个线程可以同时操作一个全局变量
# 注意：多个进程不会共享1个全局变量
tickets = 100

# 创建一把同步锁
lock = threading.Lock()

# 举例 卖票  
def sellTicket():
    global tickets
    while True:
        lock.acquire() # 价同步锁
        if tickets > 0:
            time.sleep(0.2)
            tickets -= 1
            print("线程:{}  卖出一张票，还剩{}张票".format(threading.current_thread().name, tickets))
            lock.release() # 释放锁
        else:
            print("票卖完了")
            lock.release() # 释放锁
            break
        
target1 = threading.Thread(target=sellTicket, name="线程111")
target2 = threading.Thread(target=sellTicket, name="线程222")

target1.start()
target2.start()


