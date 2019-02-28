"""
    @File  : test.py
    @Author: GaoZizhong
    @Date  : 2019/2/28
    @Desc  :
"""

__author__ = "GaoZizhong"

from flask import Flask, current_app, request, Request

app = Flask(__name__)

# ctx = app.app_context()
# ctx.push()
#
# ctx.pop()


with app.app_context():
    a = current_app
    d = current_app.config['DEBUG']
