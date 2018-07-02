# import time, threading
#
# # 新线程执行的代码:
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)
#
# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)


# cup密集型多线程分析

import threading, time
from multiprocessing import Process


def counter():
    i = 0
    for _ in range(50000000):
        i = i + 1
    return True


def main():
    l = []
    start_time = time.time()
    for i in range(2):
        t = threading.Thread(target=counter)
        t.start()
        l.append(t)
        t.join()

    end_time = time.time()
    print("多线程并行运行时间: {}".format(end_time - start_time))


def fun():
    start_time = time.time()
    i = 0
    for _ in range(500000000):
        i = i + 1
    end_time = time.time()
    print("串行运行时间: {}".format(end_time - start_time))
    return True


def fun1():
    li = []
    start_time = time.time()
    for _ in range(2):
        t = Process(target=counter)
        t.start()
        li.append(t)

    for t in li:
        t.join()

    end_time = time.time()
    print("多进程并发运行时间: {}".format(end_time - start_time))



if __name__ == '__main__':
    main()
    fun()
    fun1()

