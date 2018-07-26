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


class ProxyXicidailiSpider(scrapy.Spider):
    name = 'xicidaili'
    allowed_domains = ['www.xicidaili.com']
    start_urls=['http://www.xicidaili.com/nt']
    start_urls.append('http://www.xicidaili.com/nt/2')
    start_urls.append('http://www.xicidaili.com/nn')
    start_urls.append('http://www.xicidaili.com/nn/2')

    def parse(self, response):
        i = ProxyItem()
        index = 1
        while True:
            #item = response.xpath("//div[@id='list']/table/tbody/tr[%d]/td/text()" %(index)).extract()
            item = response.xpath("//table[@id]/tr[@class][%d]/td/text()" %(index)).extract()
            if item:
                i['source'] = 'www.xicidaili.com'
                i['ip'] = item[0]
                i['port'] = item[1]

                ## type ####################
                if item[4] == u'透明':
                    i['type'] = D_TYPE['TP']
                elif item[2] == u'高匿':
                    i['type'] = D_TYPE['HA']
                else:
                    i['type'] = D_TYPE['NA']
                ###############################

                ## support ####################
                support = item[5]
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

