"""
    @File  : fisher.py
    @Author: GaoZizhong
    @Date  : 2019/1/14
    @Desc  : 
"""
from flask import Flask, jsonify
from helper import is_isbn_or_key
from yushu_book import YuShuBook

__author__ = "GaoZizhong"

app = Flask(__name__)
app.config.from_object("config")


@app.route("/book/search/<q>/<page>")
def search(q, page):
    """
    :param q: 普通关键字 ISBN
    :param page:普通关键字下
    :return:
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key:
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=app.config["DEBUG"], port=81)
