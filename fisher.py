"""
    @File  : fisher.py
    @Author: GaoZizhong
    @Date  : 2019/1/14
    @Desc  : 
"""
from app import creat_app

__author__ = "GaoZizhong"

app = creat_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=app.config["DEBUG"], port=81)
