"""
    @File  : book.py
    @Author: GaoZizhong
    @Date  : 2019/1/15
    @Desc  : 
"""

from flask import jsonify, request, render_template, flash

from app.forms.book import SearchForm
from app.models.gift import Gift
from app.models.wish import Wish
from app.spider import yushu_book
from app.view_models.book import BookCollection, BookViewModel
from . import web


from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook

__author__ = "GaoZizhong"


# @web.route("/test")
# def test1():
#     from flask import request
#     from app.libs.none_local import n
#     print(n.v)
#     n.v = 2
#     print("----------------------")
#     print(getattr(request, "v", None))
#     setattr(request, "v", 2)
#     print("----------------------")
#     return ""

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
    books = BookCollection()

    if form.validate():
        # a = request.args.to_dict() 把结果由不可变字典换成普通字典
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == "isbn":
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)
        books.fill(yushu_book, q)
    else:
        flash("搜索的关键字不符合要求，请重新输入关键字")
    return render_template('search_result.html', books=books, form=form)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    has_in_gifts = False
    has_in_wishes = False
    # 取书籍的相关数据
    book = YuShuBook()
    book.search_by_isbn(isbn)
    book = BookViewModel(book.first)

    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

    return render_template('book_detail.html', book=book, wishes=[], gifts=[])

