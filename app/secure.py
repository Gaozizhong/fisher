"""
    @File  : config.py
    @Author: GaoZizhong
    @Date  : 2019/1/14
    @Desc  : 
"""

__author__ = "GaoZizhong"

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:Mylove0416++@188.131.235.158:3306/fisher'
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = b'W"\xc5-\xd5D\xb2?\xb4<}U\xd0\x94\xcf1H\xf1_>\xc5\xfb\x0f\xd7'

# Email配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = '631923319@qq.com'
MAIL_PASSWORD = 'dqaujurgsmstbbdh'

