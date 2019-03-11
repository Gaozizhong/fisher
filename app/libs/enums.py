"""
    @File  : enums.py
    @Author: GaoZizhong
    @Date  : 2019/3/11 0:38
    @Desc  : 
"""
from enum import Enum

__author__ = "GaoZizhong"


class PendingStatus(Enum):
    """4种交易状态"""
    Waiting = 1
    Success = 2
    Reject = 3
    Redraw = 4
