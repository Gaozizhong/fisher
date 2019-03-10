"""
    @File  : wish.py
    @Author: GaoZizhong
    @Date  : 2019/3/2
    @Desc  :
"""
from flask import current_app, flash, redirect, url_for
from flask_login import login_required, current_user

from app.models.base import db
from app.models.wish import Wish
from . import web

__author__ = "GaoZizhong"


@web.route('/my/wish')
def my_wish():
    pass


@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            wish = Wish()
            wish.isbn = isbn
            wish.uid = current_user.id
            db.session.add(wish)
    else:
        flash('这本书已添加至你的赠送清单或已存在与你的心愿清单，请不要重复添加。')
    return redirect(url_for('web.book_detail', isbn=isbn))
    pass


@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    pass