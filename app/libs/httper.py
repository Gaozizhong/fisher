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
        :param url:请求地址
        :param return_json:返会的JSON文本
        :return:json或者文本信息
        """
        r = requests.get(url)
        # restful返回格式为json
        if r.status_code != 200:
            return {} if return_json else ""
        return r.json() if return_json else r.text
