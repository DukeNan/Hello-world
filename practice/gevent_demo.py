# import gevent
# from gevent import socket
#
# urls = ['www.baudu.com', 'www.sina.com', 'www.qq.com']
#
# jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]
#
# gevent.joinall(jobs, timeout=2)
#
# li = [job.value for job in jobs]
#
# print(li)

from __future__ import print_function
import gevent
from gevent import monkey

monkey.patch_all()

import requests

urls = [
    'https://www.baidu.com/',
    'https://www.sina.com/',
    'http://www.qq.com/'
]

def print_head(url):
    print('String %s' % url)
    data = requests.get(url).text
    print('%s: %s bytes: %r' % (url, len(data), data[:50]))

jobs = [gevent.spawn(print_head, _url) for _url in urls]

gevent.wait(jobs)

