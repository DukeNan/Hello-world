import requests
import time

start_time = time.time()
li = [i for i in range(5)]

n = 3

li1 = [li[i:i+n] for i in range(0, len(li), n)]
end_time = time.time()
print(li1)
print(end_time-start_time)
    