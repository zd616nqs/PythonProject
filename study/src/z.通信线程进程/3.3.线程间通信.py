import threading
import queue
import time

# Queue是一个先进先出FIFO的队列，主进程中创建Queue对象，并作为参数传入子进程，两者之间通过put()放入数据，通过get()取出数据，执行了get()函数之后队列中的数据会被同时删除，可以使用multiprocessing模块的Queue实现多进程之间的数据传递

# ---------------多线程的数据传递:使用queue.Queue()---------------
def producer(queue):
    for i in range(100):
        print("+++{}  生产了1个面包，编号{}".format(threading.currentThread().name, i))
        queue.put("香甜{}号".format(i))
        time.sleep(0.1)
    return

def consumer(queue):
    for i in range(100):
        print("---{}  购买了1个面包，编号:{}".format(threading.currentThread().name, queue.get()))
        time.sleep(0.3)
    return
    



q = queue.Queue()
        
target1 = threading.Thread(target=producer, args=(q,), name="工厂")
target2 = threading.Thread(target=consumer, args=(q,), name="面包店11")
target3 = threading.Thread(target=consumer, args=(q,), name="面包店22")

target1.start()
target2.start()
target3.start()