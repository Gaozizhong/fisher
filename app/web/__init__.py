"""
    @File  : __init__.py
    @Author: GaoZizhong
    @Date  : 2019/1/15
    @Desc  : 
"""
from flask import Blueprint

__author__ = "GaoZizhong"

web = Blueprint("web", __name__)

from app.web import book
from app.web import user
