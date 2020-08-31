import pymongo
from motor.motor_asyncio import AsyncIOMotorClient
from motor import MotorClient
import asyncio


def util_sql_mongo_setting(uri='mongodb://localhost:27017/quantaxis'):
    """
    explanation:
        根据给定的uri返回一个MongoClient实例，采用@几何建议以使用加密

    params:
        * uri ->:
            meaning: mongodb连接uri
            type: str
            optional: [null]

    return:
        MongoClient

    demonstrate:
        Not described

    output:
        Not described
    """

    # 采用@几何的建议,使用uri代替ip,port的连接方式
    # 这样可以对mongodb进行加密:
    # uri=mongodb://user:passwor@ip:port
    client = pymongo.MongoClient(uri)
    return client

# async


def util_sql_async_mongo_setting(uri='mongodb://localhost:27017/quantaxis'):
    """
    explanation:
        根据给定的uri返回一个异步AsyncIOMotorClient实例

    params:
        * uri ->:
            meaning: mongodb连接uri
            type: str
            optional: [null]

    return:
        AsyncIOMotorClient

    demonstrate:
        Not described

    output:
        Not described
    """
    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    # async def client():
    return AsyncIOMotorClient(uri, io_loop=loop)
    # yield  client()


ASCENDING = pymongo.ASCENDING
DESCENDING = pymongo.DESCENDING
util_sql_mongo_sort_ASCENDING = pymongo.ASCENDING
util_sql_mongo_sort_DESCENDING = pymongo.DESCENDING

if __name__ == '__main__':
    # test async_mongo
    client = util_sql_async_mongo_setting().quantaxis.stock_day
    print(client)
