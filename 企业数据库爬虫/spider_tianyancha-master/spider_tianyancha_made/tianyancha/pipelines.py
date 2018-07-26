# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import datetime
from scrapy import log
from scrapy.conf import settings

class TianyanchaPipeline(object):

    def __init__(self, settings):
        self.settings = settings

    @classmethod
    def from_crawler(cls, crawler):
        return cls(settings = crawler.settings)

    def process_item(self, item, spider):
        i = item['update_item']

        try:
            ## 第一次需求 匹配公司是否存在
            spider.mongo_db.made.update_one({'company_name': i['company_name']}, {'$set': {'check': i['check'], 'cp_status': i['cp_status'], 'status': 1}})
            spider.log('update mongo succed!  company_name=%s, check=%s, cp_status=%s' % (i['company_name'], i['check'], i['cp_status']), level=log.INFO)
        except Exception, e:
            spider.log('update mongo failed! company_name=%s (%s)' % (i['company_name'], str(e)), level=log.ERROR)
