# -*- coding: utf-8 -*-
import os
import scrapy
import urllib
import codecs
import pymongo
import re
import time
from scrapy import log
from scrapy.shell import inspect_response
from proxy.items import ProxyItem
from proxy.settings import D_STATUS, D_TYPE, D_SUPPORT


class ProxyhaodailiSpider(scrapy.Spider):
    name = 'haodaili'
    allowed_domains = ['www.haodaili.com']
    start_urls = ['http://www.haodaili.com/guonei/%d' %(i) for i in range(1, 11)]

    def parse(self, response):
        i = ProxyItem()
        index = 1
        while True:
            item = response.xpath("//table[@class='proxy_table']/tr[%d]/td/text()" %(index)).extract()
            if item:
                if item[0].find('ip')!='-1':
                    continue
                i['source'] = 'www.haodaili.com'
                i['ip'] = item[0].strip('\r\n\t')
                i['port'] = item[1].strip('\r\n\t')

                ## type ####################
                if item[4] == u'透明':
                    i['type'] = D_TYPE['TP']
                elif item[2] == u'高匿':
                    i['type'] = D_TYPE['HA']
                else:
                    i['type'] = D_TYPE['NA']
                ###############################

                ## support ####################
                support = item[3]
                if support and support.find(',') == -1:
                    support += ',' + support
                support = reduce(lambda x, y: D_SUPPORT.get(x,0) | D_SUPPORT.get(y,0), [s.strip() for s in support.split(',')]) if support else 0
                i['support'] = support
                ###############################

                index += 1
                yield i
            else:
               return 

        #raise scrapy.exceptions.CloseSpider('gen appid error (%s)' %(str(e)))

