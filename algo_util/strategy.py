#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/20 23:34
# @Author  : LiJing
# @File    : strategy.py


from .BacktestBase import BacktestBase
import pandas as pd
import numpy as np


class StkSel(BacktestBase):

    def get_data(self):
        raw = pd.read_csv('http://hilpisch.com/pyalgo_eikon_eod_data.csv',
                          index_col=0, parse_dates=True).dropna()
        raw = pd.DataFrame(raw[self.symbol])
        raw = raw.loc[self.start:self.end]
        raw.rename(columns={self.symbol: 'price'}, inplace=True)
        raw['return'] = np.log(raw / raw.shift(1))
        raw['SMA1'] = raw['price'].rolling(self.SMA1).mean()
        raw['SMA2'] = raw['price'].rolling(self.SMA2).mean()
        self.data = raw

    # 
    def run_strategy(self):
        data = self.data.copy().dropna()



