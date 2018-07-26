# -*- coding: utf-8 -*-
import scrapy


class ShuidiSpider(scrapy.Spider):
    name = 'shuidi'
    allowed_domains = ['shuidi.cn']
    # start_urls = ['http://shuidi.cn/']

    def start_requests(self):
        url = "http://shuidi.cn/company-f23bbb9f1ad0e4c2388923042efacc4a.html"
        yield scrapy.Request(url)

    def parse(self, response):
        print(response.text)
        # pass
