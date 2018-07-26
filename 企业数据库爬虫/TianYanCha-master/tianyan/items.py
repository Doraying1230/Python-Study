# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TianyanItem(scrapy.Item):
    _id = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    update_time = scrapy.Field()
