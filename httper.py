"""
    @File  : httper.py
    @Author: GaoZizhong
    @Date  : 2019/1/15
    @Desc  : 
"""

__author__ = "GaoZizhong"


# urllib
# from urllib import request
# requests 推荐使用
import requests


class HTTP:
    @staticmethod
    def get(url, return_json=True):
        """

        :param url:
        :param return_json:
        :return:json或者文本信息
        """
        r = requests.get(url)
        # restful
        # json
        if r.status_code != 200:
            return {} if return_json else ""
        return r.json() if return_json else r.text
