#coding:utf-8
import scrapy
from ..conf.configuration import configurationS as config
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
    name = 'zujuan_yuwen_param'
    custom_settings = {
        'DOWNLOAD_DELAY': 3, 'CONCURRENT_REQUESTS_PER_IP': 5,
        'ITEM_PIPELINES':{'OIT_ScrapyData.pipelines.OitScrapydataPipeline': None,}

    }
    def __init__(self):
        ua = UserAgent()
        user_agent = ua.random
        self.file_name = 'zujuan_yuwen_param'
        self.cookieValue = {'isdialog': 'bad3c21672f08107d1d921526d191f58bd47d79e7dbb432bd32624a836b42e85a%3A2%3A%7Bi%3A0%3Bs%3A8%3A%22isdialog%22%3Bi%3A1%3Bs%3A4%3A%22show%22%3B%7D', '_csrf': '43bb3a38ab3e6dcb7b878e14b4d4e550bb207d7cd2114ecb23107512e428ba2ea%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22wI5jsZy4hfWZao2FGydI4W1K_iawIds4%22%3B%7D',
                            'device': '310bdaba05b30bb632f66fde9bf3e2b91ebc4d607c250c2e1a1d9e0dfb900f01a%3A2%3A%7Bi%3A0%3Bs%3A6%3A%22device%22%3Bi%3A1%3BN%3B%7D',
                            '_sync_login_identity': 'e18e5414f70a685a3db816b573812e75a4cc2f4ffe1551d309161116023ef1e3a%3A2%3A%7Bi%3A0%3Bs%3A20%3A%22_sync_login_identity%22%3Bi%3A1%3Bs%3A50%3A%22%5B1285670%2C%22Z-OuNcdl0fTBvtIZ5cpQJDUe497g6YKw%22%2C86400%5D%22%3B%7D',
                            'PHPSESSID': 'r4t085qi4k8eetr5tgjevj2466',
                            'chid': '27e8704a451201531cc9941f6f3b709b7e13397751c04b090603ffdb0a56dfb9a%3A2%3A%7Bi%3A0%3Bs%3A4%3A%22chid%22%3Bi%3A1%3Bs%3A1%3A%222%22%3B%7D',
                            'xd': 'ff8cc2c663e498cf1fffa3d89aaa8ae9f68a128de39a6036c46ec0a0ff0b9459a%3A2%3A%7Bi%3A0%3Bs%3A2%3A%22xd%22%3Bi%3A1%3Bs%3A1%3A%221%22%3B%7D',
                            '_identity': 'd34e780a83bd0292844ae357a1319cd91eff1975274782715adfa3d5215ff63da%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A50%3A%22%5B1285670%2C%22090bb7b982259bff57e00f8d3e62b8da%22%2C86400%5D%22%3B%7D',
                            'Hm_lvt_6de0a5b2c05e49d1c850edca0c13051f': '1515665121',
                            'Hm_lpvt_6de0a5b2c05e49d1c850edca0c13051f': '1515665190'}
        self.hearders = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Connection': 'keep - alive',
            # 'Referer': 'http://www.zujuan.com/question /index?chid = 3 & xd = 1',
            'User-Agent': user_agent
        }
        self.domain = 'http://www.zujuan.com'

    # @classmethod
    # def from_crawler(cls, crawler, *args, **kwargs):
    #     # print('boolean === redis ===%s'%kwargs[KEY_REDIS_IS_EXEC] =='1')
    #     # GJ:切换目录到 scrapy 项目这边，这样才能让scraoy runspider的时候找到项目
    #     print('*' * 60)
    #     print('dir is {}'.format(os.getcwd()))
    #     # os.chdir('/opt/azkaban/scripts/hfbank_hfwebcrawler/python')
    #     print('dir is {}'.format(os.getcwd()))
    #     print('project is ==={}'.format(dict(get_project_settings())['BOT_NAME']))
    #     print('*' * 60)
    #
    #     # sets = Settings()
    #     sets = get_project_settings()
    #     # sets = crawler.settings
    #     # GJ：scrapy_redis 配置
    #     # sets.set('REDIS_URL','redis://root:password@redis.local:6379')
    #     # ERIC: sets.set('REDIS_URL','redis://root:password@redis.local:6379')
    #     sets.set('REDIS_URL', 'redis://redis.local:6379')
    #     # GJ:如果是tieba爬虫的话，则跳过模拟浏览器头
    #     if crawler.spidercls.name == 'tieba_spider':
    #         sets.set(
    #             'DOWNLOADER_MIDDLEWARES', {
    #                 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 400,
    #                 'hfdata.middlewares.RandomUserAgent': None,
    #             }
    #         )
    #     if kwargs.get(KEY_REDIS_IS_EXEC, '') and int(kwargs[KEY_REDIS_IS_EXEC]) == 1:
    #         # ERIC:    sets.set('PROXY','10.3.63.1:8080')
    #         # ERIC:    sets.set('DOWNLOADER_MIDDLEWARES','{"hfdata.middlewares.ProxyMiddleware": 100}')
    #         sets.set('DUPEFILTER_CLASS', 'scrapy_redis.dupefilter.RFPDupeFilter')
    #         sets.set('SCHEDULER', 'scrapy_redis.scheduler.Scheduler')
    #         # ERIC:    sets.set('REDIS_URL','redis://root:password@redis.local:6379')
    #         sets.set('REDIS_URL', 'redis://redis.local:6379')
    #     crawler.settings = sets
    #     print('*' * 60)
    #     print('project is ==={}'.format(dict(crawler.settings)['BOT_NAME']))
    #     print('*' * 60)
    #     spider = super(BaseRedisCrawlSpider, cls).from_crawler(crawler, *args, **kwargs)
    #     crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
    #     return spider

    # def spider_closed(self, spider):
    #     clien = MongoClient('mongodb://172.17.0.1')['tmp']['spider_status']
    #     run_time = self.crawler.stats._stats['finish_time'] - self.crawler.stats._stats['start_time']
    #     clien.insert_one({
    #         'item_scraped_count': self.crawler.stats._stats.get('item_scraped_count', 0),
    #         'spider_name': spider.name,
    #         'run_time': run_time.microseconds,
    #         'sub_site': self.meta.get('sub_site'),
    #         'website': self.meta.get('website'),
    #         'site_name': self.meta.get('site_name'),
    #         'today': datetime.today().strftime('%Y-%m-%d')
    #     })
    def start_requests(self):
        start_url = 'http://www.zujuan.com/question/index?chid=2&xd=1'
        return [Request(url=start_url,cookies=self.cookieValue,headers=self.hearders,callback=self.parse_version)]
    def parse_version(self,response):
        result = response.body.decode()
        resu = Selector(text=result)
        versionTexts = resu.xpath('//div[@class="type-items"][1]/div/div/div/a/text()').extract()
        versionUrls = resu.xpath('//div[@class="type-items"][1]/div/div/div/a/@href').extract()
        version = dict(zip(versionTexts, versionUrls))
        print(version)#{'人教版': '/question?bookversion=11740&chid=3&xd=1', '青岛版六三制': '/question?bookversion=23087&chid=3&xd=1', '北师大版': '/question?bookversion=23313&chid=3&xd=1', '苏教版': '/question?bookversion=25571&chid=3&xd=1', '西师大版': '/question?bookversion=47500&chid=3&xd=1', '青岛版五四制': '/question?bookversion=70885&chid=3&xd=1', '浙教版': '/question?bookversion=106060&chid=3&xd=1'}
        #下次请求需要的url:http://www.zujuan.com/question?bookversion=13132&chid=2&xd=1需要的请求:
        for text in version :
            if ('苏教' in text):
                manURL =self.domain+version[text]#http://www.zujuan.com/question?bookversion=25571&chid=3&xd=1
                deliver_param = {'version':'苏教版'}
                deliver_param['course'] = '语文'
                return [Request(url=manURL, meta=deliver_param,cookies=self.cookieValue, headers=self.hearders,callback=self.parse_categories)]
            elif('沪教' in text):
                manURL = self.domain + version[text]  # http://www.zujuan.com/question?bookversion=25571&chid=3&xd=1
                deliver_param = {'version': '沪教版'}
                deliver_param['course'] = '语文'
                return [Request(url=manURL,meta=deliver_param, cookies=self.cookieValue, headers=self.hearders,
                                callback=self.parse_categories)]
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
        #下次请求需要的url:http://www.zujuan.com/question?categories=13133&bookversion=13132&nianji=13133&chid=2&xd=1
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

        with open('d:\\xiti10001\\zujuan\\{0}\\{1}\\categories_yuwen_{0}.txt'.format(time.strftime('%Y%m%d',time.localtime(time.time())),self.file_name),'a') as f:
            f.write(need_sections_str)
            f.write('\n')



    def make_file(self):
        path = 'd:\\xiti10001\\zujuan\\{0}\\{1}\\'.format(time.strftime('%Y%m%d',time.localtime(time.time())),self.file_name)
        isExists = os.path.exists(path)
        if (isExists):
            pass;
        else:
            os.makedirs(path)











