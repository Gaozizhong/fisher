"""
    @File  : gift.py
    @Author: GaoZizhong
    @Date  : 2019/3/3 11:18
    @Desc  : 
"""
from flask import current_app
from sqlalchemy import Column, Integer, Boolean, ForeignKey, String, desc
from sqlalchemy.orm import relationship

from app.models.base import Base
from app.spider.yushu_book import YuShuBook

__author__ = "GaoZizhong"


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('book.id'))
    launched = Column(Boolean, default=False)

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    @classmethod
    def recent(cls):
        recent_gift = Gift.query.filter_by(
            launched=False).group_by(
            Gift.isbn).order_by(
            desc(Gift.creat_time)).limit(
            current_app.config['RECENT_BOOK_COUNT']).distinct().all()
        return recent_gift
