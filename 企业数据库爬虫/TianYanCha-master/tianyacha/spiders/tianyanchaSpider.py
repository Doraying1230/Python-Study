# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from  selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from pyquery import PyQuery as pq
import time,re


class TianyanchaspiderSpider(scrapy.Spider):
    name = 'tianyanchaSpider'
    allowed_domains = ['https://bj.tianyancha.com']
    keyword = input('请输入查询的公司名称：')
    # start_urls = ['http://bj.tianyancha.com/search?key='+str(keyword)]
    print('-----------------------------天眼查！start!!!------------------------------')
    def start_requests(self):
        url = 'http://bj.tianyancha.com/login'
        
        yield scrapy.Request(url=url,callback=self.parse)
    #页面处理方法
    def parse(self, response):
        print('-----------------------------天眼查！start!!!------------------------------')
        print(response.text)
        '''

        :param response: 请求发出之后返回的响应
        :return: 页面处理完成之后的数据或者是请求
        '''

