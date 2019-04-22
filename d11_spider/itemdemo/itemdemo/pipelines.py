# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CsvPipeline(object):
    def process_item(self, item, spider):

        print(item)
        print('存储Redis CSV都可以 数据项的最终处理')
        return item

class MongoDBPipeline(object):
    def process_item(self, item, spider):
        # 连接MongoDB
        # 找到数据库
        # 数据存储
        return item

class RedisPipeline(object):
    def process_item(self, item, spider):
        # 连接Redis
        # 找到数据库
        # 数据存储
        pass
        return




