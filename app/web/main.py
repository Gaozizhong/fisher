"""
    @File  : main.py
    @Author: GaoZizhong
    @Date  : 2019/3/2
    @Desc  :
"""

from . import web

__author__ = "GaoZizhong"


@web.route('/')
def index():
    return "Index"


@web.route('/personal')
def personal_center():
    pass
