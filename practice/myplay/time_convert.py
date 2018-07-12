
#  时间和时间戳之间的转换

import time
import datetime



# -----时间转时间戳------------------
dt = '2017-11-11 11:11:11'
time_array = time.strptime(dt, '%Y-%m-%d %H:%M:%S')
timestamp = time.mktime(time_array)
print(timestamp)


# ------时间戳转时间——————————————————————

timestamp = 1462451334
time_local = time.localtime(timestamp)
dt = time.strftime('%Y-%m-%d %H:%M:%S', time_local)

print(dt)


# -------计算时间间隔--------------------
t1 = datetime.datetime.strptime('2017-10-11 11:11:11', '%Y-%m-%d %H:%M:%S')
t2 = datetime.datetime.strptime('2017-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
now = datetime.datetime.now()
print((t1-t2).days)

# -------时间推移----------------

t5 = datetime.datetime.strptime('2017-10-11 11:11:11', '%Y-%m-%d %H:%M:%S')
# 计算前一天

print(t5 + datetime.timedelta(days=-1))  # 往前推一天
print(t5 + datetime.timedelta(hours=3))  # 往后推3小时
