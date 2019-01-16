"""
    @File  : book.py
    @Author: GaoZizhong
    @Date  : 2019/1/16
    @Desc  : 
"""
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired

__author__ = "GaoZizhong"


class SearchForm(Form):
    q = StringField(validators=[DataRequired(), Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
