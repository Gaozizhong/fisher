"""
    @File  : __init__.py
    @Author: GaoZizhong
    @Date  : 2019/1/15
    @Desc  : 
"""
from flask import Flask

__author__ = "GaoZizhong"


def creat_app():
    app = Flask(__name__)
    app.config.from_object("config")
    return app
