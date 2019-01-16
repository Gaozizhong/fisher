"""
    @File  : yushu_book.py
    @Author: GaoZizhong
    @Date  : 2019/1/15
    @Desc  : 
"""
from app.libs.httper import HTTP
from flask import current_app

__author__ = "GaoZizhong"


class YuShuBook:
    isbn_url = "http://t.yushu.im/v2/book/isbn/{}"
    keyword_url = "http://t.yushu.im/v2/book/search?q={}&count={}&start={}"

    @classmethod
    def search_by_isbn(cls, isbn):
        url = YuShuBook.isbn_url.format(isbn)
        # dict
        result = HTTP.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword, page=1):

        url = YuShuBook.keyword_url.format(keyword, current_app.config["PER_PAGE"], cls.calculate_start(page))
        # dict
        result = HTTP.get(url)
        return result

    @staticmethod
    def calculate_start(page):
        return (page - 1) * current_app.config["PER_PAGE"]
