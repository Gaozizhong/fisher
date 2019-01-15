"""
    @File  : fisher.py
    @Author: GaoZizhong
    @Date  : 2019/1/14
    @Desc  : 
"""
from flask import Flask

__author__ = "GaoZizhong"

app = Flask(__name__)

print("启动文件初始化的APP的id为："+str(id(app)))
app.config.from_object("config")

from app.web import book

if __name__ == "__main__":
    print("启动的APP的id为："+str(id(app)))
    app.run(host="0.0.0.0", debug=app.config["DEBUG"], port=81)
