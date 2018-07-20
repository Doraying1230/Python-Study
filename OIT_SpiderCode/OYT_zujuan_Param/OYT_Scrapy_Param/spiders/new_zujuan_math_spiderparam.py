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
    name = 'zujuan_math_param'
    custom_settings = {
        'DOWNLOAD_DELAY': 3, 'CONCURRENT_REQUESTS_PER_IP': 5,
        'ITEM_PIPELINES': {'OIT_ScrapyData.pipelines.OitScrapydataPipeline': None, }

    }
    def __init__(self):
        ua = UserAgent()
        user_agent = ua.random
        self.file_name='zujuan_math_param'
        self.cookieValue = {'chid': 'edb26e513d9f6c5b27f481f2930c0f29b22e216a8813fde3b300c0c1883d7d9ba%3A2%3A%7Bi%3A0%3Bs%3A4%3A%22chid%22%3Bi%3A1%3Bi%3A3%3B%7D',
                            'isdialog': 'bad3c21672f08107d1d921526d191f58bd47d79e7dbb432bd32624a836b42e85a%3A2%3A%7Bi%3A0%3Bs%3A8%3A%22isdialog%22%3Bi%3A1%3Bs%3A4%3A%22show%22%3B%7D',
                            '_csrf': '7df64cd6bf0f3eea0a565874bc08c7d2321c568be803903967d1f8768051c79ca%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22FA6JlxwVnh_xuBRKn8aG7jDLRCVAP_Xl%22%3B%7D',
                            'Hm_lvt_6de0a5b2c05e49d1c850edca0c13051f': '1515133822,1515475032,1515569874,1515662142',
                            'device': '310bdaba05b30bb632f66fde9bf3e2b91ebc4d607c250c2e1a1d9e0dfb900f01a%3A2%3A%7Bi%3A0%3Bs%3A6%3A%22device%22%3Bi%3A1%3BN%3B%7D',
                            '_sync_login_identity': '7ad94290c81be7c912e6aa8e6ceae29fbd1883b33974bb380d2bf4d7c7dc9668a%3A2%3A%7Bi%3A0%3Bs%3A20%3A%22_sync_login_identity%22%3Bi%3A1%3Bs%3A50%3A%22%5B1236869%2C%22hg0WmUhfJqDitwbged_BMDDusbx8W6e9%22%2C86400%5D%22%3B%7D',
                            'PHPSESSID': 'bb6lv6bc5psbdusj5ll7bao3d7',
                            '_identity': '38baa4575a924f6b01dda1e6db5dd586570752de75750f192152ef78340ab60aa%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A50%3A%22%5B1236869%2C%226b852f961c7ce98b76b353ad3d1190df%22%2C86400%5D%22%3B%7D',
                            'xd': 'ff8cc2c663e498cf1fffa3d89aaa8ae9f68a128de39a6036c46ec0a0ff0b9459a%3A2%3A%7Bi%3A0%3Bs%3A2%3A%22xd%22%3Bi%3A1%3Bs%3A1%3A%221%22%3B%7D',
                            'Hm_lpvt_6de0a5b2c05e49d1c850edca0c13051f': '1515662209'}
        self.hearders = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Connection': 'keep - alive',
            # 'Referer': 'http://www.zujuan.com/question /index?chid = 3 & xd = 1',
            'User-Agent': user_agent
        }
        self.domain = 'http://www.zujuan.com'
    def start_requests(self):
        start_url = 'http://www.zujuan.com/question/index?chid=3&xd=1'
        return [Request(url=start_url,cookies=self.cookieValue,headers=self.hearders,callback=self.parse_version)]
    def parse_version(self,response):
        result = response.body.decode()
        resu = Selector(text=result)
        versionTexts = resu.xpath('//div[@class="type-items"][1]/div/div/div/a/text()').extract()
        versionUrls = resu.xpath('//div[@class="type-items"][1]/div/div/div/a/@href').extract()
        version = dict(zip(versionTexts, versionUrls))
        print(version)#{'人教版': '/question?bookversion=11740&chid=3&xd=1', '青岛版六三制': '/question?bookversion=23087&chid=3&xd=1', '北师大版': '/question?bookversion=23313&chid=3&xd=1', '苏教版': '/question?bookversion=25571&chid=3&xd=1', '西师大版': '/question?bookversion=47500&chid=3&xd=1', '青岛版五四制': '/question?bookversion=70885&chid=3&xd=1', '浙教版': '/question?bookversion=106060&chid=3&xd=1'}
        for text in version :
            if ('苏教' in text):
                manURL =self.domain+version[text]#http://www.zujuan.com/question?bookversion=25571&chid=3&xd=1
                deliver_param = {'version':'苏教版'}
                deliver_param['course'] = '数学'
                return [Request(url=manURL, meta=deliver_param,cookies=self.cookieValue, headers=self.hearders,callback=self.parse_categories)]
            elif('沪教' in text):
                manURL = self.domain + version[text]  # http://www.zujuan.com/question?bookversion=25571&chid=3&xd=1
                deliver_param = {'version': '沪教版'}
                deliver_param['course'] = '数学'
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

        with open('d:\\xiti10001\\zujuan\\{0}\\{1}\\categories_math_{0}.txt'.format(time.strftime('%Y%m%d',time.localtime(time.time())),self.file_name),'a') as f:
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



        # questionTypeText = resu.xpath('//div[@class="tag-items"][1]/div/div/div/a/text()').extract()
        # questionTypeUrl = resu.xpath('//div[@class="tag-items"][1]/div/div/div/a/@data-value').extract()
        # questionType = dict(zip(questionTypeText, questionTypeUrl))
        # print(questionType)

        #http://www.zujuan.com/question/list?categories=93263&question_channel_type=1&difficult_index=&exam_type=&kid_num=&grade_id%5B%5D=0&grade_id%5B%5D=1&grade_id%5B%5D=2&grade_id%5B%5D=3&grade_id%5B%5D=4&grade_id%5B%5D=5&grade_id%5B%5D=6&sortField=time&page=2&_=1514887846715
        # print(questionType)#{'全部': '', '单选题': '1', '多选题': '2', '判断题': '3', '填空题': '4', '计算题': '5', '解答题': '6', '作图题': '25', '综合题': '28', '应用题': '36'}
        #
        # 'http: // www.zujuan.com / question?categories = 25576 & bookversion = 25571 & nianji = 25576 & chid = 3 & xd = 1'
#

#http://www.zujuan.com/question/list?categories=25601&question_channel_type=1&difficult_index=&exam_type=&kid_num=&grade_id%5B%5D=0&grade_id%5B%5D=1&grade_id%5B%5D=2&grade_id%5B%5D=3&grade_id%5B%5D=4&grade_id%5B%5D=5&grade_id%5B%5D=6&sortField=time&page=1&_=1514888347731
        # {'第一单元《数一数》': '/question?categories=25601&tree_type=category&chid=3&xd=1',
        #  '第二单元《比一比》': '/question?categories=25602&tree_type=category&chid=3&xd=1',
        #  '第三单元《分一分》': '/question?categories=25603&tree_type=category&chid=3&xd=1',
        #  '第四单元《认位置》': '/question?categories=25604&tree_type=category&chid=3&xd=1',
        #  '第五单元 《认识10以内的数》': '/question?categories=25605&tree_type=category&chid=3&xd=1',
        #  '第六单元  《认识图形（一）》': '/question?categories=25606&tree_type=category&chid=3&xd=1',
        #  '有趣的拼搭': '/question?categories=77679&tree_type=category&chid=3&xd=1',
        #  '第七单元《分与合》': '/question?categories=25607&tree_type=category&chid=3&xd=1',
        #  '第八单元  《10以内的加法和减法》': '/question?categories=25608&tree_type=category&chid=3&xd=1',
        #  '丰收的果园': '/question?categories=77680&tree_type=category&chid=3&xd=1',
        #  '第九单元 《认识11-20各数》': '/question?categories=25610&tree_type=category&chid=3&xd=1',
        #  '第十单元 《20以内的进位加法》': '/question?categories=77681&tree_type=category&chid=3&xd=1'}









