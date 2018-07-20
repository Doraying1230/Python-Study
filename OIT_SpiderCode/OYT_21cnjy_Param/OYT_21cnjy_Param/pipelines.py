# -*- coding: utf-8 -*-
# from .conf.configuration import configuration as config
import codecs
import time
import json
import os
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
class Oyt21CnjyParamPipeline(object):
    # @classmethod
    # def from_crawler(cls, crawler):
    #     return cls(
    #         mongo_uri=crawler.settings.get('MONGO_URI'),
    #         mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
    #     )

    def open_spider(self, spider):
        self.SavePath = "D:\\21cnjy\\{0}\\categories_data\\".format(time.strftime('%Y%m%d', time.localtime()))
        path = self.SavePath+'{0}\\'.format(spider.name)
        isExists = os.path.exists(path)
        if isExists:
            pass
        else:
            os.makedirs(path)
        self.file = codecs.open(path + 'data.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        print('进程打印信息：',spider.name)
        lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(lines)
        return item

    def close_spider(self, spider):
        self.file.close()
