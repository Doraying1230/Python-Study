# -*- coding: utf-8 -*-
import scrapy
import requests
from scrapy_redis.spiders import RedisCrawlSpider
from ..items import TianyanItem


class ChaSpider(RedisCrawlSpider):
    name = 'tycha'
    allowed_domains = ['www.tianyancha.com', ]
    redis_key = 'tianyancha:filter:url'

    def parse(self, response):
        url = response.xpath('//a[@class="sec-c1"]/@href').extract()
        print('result url', url)
        title = response.xpath('//a[@class="sec-c1"]/@title').extract()
        print('result title', title)
        ret = map(lambda x, y: (x, y), url, title)
        for tup in ret:
            yield ChaSpider.parse_item(tup)

    @staticmethod
    def parse_item(tup):
        item = TianyanItem()
        title, url = tup
        item['_id'] = ''
        item['title'] = title
        item['url'] = url
        item['update_time'] = ''

        return item

