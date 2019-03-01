"""
    @File  : test3.py
    @Author: GaoZizhong
    @Date  : 2019/3/1 14:50
    @Desc  : 
"""
from flask import Request

__author__ = "GaoZizhong"

import time
import threading

request = None

request1 = Request()
request2 = Request()
request3 = Request()

def worker():
    request = Request()
    print("I am thread")
    t = threading.current_thread()
    time.sleep(8)
    print(t.getName())


new_t = threading.Thread(target=worker, name=__author__ + "_thread")
new_t.start()
new_t = threading.Thread(target=worker, name=__author__ + "_thread")
new_t.start()
new_t = threading.Thread(target=worker, name=__author__ + "_thread")
new_t.start()
