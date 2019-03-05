"""
    @File  : base.py
    @Author: GaoZizhong
    @Date  : 2019/3/3 11:19
    @Desc  : 
"""
from contextlib import contextmanager
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from sqlalchemy import SmallInteger, Column, Integer

__author__ = "GaoZizhong"


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
    pass


db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    creat_time = Column('creat_time',Integer)
    status = Column(SmallInteger, default=1)

    def __init__(self):
        self.creat_time = int(datetime.now().timestamp())

    def set_attrs(self, attrs_dict):
        for key,value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)
