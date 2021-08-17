#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/7 0:20
# @Author  : LiJing
# @File    : mysql_tool.py


import pandas as pd
from sqlalchemy import create_engine, types, Column
from sqlalchemy.ext.declarative import declarative_base
from smodel import Base
from sqlalchemy.orm import sessionmaker


class MysqlDumper:

    def __init__(self, uri='localhost', user='root', password='19860725', database='easyquotation', dump_table='snapshot'):
        self.uri = uri
        self.user = user
        self.password = password
        self.database = database
        self.engine = create_engine("mysql://{}:{}@{}/{}?charset=utf8mb4".
                                    format(self.user, self.password, self.uri, self.database))
        self.dump_table = dump_table
        self.session = sessionmaker(bind=self.engine)()

    def create_table(self):
        Base.metadata.create_all(self.engine)

    def dump_df(self, df: pd.DataFrame):
        df.to_sql(self.dump_table, con=self.engine, index=False, if_exists='append')


if __name__ == "__main__":
    dumper = MysqlDumper()
    dumper.create_table()
