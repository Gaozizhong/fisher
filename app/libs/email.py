"""
    @File  : email.py
    @Author: GaoZizhong
    @Date  : 2019/3/10 21:08
    @Desc  : 
"""
from threading import Thread

from flask import current_app, render_template
from flask_mail import Message

from app import mail

__author__ = "GaoZizhong"


def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            pass


def send_mail(to, subject, template, **kwargs):
    # Python email接口
    # msg = Message('测试邮件', sender='631923319@qq.com', body='test',
    #               recipients=['631923319@qq.com'])
    msg = Message('[鱼书]'+''+subject,
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[to])
    msg.html = render_template(template, **kwargs)
    app = current_app._get_current_object()
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
