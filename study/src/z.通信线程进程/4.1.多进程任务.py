import time
import multiprocessing
import os


def dance(count):
    for i in range(count):
        print('pid:{}  正在跳舞'.format(os.getpid()))
        time.sleep(0.2)
    return

def sing(count):
    for i in range(count):
        print('pid:{}  正在唱歌'.format(os.getpid()))
        time.sleep(0.3)
    return
    


if __name__ == "__main__":
    print("主进程pid={}".format(os.getpid()))
    process1 = multiprocessing.Process(target=dance, args=(30,))
    process2 = multiprocessing.Process(target=sing, args=(50,))

    process1.start()
    process2.start()