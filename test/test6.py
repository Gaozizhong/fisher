"""
    @File  : test6.py
    @Author: GaoZizhong
    @Date  : 2019/3/1 15:44
    @Desc  : 
"""
import threading
import time

from werkzeug.local import LocalStack

__author__ = "GaoZizhong"

my_stack = LocalStack()
my_stack.push(1)
print("In main thread after push, value is:" + str(my_stack.top))


def worker():
    # 新线程
    print("In new thread before push, value is:" + str(my_stack.top))
    my_stack.push(2)
    print("In new thread after push, value is:" + str(my_stack.top))


new_t = threading.Thread(target=worker, name=__author__ + "_thread")
new_t.start()
time.sleep(1)
# 主线程
print("Finally, in main thread  value is:" + str(my_stack.top))

