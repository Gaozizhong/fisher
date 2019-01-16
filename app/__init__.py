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
    app.config.from_object("app.secure")
    app.config.from_object("app.setting")
    register_blueprint(app)
    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
