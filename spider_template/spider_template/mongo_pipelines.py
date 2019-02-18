# -*- coding: utf-8 -*-


__author__ = 'zhougy'
__date__ = '2018/12/25 下午3:01'

from settings import MONGODB_SETTINGS
import pymongo


class MongoPipeLines(object):
    def __init__(self, db_host, db_name, db_port, collect_sy):
        self.__db_host = db_host
        self.__db_name = db_name
        self.__db_port = db_port
        self.__collect_sy = collect_sy

    @classmethod
    def from_crawler(cls, *args, **kwargs):
        db_host = MONGODB_SETTINGS['db_host']
        db_name = MONGODB_SETTINGS['db_name']
        db_port = MONGODB_SETTINGS['db_port']
        collect_sy = MONGODB_SETTINGS['collect_sy']
        return cls(db_host=db_host, db_name=db_name, db_port=db_port,
                   collect_sy=collect_sy)

    def open_spider(self, spider):
        '''
        初始工作，连接数据库操作
        :param spider:
        :return:
        '''
        self.__client = pymongo.MongoClient(host=self.__db_host,
                                            port=self.__db_port)
        self.__db = self.__client[self.__db_name]

    def process_item(self, item, spider):
        '''
        mongodb 处理数据操作函数
        :param item:
        :param spider:
        :return:
        '''

        item_name = item.get_name()
        spider_name=spider.name
        if item_name == "XxsyItem" and spider_name=='xxsy':
            sy_collection = self.__db[self.__collect_sy]
            data = dict(item)
            sy_collection.insert(data)
            return item
        elif item_name == "JDGoodItem" and spider_name=='jd':
            sy_collection = self.__db[self.__collect_sy]
            data = dict(item)
            sy_collection.insert(data)
            return item
        elif item_name == "TmallItem" and spider_name=='tmall':
            sy_collection = self.__db[self.__collect_sy]
            data = dict(item)
            sy_collection.insert(data)
            return item

    def close(self, spider):
        '''
        清理资源工作
        :param spider:
        :return:
        '''
        self.__client.close()
