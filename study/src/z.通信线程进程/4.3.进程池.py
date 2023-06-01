import time
import os
from multiprocessing import Pool
import random


def worker(msg):
    t_start = time.time()
    print('任务序列:%s，开始执行任务，pid=%d' % (msg, os.getpid()))
    time.sleep(random.random()*2)
    t_stop = time.time()
    print('任务序列:%s，执行完毕，耗时%0.2f' % (msg, t_stop-t_start))
    

if __name__ == "__main__":
    po = Pool(3) # 定义一个进程池，最大进程数位3
    for i in range(0, 10):
        # Pool().apply_async(要调用的目标，(传递个目标的参数元组,))
        # 每次循环都会用空闲出来的子进程去调用目标
        # 每次循环都会用空闲出来的子进程去调用目标是的发生的
        po.apply_async(worker, (i,))
        
    print('-----start------')
    po.close() # 关闭进程池，关闭后po不再接受新的请求
    po.join()  # 等待po中所有子进程执行完成，必须放在close之后
    print('-----end------')
    
'''  
-----start------
任务序列:0，开始执行任务，pid=68773
任务序列:1，开始执行任务，pid=68772
任务序列:2，开始执行任务，pid=68774
任务序列:1，执行完毕，耗时0.04
任务序列:3，开始执行任务，pid=68772
任务序列:2，执行完毕，耗时0.53
任务序列:4，开始执行任务，pid=68774
任务序列:4，执行完毕，耗时0.39
任务序列:5，开始执行任务，pid=68774
任务序列:0，执行完毕，耗时1.07
任务序列:6，开始执行任务，pid=68773
任务序列:6，执行完毕，耗时0.77
任务序列:7，开始执行任务，pid=68773
任务序列:3，执行完毕，耗时1.81
任务序列:8，开始执行任务，pid=68772
任务序列:8，执行完毕，耗时0.08
任务序列:9，开始执行任务，pid=68772
任务序列:5，执行完毕，耗时1.45
任务序列:7，执行完毕，耗时1.01
任务序列:9，执行完毕，耗时1.85
-----end------
'''
