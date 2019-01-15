"""
    @File  : fisher.py
    @Author: GaoZizhong
    @Date  : 2019/1/14
    @Desc  : 
"""
from flask import Flask
from helper import is_isbn_or_key

__author__ = "GaoZizhong"

app = Flask(__name__)
app.config.from_object("config")


@app.route("/book/search/<q>")
def search(q):
    """
    :param q: 普通关键字 ISBN
    :param page:
    :return:
    """
    isbn_or_key = is_isbn_or_key(q)
    return isbn_or_key


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=app.config["DEBUG"], port=81)
