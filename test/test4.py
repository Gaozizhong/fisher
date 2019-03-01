"""
    @File  : test4.py
    @Author: GaoZizhong
    @Date  : 2019/3/1 15:00
    @Desc  : 
"""
import threading
import time

from werkzeug.local import Local

__author__ = "GaoZizhong"


class A:
    b = 1


my_obj = Local()
my_obj.b = 1

def worker():
    # 新线程
    my_obj.b = 2
    print("In new thread b is" + str(my_obj.b))


new_t = threading.Thread(target=worker, name=__author__ + "_thread")
new_t.start()
time.sleep(1)
# 主线程
print("In main thread b is" + str(my_obj.b))
