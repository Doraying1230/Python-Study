# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProxyItem(scrapy.Item):
    # define the fields for your item here like:
    ip = scrapy.Field()
    port = scrapy.Field()
    status = scrapy.Field() ## 0 initialized 1 available 2 invalid
    type = scrapy.Field()   ## 0 transparent 1 high anonymity 2 normal anonymity
    update_time = scrapy.Field()
    err_count = scrapy.Field()
    source = scrapy.Field()
    forbid = scrapy.Field() ## 1688|taobao
    weight = scrapy.Field() ## 1~10
    support = scrapy.Field()## 0x1 http 0x2 https 0x4 socket5 0x8 socket4
