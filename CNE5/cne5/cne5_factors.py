import pandas as pd
import numpy as np
from datetime import datetime
import dask.dataframe as dd
import dask.array as da


def halflife(half_life=63, length=252):
    t = np.arange(length)
    w = 2 ** (t/half_life) / sum(2 ** (t/half_life))
    return w


def pct_chg(ser):
    return ser.map_partitions(pd.diff)/ser.map_partitions(pd.shift)


def halflife_da(half_life=63, length=252):
    t = da.arange(length)
    w = 2 ** (t/half_life) / sum(2 ** (t/half_life))
    return w


class CNE5:
    """
    此类实现CNE5的所有的因子的实现，因子定义如下：
    "size"
        = 1.0*lncap
            - lncap: Natural log of market cap
    "Beta"
        = 1.0*beta
            beta的计算就稍微有点麻烦了，这里是用过去252天的数据去做加权最小二乘的回归，权重是半衰期=63的半衰期加权，半衰期加权在barra的文档中经常会用到，在这里再多说一句半衰期加权的算法
    "Monmentum"
        = 1.0*RSTR


    """

    def __init__(self, indicator_data_path: str, quota_data_path: str = None,
                 index_data_path: str = None):
        """

        :param indicator_data_path: 指标数据地址
        :param market_data_path: 行情数据地址
        """
        self.ind_df = pd.read_csv(indicator_data_path, dtype={'symbol': str}, parse_dates=['trade_date'])
        self.start_date = datetime(2016, 1, 1)
        self.end_date = datetime(2020, 3, 20)
        self.time_span = self.end_date - self.start_date
        self.length = self.time_span.days
        self.quota_df = pd.read_csv(quota_data_path, dtype={'symbol': 'str'}, parse_dates=['date'])
        self.quota_ddf = dd.read_csv(quota_data_path, dtype={'symbol': 'str'}, parse_dates=['date'])
        self.index_df = pd.read_csv(index_data_path, parse_dates=['date'])

    @property
    def lncap(self):
        return np.log(self.ind_df['total_mv']*10000)
        # print(self.data.lncap)

    def rstr(self, T=504, L=21, half_life=126):
        rstr = np.tile(np.nan, self.length)
        for t in np.arange(T + L, self.length+1):
            rt = self.quota_df.close.pct_change().iloc[(t-T-L):(t-L)].copy()
            # 0.0000985341949802 = 9.85e-5  无风险收益的日平均收益率
            rft = 9.85e-5
            rstr[t-1] = sum((np.log(1+rt)-np.log(1+rft)) * halflife(half_life, length=T))
        return rstr

    def rstr_dk(self, T=504, L=21, half_life=126):
        rstr = np.tile(np.nan, self.length)
        rstr = dd.from_array(rstr).compute()
        rt_whole = (self.quota_ddf.close.diff()/self.quota_ddf.close.shift()).compute()
        for t in np.arange(T+L, self.length+1):
            rt = rt_whole[(t-T-L):(t-L)]
            rft = 9.85e-5
            # rstr[t - 1] = sum((np.log(1 + rt) - np.log(1 + rft)) * halflife_da(half_life, length=T))
            rstr[t - 1] = sum((np.log(1+rt.values)-np.log(1+rft)) * halflife(half_life, length=T))
        return rstr

    def beta(self, symbol, t, T=252, halflife=63):
        symbol_return = self.quota_df[t-T:t][self.quota_df['symbol'] == symbol]['close']
        symbol_return = symbol_return.diff()/symbol_return.shift()
        symbol_return = symbol_return.fillna(method='bfill')
        universe_return = self.index_df[t-T:t]['close']
        universe_return = universe_return.diff()/universe_return.shift()
        universe_return = universe_return.fillna(method='bfill')
        universe_return_np = universe_return.to_numpy()
        symbol_return_np = symbol_return.to_numpy()
        numerator_np = (symbol_return_np-symbol_return_np.mean())*(universe_return_np-universe_return_np.mean())
        numerator_pd = pd.Series(numerator_np)
        numerator_pd = numerator_pd.ewm(halflife=halflife).mean()
        denominator_np = (symbol_return_np-symbol_return_np.mean())**2
        denominator_pd = pd.Series(denominator_np)
        denominator_pd = denominator_pd.ewm(halflife=halflife).mean()
        beta_np = numerator_pd.to_numpy()/denominator_pd.to_numpy()
        return beta_np


        



cne5 = CNE5('D:/data/indicator_data/whole_data.csv', 'D:/data/day_data/whole_data.csv', 'D:/data/zh_index_daily_300.csv')
import time
b = time.time()
print(cne5.beta('sh600000', 600))
e = time.time()
print("++++++++++++++++++++", e-b)
