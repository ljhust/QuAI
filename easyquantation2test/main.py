#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/4 15:13
# @Author  : LiJing
# @File    : main.py


import easyquotation
import time

start = time.time()
quotation = easyquotation.use('sina')

all = quotation.all
all_market = quotation.all_market
stock_list = quotation.stock_list
market_snapshot = quotation.market_snapshot(prefix=True)
stock_codes = easyquotation.update_stock_codes()


to_print = quotation.market_snapshot(prefix=True)

end = time.time()

print(quotation)
print('time elapse: ', end-start)

# import akshare as ak
# stock_zh_a_spot_em_df = ak.stock_zh_a_spot_em()re
# print(stock_zh_a_spot_em_df)