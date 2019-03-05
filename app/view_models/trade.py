"""
    @File  : trade.py
    @Author: GaoZizhong
    @Date  : 2019/3/5 17:22
    @Desc  : 
"""

__author__ = "GaoZizhong"


class TradeInfo:
    def __init__(self, goods):
        self.total = 0
        self.trades = []
        self.__parse(goods)

    def __parse(self, goods):
        self.total = len(goods)
        self.trades = [self.__map_to_trade(single) for single in goods]
        pass

    def __map_to_trade(self, single):
        return dict(
            user_name=single.user.nickname,
            time=single.create_time.strftime('%Y-%m-%d'),
            id=single.id
        )
