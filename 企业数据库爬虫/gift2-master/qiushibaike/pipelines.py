# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.mail import MailSender
import pymysql
import pymysql.cursors
from twisted.enterprise import adbapi
class QiushibaikePipeline(object):
    # def process_item(self, item, spider):
    #     return item

    def __init__(self):
        dbargs = dict(
            host='127.0.0.1',
            db='qiushibaike',
            user='root',
            passwd='root',
            cursorclass=pymysql.cursors.DictCursor,
            charset='utf8',
            use_unicode=True
        )
        self.dbpool = adbapi.ConnectionPool('pymysql', **dbargs)

    '''
    The default pipeline invoke function
    '''

    def process_item(self, item, spider):
        res = self.dbpool.runInteraction(self.insert_into_table, item)
        return item

    # 插入的表，此表需要事先建好
    def insert_into_table(self, conn, item):
        conn.execute('insert into qiushibaike(content, ulike) values(%s,%s)', (
            item['content'],
            item['like'])
        )