"""
    @File  : book.py
    @Author: GaoZizhong
    @Date  : 2019/1/15
    @Desc  : 
"""
from flask import jsonify, request

from app.forms.book import SearchForm
from . import web


from helper import is_isbn_or_key
from yushu_book import YuShuBook

__author__ = "GaoZizhong"


@web.route("/book/search")
def search():
    """
    :param q: 普通关键字 ISBN
    :param page:普通关键字下
    ?q=金庸&page=1
    :return:
    """
    # # app.add_url_rule("url", view_func=, endpoint=)
    # q = request.args["q"]
    # # 至少有一个字符，长度限制
    # page = request.args["page"]
    # # 正整数，也要有一个最大值限制
    form = SearchForm(request.args)
    if form.validate():
        # a = request.args.to_dict() 把结果由不可变字典换成普通字典
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == "isbn":
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
        return jsonify(result)
    else:
        return jsonify(form.errors)

