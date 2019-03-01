"""
    @File  : test5.py
    @Author: GaoZizhong
    @Date  : 2019/3/1 15:30
    @Desc  : 
"""
from werkzeug.local import LocalStack

__author__ = "GaoZizhong"

s = LocalStack()
s.push(1)
print(s.top)
print(s.top)
print(s.pop())
print(s.top)

s.push(1)
s.push(2)
print(s.top)
print(s.top)
print(s.pop())
print(s.top)
