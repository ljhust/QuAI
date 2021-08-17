#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/25 19:15
# @Author  : LiJing
# @File    : Feature.py


"""
负责生成新的feature序列
"""

import numpy as np

from abc import ABCMeta, abstractmethod
from typing import Callable, NewType


class Feature:

    """
    从real为基础的数据中，通过调用ufunc建立新的real
    """
    @abstractmethod
    def creat_feature(self, real: np.ndarray, ufunc: Callable):
        pass


