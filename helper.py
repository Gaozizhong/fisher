"""
    @File  : helper.py
    @Author: GaoZizhong
    @Date  : 2019/1/15
    @Desc  : 
"""

__author__ = "GaoZizhong"


def is_isbn_or_key(word):
    """
    以下代码是用来判断q是ISBN还是关键字
    isbn13 13个0-9的数组组成
    isbn10 含有一些“—”
    :param word: isbn or 关键字
    :return:isbn_or_key
    """
    isbn_or_key = "key"
    if len(word) == 13 and word.isdigit():
        isbn_or_key = "isbn"
    short_word = word.replace("-", "")
    if "-" in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = "isbn"
    return isbn_or_key
