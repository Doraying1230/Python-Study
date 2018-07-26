# -*- coding:utf-8 -*-
from scrapy.http import Request
import xml.etree.ElementTree
from scrapy.selector import Selector

import scrapy
import re
from pymongo import MongoClient
from copy import copy
import traceback
import pymongo
from scrapy import log
from tianyancha.items import TianyanchaItem
import time
import datetime
import sys
import logging
import random
import binascii
from scrapy.conf import settings
import json

reload(sys)
sys.setdefaultencoding('utf-8')


class TianyanchaSpider(scrapy.Spider):
    name = "spider_made"

    def __init__(self, settings, *args, **kwargs):
        super(TianyanchaSpider, self).__init__(*args, **kwargs)
        self.settings = settings
        mongo_info = settings.get('MONGO_INFO', {})

        try:
            self.mongo_db = pymongo.MongoClient(mongo_info['host'], mongo_info['port']).tianyancha
        except Exception, e:
            self.log('connect mongo 192.168.60.65:10010 failed! (%s)' % (str(e)), level=log.CRITICAL)
            raise scrapy.exceptions.CloseSpider('initialization mongo error (%s)' % (str(e)))

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def start_requests(self):

        try:
            tyc_url = 'https://m.tianyancha.com/search?key='
            # tyc_url = 'https://www.tianyancha.com/search?key='
            records = self.mongo_db.made.find({'status':0}, {'company_name': 1})
            for record in records:
                company_name = record['company_name']
                company_url = ''.join([tyc_url, company_name, '&checkFrom=searchBox'])
                meta = {'dont_redirect': True, 'company_name': company_name, 'company_url': company_url, 'dont_retry': True}
                self.log('spider new url=%s' % (company_url), level=log.INFO)
                yield scrapy.Request(url = company_url, meta = meta, callback = self.parse, dont_filter = True)
            # company_name = u'山东省临沂市斯利可桐木制品厂'
            # # company_name = u'重庆金联陶瓷有限公司'
            # company_name = company_name.decode('utf-8')
            # company_url = ''.join(['https://www.tianyancha.com/search?key=', company_name, '&checkFrom=searchBox'])
            # print company_url
            # meta = {'dont_redirect': True, 'company_name': company_name, 'dont_retry': True}
            # self.log('spider new url=%s' % (company_url), level=log.INFO)
            # yield scrapy.Request(url = company_url, meta = meta, callback = self.parse, dont_filter = True)
        except:
            self.log('start_request error! (%s)' % (str(traceback.format_exc())), level=log.INFO)


    ## 核实公司是否找到
    def parse(self, response):
        sel = Selector(response)

        ret_item = TianyanchaItem()
        ret_item['update_item'] = {}
        i = ret_item['update_item']
        i['company_name'] = response.meta['company_name']
        company_url = response.meta['company_url']

        if response.status != 200 or len(response.body) <= 0:
            self.log('fetch failed ! status = %d, company_url=%s' % (response.status, company_url), level = log.WARNING)

        ## m 站xpath
        tyc_company_name = sel.xpath("//div[@class='new-border-bottom pt5 pb5 ml15 mr15'][1]//a[@class='query_name in-block']/span/em/text()").extract()
        # tyc_company_name = sel.xpath("//div[@class='search_result_single search-2017 pb25 pt25 pl30 pr30'][1]//\
                # a[@class='query_name sv-search-company f18 in-block vertical-middle']/span/em/text()").extract()

        if tyc_company_name:
            tyc = tyc_company_name[0].strip()
            if tyc == i['company_name']:
                i['check'] = u"已核实"
            else:
                i['check'] = u"没找到"
        else:
            i['check'] = u"没找到"

        self.log('check done! company_name=%s, check=%s' % (i['company_name'], i['check']), level=log.INFO)
        yield ret_item



