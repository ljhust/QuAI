from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import backtrader as bt
import os
import sys
import datetime
from DayCSVData import DayCSVData


class TestStrategy(bt.Strategy):

    params = (
        ('maperiod', 15),
        ('printlog', False)
    )

    def log(self, txt, dt=None, doprint=False):
        ''' Logging function for this strategy'''
        if self.params.printlog or doprint:
            dt = dt or self.datas[0].datetime.date(0)
            print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close
        self.datahigh = self.datas[0].high
        self.datahighdelay = self.datas[0].high(-1)

        self.preclose = self.datas[0].close(-1)
        self.order = None
        self.buyprice = None
        self.buycomm = None

        # self.sma = bt.indicators.MovingAverageSimple(self.datas[0], period=self.params.maperiod)
        self.upmove = self.datahigh - self.datahigh(-1)

        # bt.indicators.ExponentialMovingAverage(self.datas[0], period=25)
        # bt.indicators.WeightedMovingAverage(self.datas[0], period=25, subplot=True)
        # bt.indicators.Stochastic(self.datas[0])
        # rsi = bt.indicators.RSI(self.datas[0])
        # bt.indicators.SmoothedMovingAverage(rsi, period=15)
        # bt.indicators.ATR(self.datas[0], plot=False)

        # sma0 = bt.indicators.SMA(self.data0, period=15)

    # def notify_order(self, order):
    #     if order.status in [order.Submitted, order.Accepted]:
    #         return
    #
    #     if order.status in [order.Completed]:
    #         if order.isbuy():
    #             self.log('BUY EXECUTED, price: %.2f, cost: %.2f, comm: %.2f' %
    #                      (order.executed.price,
    #                       order.executed.value,
    #                       order.executed.comm))
    #
    #             self.buyprice = order.executed.price
    #             self.buycomm = order.executed.comm
    #
    #         elif order.issell():
    #             self.log('BUY EXECUTED, price: %.2f, cost: %.2f, comm: %.2f' %
    #                      (order.executed.price,
    #                       order.executed.value,
    #                       order.executed.comm))
    #
    #         self.bar_executed = len(self)
    #
    #     elif order.status in [order.Canceled, order.Margin, order.Rejected]:
    #         self.log("Order Canceled/Margin/Rejected")
    #
    #     self.order = None
    #
    # def notify_trade(self, trade):
    #     if not trade.isclosed:
    #         return
    #
    #     self.log('OPERATION PROFIT, gross %.2f, net %.2f' %
    #              (trade.pnl, trade.pnlcomm))

    def next(self):
        # Simply log the closing price of the series from the reference
        # self.log('Close, %.2f' % self.dataclose[0], doprint=True)
        self.log('close, %.2f' % self.dataclose[0], doprint=True)
        self.log('preclose, %.2f' % self.preclose[0], doprint=True)
        r_t = self.dataclose[0]-self.preclose[0]
        r_t = r_t/self.dataclose[0]
        self.log('rt, %.8f' % r_t, doprint=True)


        # if self.order:
        #     return
        #
        # if not self.position:
        #     if self.dataclose[0] > self.sma[0]:
        #         self.log('BUY created, %.2f' % self.dataclose[0])
        #         self.order = self.buy()
        #
        # else:
        #     if self.dataclose[0] < self.sma[0]:
        #         self.log('SELL created, %.2f' % self.dataclose[0])
        #         self.order = self.sell()

    # def stop(self):
    #     self.log('(MA Period %2d) Ending Value %.2f' %
    #              (self.params.maperiod, self.broker.getvalue()), doprint=True)


if __name__ == '__main__':
    cerebro = bt.Cerebro(stdstats=False, optdatas=True)

    modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
    datapath = os.path.join(modpath, '../../datas/orcl-1995-2014.txt')


    data = bt.feeds.YahooFinanceCSVData(
        dataname=datapath,
        # Do not pass values before this date
        fromdate=datetime.datetime(2000, 1, 1),
        # Do not pass values after this date
        todate=datetime.datetime(2000, 12, 31),
        reverse=False)

    data1 = DayCSVData(
        # dataname="D:/data/day_data/whole_data.csv",
        dataname="D:/data/day_data/sh600000_qfq.csv",
        fromdate=datetime.datetime(2011, 1, 1),
        todate=datetime.datetime(2011, 12, 31),
    )

    # cerebro.adddata(data)
    cerebro.adddata(data1)

    cerebro.addsizer(bt.sizers.FixedSize, stake=10)

    cerebro.broker.set_cash(1000.0)

    cerebro.broker.setcommission(commission=0.0)

    cerebro.addstrategy(TestStrategy)
    # cerebro.optstrategy(
    #     TestStrategy,
    #     maperiod=range(10, 31)
    # )

    # print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
    from time import time
    st_time = time()
    cerebro.run()
    end_time = time()
    elapse = end_time - st_time
    print('whole time elapse: %f' % elapse)

    # print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

    # cerebro.plot()