"""
    @File  : yushu_book.py
    @Author: GaoZizhong
    @Date  : 2019/1/15
    @Desc  : 
"""
from httper import HTTP

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
    def search_by_keyword(cls, keyword,count=15, start=0):
        url = YuShuBook.keyword_url.format(keyword, count, start)
        # dict
        result = HTTP.get(url)
        return result
