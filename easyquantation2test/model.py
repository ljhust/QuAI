#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/6 13:43
# @Author  : LiJing
# @File    : model.py

from sqlalchemy import Column, Date, Float, Integer, SmallInteger, String, Time
from sqlalchemy.dialects.mysql import INTEGER, TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData, Table


Base = declarative_base()
metadata = Base.metadata


class SnapShot(Base):
    __tablename__ = 'snapshot'

    name = Column(VARCHAR(10))
    open = Column(Float)
    close = Column(Float)
    now = Column(Float)
    low = Column(Float)
    buy = Column(Float)
    sell = Column(Float)
    turnover = Column(Integer) # 交易股数
    volume = Column(Float) # 交易金额
    bid1_volume = Column(Integer)
    bid1 = Column(Float)
    bid2_volume = Column(Integer)
    bid2 = Column(Float)
    bid3_volume = Column(Integer)
    bid3 = Column(Float)
    bid4_volume = Column(Integer)
    bid4 = Column(Float)
    bid5_volume = Column(Integer)
    bid5 = Column(Float)
    ask1_volume = Column(Integer)
    ask1 = Column(Float)
    ask2_volume = Column(Integer)
    ask2 = Column(Float)
    ask3_volume = Column(Integer)
    ask3 = Column(Float)
    ask4_volume = Column(Integer)
    ask4 = Column(Float)
    ask5_volume = Column(Integer)
    ask5 = Column(Float)
    date = Column(Date)
    time = Column(Time)

    id = Column(VARCHAR(50), primary_key=True)