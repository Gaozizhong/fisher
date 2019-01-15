"""
    @File  : book.py
    @Author: GaoZizhong
    @Date  : 2019/1/15
    @Desc  : 
"""
from flask import jsonify

from helper import is_isbn_or_key
from yushu_book import YuShuBook
from fisher import app

__author__ = "GaoZizhong"


@app.route("/book/search/<q>/<page>")
def search(q, page):
    """
    :param q: 普通关键字 ISBN
    :param page:普通关键字下
    :return:
    """
    # app.add_url_rule("url", view_func=, endpoint=)
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key:
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)