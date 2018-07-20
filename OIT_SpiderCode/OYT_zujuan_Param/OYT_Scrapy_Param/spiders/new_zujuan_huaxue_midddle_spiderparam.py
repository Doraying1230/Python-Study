#coding:utf-8
import scrapy
from ..common.BaseObject import BaseObject
from scrapy.spider import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request,FormRequest
from scrapy.selector import Selector
from scrapy.http.cookies import CookieJar
from fake_useragent import UserAgent
import time
import re
import os
class ZuQuanLoadData(BaseObject,CrawlSpider):
    name = 'zujuan_huaxue_middle_param'
    custom_settings = {
        'DOWNLOAD_DELAY': 3, 'CONCURRENT_REQUESTS_PER_IP': 5,
        'ITEM_PIPELINES': {'OIT_ScrapyData.pipelines.OitScrapydataPipeline': None, }

    }
    def __init__(self):
        ua = UserAgent()
        user_agent = ua.random
        self.file_name='zujuan_huaxue_middle_param'
        self.cookieValue = {'xd': '75519cb9f2bf90d001c0560f5c40520062a60ada9cb38350078f83e04ee38a31a%3A2%3A%7Bi%3A0%3Bs%3A2%3A%22xd%22%3Bi%3A1%3Bi%3A2%3B%7D',
                            'isdialog': 'bad3c21672f08107d1d921526d191f58bd47d79e7dbb432bd32624a836b42e85a%3A2%3A%7Bi%3A0%3Bs%3A8%3A%22isdialog%22%3Bi%3A1%3Bs%3A4%3A%22show%22%3B%7D',
                            '_csrf': 'c46fcf318573a3669dc5292a70f0f0b0412f0dc06a496a0caecd50bbfbbd8f9ea%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22ZLzvBUGQ0Qwpp7U-3Ay5yRBroqnqO76Z%22%3B%7D',
                            'device': '310bdaba05b30bb632f66fde9bf3e2b91ebc4d607c250c2e1a1d9e0dfb900f01a%3A2%3A%7Bi%3A0%3Bs%3A6%3A%22device%22%3Bi%3A1%3BN%3B%7D',
                            '_sync_login_identity': '1864fd5ffb62277fe66a445e3ff8c812d1459ba1aad454022e7f7fd17aa1e84da%3A2%3A%7Bi%3A0%3Bs%3A20%3A%22_sync_login_identity%22%3Bi%3A1%3Bs%3A50%3A%22%5B1236678%2C%22nrddR6I3sbMlKJ4RO0e35TK9T4v80DQQ%22%2C86400%5D%22%3B%7D',
                            'PHPSESSID': 'r4k30lsjr52tsbjgm230b4g7l7', 'chid': '5b430739a3b769fd149f00e15357022edc2cea4511390cba95225dcbcaacc273a%3A2%3A%7Bi%3A0%3Bs%3A4%3A%22chid%22%3Bi%3A1%3Bs%3A1%3A%227%22%3B%7D',
                            '_identity': '58c14c05c924b81b6d3f45456b78313e53d075bc4db1a95f0bc64358d6ba2fafa%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A50%3A%22%5B1236678%2C%22f2828bc8e0832bb1d0de103ad9c60a5b%22%2C86400%5D%22%3B%7D',
                            'Hm_lvt_6de0a5b2c05e49d1c850edca0c13051f': '1515573560,1515666945',
                            'Hm_lpvt_6de0a5b2c05e49d1c850edca0c13051f': '1515667072'}
        self.hearders = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Connection': 'keep - alive',
            # 'Referer': 'http://www.zujuan.com/question /index?chid = 3 & xd = 1',
            'User-Agent': user_agent#'Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'
        }
        print(self.hearders)
        self.domain = 'http://www.zujuan.com'
    def start_requests(self):
        start_url = 'http://www.zujuan.com/question/index?chid=7&xd=2'
        return [Request(url=start_url,cookies=self.cookieValue,headers=self.hearders,callback=self.parse_version)]
    def parse_version(self,response):
        result = response.body.decode()
        resu = Selector(text=result)
        versionTexts = resu.xpath('//div[@class="type-items"][1]/div/div/div/a/text()').extract()
        versionUrls = resu.xpath('//div[@class="type-items"][1]/div/div/div/a/@href').extract()
        version = dict(zip(versionTexts, versionUrls))
        print(version)#{'人教版': '/question?bookversion=11740&chid=3&xd=1', '青岛版六三制': '/question?bookversion=23087&chid=3&xd=1', '北师大版': '/question?bookversion=23313&chid=3&xd=1', '苏教版': '/question?bookversion=25571&chid=3&xd=1', '西师大版': '/question?bookversion=47500&chid=3&xd=1', '青岛版五四制': '/question?bookversion=70885&chid=3&xd=1', '浙教版': '/question?bookversion=106060&chid=3&xd=1'}
        for text in version :
            if ('人教' in text):
                manURL =self.domain+version[text]#http://www.zujuan.com/question?bookversion=25571&chid=3&xd=1
                deliver_param = {'version':'人教版'}
                deliver_param['course'] = '化学'
                return [Request(url=manURL, meta=deliver_param,cookies=self.cookieValue, headers=self.hearders,callback=self.parse_categories)]
            # elif('沪科' in text):
            #     manURL = self.domain + version[text]  # http://www.zujuan.com/question?bookversion=25571&chid=3&xd=1
            #     deliver_param = {'version': '沪科版'}
            #     deliver_param['course'] = '物理'
            #     return [Request(url=manURL,meta=deliver_param, cookies=self.cookieValue, headers=self.hearders,
            #                     callback=self.parse_categories)]
            else:
                pass
    def parse_categories(self,response):
        print(123,response.meta)
        result  = response.body.decode()
        resu = Selector(text=result)

        categoriesTexts = resu.xpath('//div[@class="type-items"][2]/div/div/div/a/text()').extract()
        categoriesUrls = resu.xpath('//div[@class="type-items"][2]/div/div/div/a/@href').extract()
        #http://www.zujuan.com/question?categories=25576&bookversion=25571&nianji=25576&chid=3&xd=1
        categories = dict(zip(categoriesTexts, categoriesUrls))
        print(123,categories)
        categories_list = []
        # print(categories)# {'一年级上册': '/question?categories=25572&bookversion=25571&nianji=25572&chid=3&xd=1', '一年级下册': '/question?categories=25573&bookversion=25571&nianji=25573&chid=3&xd=1', '二年级上册': '/question?categories=25574&bookversion=25571&nianji=25574&chid=3&xd=1', '二年级下册': '/question?categories=25575&bookversion=25571&nianji=25575&chid=3&xd=1', '三年级上册': '/question?categories=25576&bookversion=25571&nianji=25576&chid=3&xd=1', '三年级下册': '/question?categories=25577&bookversion=25571&nianji=25577&chid=3&xd=1', '四年级上册': '/question?categories=25578&bookversion=25571&nianji=25578&chid=3&xd=1', '四年级下册': '/question?categories=25579&bookversion=25571&nianji=25579&chid=3&xd=1', '五年级上册': '/question?categories=25580&bookversion=25571&nianji=25580&chid=3&xd=1', '五年级下册': '/question?categories=25581&bookversion=25571&nianji=25581&chid=3&xd=1', '六年级上册': '/question?categories=25582&bookversion=25571&nianji=25582&chid=3&xd=1', '六年级下册': '/question?categories=25592&bookversion=25571&nianji=25592&chid=3&xd=1'}
        for text in categories:
            categories_list.append(text)
        comment = 0
        while comment < len(categories_list):
            text = categories_list[comment]
            nianjiContentUrl = self.domain + categories[text]
            print(12,nianjiContentUrl)
            nianjiContentUrl =self.domain+categories[text]
            comment += 1
            response.meta['nianji'] = text
            yield Request(url=nianjiContentUrl,meta=response.meta,cookies=self.cookieValue, headers=self.hearders,callback=self.parse_categories_content)

    def parse_categories_content(self,response):
        print(123,response.meta)
        result = response.body.decode()
        resu = Selector(text=result)
        sectionsText = resu.xpath('//div[@id="J_Tree"]/div/a/text()').extract()
        sectionsUrl = resu.xpath('//div[@id="J_Tree"]/div/a/@href').extract()
        sections = dict(zip(sectionsText,sectionsUrl))
        print(sections)
        self.make_file()
        sections_Text = []
        sections_number = []
        for text in sections:
            sections_Text.append(text)
            categoriesNumber = sections[text]
            print(type(categoriesNumber),categoriesNumber)
            ret = re.findall(r'categories=(\d*)&',categoriesNumber)
            sections_number.append(ret[0])
            print(123, ret)
            need_sections_dict = dict(zip(sections_Text, sections_number))

            nianji = response.meta ['nianji']
            response.meta[nianji] = need_sections_dict
            need_sections_str = str(response.meta)

        with open('d:\\xiti10001\\zujuan\\{0}\\{1}\\categories_huaxue_{0}.txt'.format(time.strftime('%Y%m%d',time.localtime(time.time())),self.file_name),'a') as f:
            f.write(need_sections_str)
            f.write('\n')

            # categoriesNumber_s = categoriesNumber.find('=')
            # print(categoriesNumber_s)
            # categoriesNumber_e = categoriesNumber.find('&')
            # print(categoriesNumber_e)
            # categoriesNumbers = categoriesNumber[categoriesNumber_s,categoriesNumber_e]


    def make_file(self):
        path = 'd:\\xiti10001\\zujuan\\{0}\\{1}'.format(time.strftime('%Y%m%d',time.localtime(time.time())),self.file_name)
        isExists = os.path.exists(path)
        if (isExists):
            pass;
        else:
            os.makedirs(path)









