"""
    @File  : wish.py
    @Author: GaoZizhong
    @Date  : 2019/3/2
    @Desc  :
"""

from . import web

__author__ = "GaoZizhong"


@web.route('/my/wish')
def my_wish():
    pass


@web.route('/wish/book/<isbn>')
def save_to_wish(isbn):
    pass


@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    pass
