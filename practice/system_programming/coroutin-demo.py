# yield实现协程

# def consumer(name):
#     print("要开始啃骨头了...")
#     while True:
#         print("\033[31;1m[consumer] %s\033[0m " % name)
#         bone = yield
#         print("[%s] 正在啃骨头 %s" % (name, bone))
#
#
# def producer(obj1, obj2):
#     obj1.send(None)    # 启动obj1这个生成器,第一次必须用None  <==> obj1.__next__()
#     obj2.send(None)    # 启动obj2这个生成器,第一次必须用None  <==> obj2.__next__()
#     n = 0
#     while n < 5:
#         n += 1
#         print("\033[32;1m[producer]\033[0m 正在生产骨头 %s" % n)
#         obj1.send(n)
#         obj2.send(n)
#
#
# if __name__ == '__main__':
#     con1 = consumer("消费者A")
#     con2 = consumer("消费者B")
#     producer(con1, con2)


# greenlet实现协程

# from greenlet import greenlet
# greenlet 其实就是手动切换；gevent是对greenlet的封装，可以实现自动切换


# def test1():


# gevent实现协程

# import gevent, timeit
#
#
# def func1():
#     start = timeit.default_timer()
#     print('func1 running')
#     gevent.sleep(3)
#     end = timeit.default_timer()
#     print('switch func1,', 'runtime:{}'.format(end-start))
#
#
# def func2():
#     start = timeit.default_timer()
#     print('func2 running')
#     gevent.sleep(2)
#     end = timeit.default_timer()
#     print('switch func2,', 'runtime:{}'.format(end-start))
#
#
# def func3():
#     start = timeit.default_timer()
#     print('func3 running')
#     gevent.sleep(0)
#     end = timeit.default_timer()
#     print('switch func3,', 'runtime:{}'.format(end-start))
#
#
# gevent.joinall([
#     gevent.spawn(func1),
#     gevent.spawn(func2),
#     gevent.spawn(func3),
# ])


# 同步和异步的区别


# import gevent
#
#
# def task(pid):
#     gevent.sleep(0.5)
#     print('Task {} done'.format(pid))
#
#
# def synchronous():
#     for i in range(1, 10):
#         task(i)
#
#
# def asynchronous():
#     threads = [gevent.spawn(task, i) for i in range(10)]
#     gevent.joinall(threads)
#
#
# print('Synchronous:')
# synchronous()
#
# print('Asynchronous:')
# asynchronous()


# 遇到阻塞时会切换任务之【爬虫版】


import requests
import gevent, timeit
from gevent import monkey


monkey.patch_all()  # 把当前程序中的所有io操作都做上标记


def spider(url):
    print('GET:%s' % url)
    resp = requests.get(url)
    data = resp.text
    print('-----------------------------------')
    # print(data)
    print("%s bytes received from %s.." % (len(data), url))


urls = [
    "https://www.python.org/",
    "https://www.yahoo.com/",
    "https://github.com/",
    "https://stackoverflow.com/"
]

start_time = timeit.default_timer()

for url in urls:
    spider(url)

print('同步耗时：{}'.format(timeit.default_timer() - start_time))


async_time_start = timeit.default_timer()

gevent.joinall([gevent.spawn(spider, url) for url in urls])

print('异步耗时：{}'.format(timeit.default_timer() - async_time_start))