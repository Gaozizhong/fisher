"""
    @File  : test2.py
    @Author: GaoZizhong
    @Date  : 2019/3/1 10:25
    @Desc  : 
"""
import time

__author__ = "GaoZizhong"

import threading


def worker():
    print("I am thread")
    t = threading.current_thread()
    time.sleep(10)
    print(t.getName())


# 开启副线程
new_t = threading.Thread(target=worker, name=__author__ + "_thread")
new_t.start()
# worker()

# 主线程
t = threading.current_thread()
print(t.getName())

