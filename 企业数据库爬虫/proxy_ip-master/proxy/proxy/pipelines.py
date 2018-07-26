# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import time
from pymongo import MongoClient
from proxy.settings import D_STATUS, D_TYPE, D_SUPPORT

class ProxyPipeline(object):

    def open_spider(self, spider):
        try:
            self.db = MongoClient('192.168.60.64', 10010).proxy
            #self.db.ip_tbl.ensure_index([("ip", 1)], unique=True)
            self.db.ip_tbl.ensure_index([("ip", 1),("port",1)], unique=True)
        except Exception, e:
            #self.log('connect mongo 192.168.60.64:10010 failed! (%s)' %(str(e)), level=log.CRITICAL)
            self.log('connect mongo 192.168.60.64:10010 failed! (%s)' %(str(e)), level=self.logger.CRITICAL)

    def close_spider(self, spider):
        if self.db:
            pass
            #self.db.close()

    def process_item(self, item, spider):
        if item['ip'] and item['port']:
            try:
                self.db.ip_tbl.insert({'ip':item['ip'], 'port':str(item['port']), 
                    'source':item['source'], 'type':item['type'],
                    'support':item['support'], 'status':D_STATUS['INIT'],
                    'update_time':time.time(), 'err_count':0,
                    'forbid':'', 'weight':10})
            except Exception, e:
                #spider.log('insert mongo error! (%s)' %(str(e)), level=log.WARNING)
                spider.log('insert mongo error! (%s)' %(str(e)), level=self.logger.WARNING)
        return item
