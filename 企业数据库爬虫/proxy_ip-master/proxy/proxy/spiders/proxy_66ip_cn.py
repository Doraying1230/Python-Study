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


class Proxy66ipcnSpider(scrapy.Spider):
    name = '66ipcn'
    allowed_domains = ['www.66ip.cn']
    start_urls=['http://www.66ip.cn/nmtq.php?getnum=800&isp=0&anonymoustype=0&start=&ports=&export=&ipaddress=&area=1&proxytype=0&api=66ip']

    def parse(self, response):
        print response.url
        i = ProxyItem()
        regex=re.compile(r'(?<=<script src=")[\s\S]*?(?=<script type=")')
        list_text=regex.findall(response.body,re.S)
        if list_text:
            #list_url=list_text[0].split("<br \>")
            list_ip_port=list_text[0].replace("\r","").replace("\n","").replace("\t","").split("</script>")[1].split("<br />")

        for ip_port in list_ip_port:
            if ip_port:
                i['source'] = 'www.66ip.cn'
                ip_port = ip_port.split(":")
                i['ip'] = ip_port[0].strip(" ")
                i['port'] =ip_port[1].strip(" ") 

                ## type ####################
                i['type'] = D_TYPE['NA'] #to default set
                ###############################

                ## support ####################
                i['support']=0 #to default set
                ###############################

                yield i
            else:
               return 

        #raise scrapy.exceptions.CloseSpider('gen appid error (%s)' %(str(e)))

