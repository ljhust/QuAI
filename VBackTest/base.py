#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/25 16:13
# @Author  : LiJing
# @File    : base.py

import pandas as pd

"""
vector backtest 投研框架的基础类，利用python的向量化计算生态，主要设计目标如下：
1， 进入的基础数据全是pd.DataFrame；
2， Feature: 负责创建新的向量数据，并回存self.data;
3， Signal: 事件回调，能够计算出序列的信号；
4， Position: 计算仓位序列；
5， Perf: 总体回报指标；
6， Scheduler: 负责回调； 
"""
class VBase:

    """
    :param raw-> 包含 h
    """
    def __init__(self, raw: pd.DataFrame):
