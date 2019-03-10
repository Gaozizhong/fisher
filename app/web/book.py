"""
    @File  : book.py
    @Author: GaoZizhong
    @Date  : 2019/1/15
    @Desc  : 
"""

from flask import request, render_template, flash
from flask_login import current_user

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookCollection, BookViewModel
from app.view_models.trade import TradeInfo
from . import web

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
    """
            1. 当书籍既不在心愿清单也不在礼物清单时，显示礼物清单
            2. 当书籍在心愿清单时，显示礼物清单
            3. 当书籍在礼物清单时，显示心愿清单
            4. 一本书要防止即在礼物清单，又在赠送清单，这种情况是不符合逻辑的

            这个视图函数不可以直接用cache缓存，因为不同的用户看到的视图不一样
            优化是一个逐步迭代的过程，建议在优化的初期，只缓存那些和用户无关的“公共数据"
        """
    has_in_gifts = False
    has_in_wishes = False
    # 获取书籍的相关数据
    book = YuShuBook()
    book.search_by_isbn(isbn)

    if current_user.is_authenticated:
        # 如果未登录，current_user将是一个匿名用户对象
        if Gift.query.filter_by(uid=current_user.id,
                                isbn=isbn, launched=False).first():
            has_in_gifts = True
        if Wish.query.filter_by(uid=current_user.id,
                                isbn=isbn, launched=False).first():
            has_in_wishes = True
    book = BookViewModel(book.first)

    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes_model = TradeInfo(trade_wishes)
    trade_gifts_model = TradeInfo(trade_gifts)

    return render_template('book_detail.html', book=book,
                           wishes=trade_wishes_model,
                           gifts=trade_gifts_model,
                           has_in_gifts=has_in_gifts,
                           has_in_wishes=has_in_wishes)

