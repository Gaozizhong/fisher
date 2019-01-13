"""
    @File  : fisher.py
    @Author: GaoZizhong
    @Date  : 2019/1/14
    @Desc  : 
"""
from flask import Flask

__author__ = "GaoZizhong"

app = Flask(__name__)
app.config.from_object("config")


@app.route("/hello")
def hello():
    return "hello gaozizhong"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=app.config["DEBUG"], port=81)
