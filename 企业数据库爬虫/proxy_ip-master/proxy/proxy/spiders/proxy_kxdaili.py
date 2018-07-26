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


class ProxyKxdailiSpider(scrapy.Spider):
    name = 'kxdaili'
    allowed_domains = ['www.kxdaili.com']
    start_urls=['http://www.kxdaili.com']
    urls = [

            'http://www.kxdaili.com/ipList/%d.html#ip' %(i) for i in range(2,11)

            ]
    start_urls.extend(urls)

    def parse(self, response):
        i = ProxyItem()
        index = 2
        while True:
            item = response.xpath("//table[@class]/tbody/tr[%d]/td/text()" %(index)).extract()
            #list_ip=response.xpath('//table[@class]/tbody/tr/td[1]/text()').extract()
            if item:
                i['source'] = 'www.kxdaili.com'
                i['ip'] = item[0]
                i['port'] = item[1]

                ## type ####################
                if item[3] == u'透明':
                    i['type'] = D_TYPE['TP']
                elif item[3] == u'高匿':
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

