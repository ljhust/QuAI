import backtrader as bt
import backtrader.indicators as btind
import os,  sys
import datetime


cerebro = bt.Cerebro(stdstats=False)

modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
datapath = os.path.join(modpath, '../../datas/orcl-1995-2014.txt')

data = bt.feeds.YahooFinanceCSVData(
    dataname=datapath,
    # Do not pass values before this date
    fromdate=datetime.datetime(2000, 1, 1),
    # Do not pass values after this date
    todate=datetime.datetime(2000, 12, 31),
    reverse=False,
    timeframe=bt.TimeFrame.Days
)

cerebro.adddata(data)

cerebro.resampledata(data, timeframe=bt.TimeFrame.Weeks)
cerebro.replaydata(data, timeframe=bt.TimeFrame.Minutes)

print(cerebro.datas)