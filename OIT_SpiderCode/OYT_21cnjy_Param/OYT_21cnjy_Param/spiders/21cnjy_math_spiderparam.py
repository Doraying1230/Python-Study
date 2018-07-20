#coding:utf-8
from scrapy.spiders import CrawlSpider
from fake_useragent import UserAgent
from ..common.BaseObject import BaseObject
from scrapy.selector import Selector
from scrapy.http import Request
import time
import os
import re

class SpiderMath(CrawlSpider,BaseObject):
    name = '21cnjy_param'
    custom_settings = {
        'ITEM_PIPELINES': {'OYT_21cnjy_Param.pipelines.Oyt21CnjyParamPipeline': None, }



    }
    def __init__(self):
        ua = UserAgent()
        user_agent = ua.random
        self.headers = {
            'User-Agent':user_agent,
            'Host':'zujuan.21cnjy.com',
            'cookie':'aaaaHqNL_ef65_saltkey=G7Kkkp1p; aaaaHqNL_ef65_lastvisit=1515573337; UM_distinctid=160df6ccd0a1c6-069961f6e93678-454c092b-1aeaa0-160df6ccd0b786; _qddaz=QD.myeb91.xj6lqb.jc8vdlxs; HqNL_ef65_saltkey=rXoG19po; HqNL_ef65_lastvisit=1515573663; Hm_lvt_0280ecaa2722243b1de4829d59602c72=1515576938,1515727104; _csrf=2d53818b4605f7b8927b7ac5697b32f6b891d079a3872e07336d39ef514225fba%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22z7r-pnQhITVpiDOdLvUAfgnNvVCvWu47%22%3B%7D; xd=494a1f745cfdce14dad87288ba1fd45465b7d32eec1df130011fd3cd0b6415c2a%3A2%3A%7Bi%3A0%3Bs%3A2%3A%22xd%22%3Bi%3A1%3Bs%3A1%3A%221%22%3B%7D; aaaaHqNL_ef65_sid=MX23cQ; aaaaHqNL_ef65_lastact=1515738681%09tiku.php%09; Hm_lvt_5d70f3704df08b4bfedf4a7c4fb415ef=1515727909,1515738493,1515738647,1515738704; chid=d79688f1e7866722fd16866f40a252116287a86b4e6e2213e3150af3ba96e038a%3A2%3A%7Bi%3A0%3Bs%3A4%3A%22chid%22%3Bi%3A1%3Bs%3A1%3A%222%22%3B%7D; HqNL_ef65_sid=jrbubn; HqNL_ef65_lastact=1515738789%09index.php%09index; Hm_lpvt_0280ecaa2722243b1de4829d59602c72=1515738790; Hm_lpvt_5d70f3704df08b4bfedf4a7c4fb415ef=1515739187'
        }
        self.comment_headers = {
            'User-Agent': user_agent,
            'Host': 'zujuan.21cnjy.com',
            'cookie': 'aaaaHqNL_ef65_saltkey=G7Kkkp1p; aaaaHqNL_ef65_lastvisit=1515573337; UM_distinctid=160df6ccd0a1c6-069961f6e93678-454c092b-1aeaa0-160df6ccd0b786; _qddaz=QD.myeb91.xj6lqb.jc8vdlxs; HqNL_ef65_saltkey=rXoG19po; HqNL_ef65_lastvisit=1515573663; Hm_lvt_0280ecaa2722243b1de4829d59602c72=1515576938,1515727104; _csrf=2d53818b4605f7b8927b7ac5697b32f6b891d079a3872e07336d39ef514225fba%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22z7r-pnQhITVpiDOdLvUAfgnNvVCvWu47%22%3B%7D; xd=494a1f745cfdce14dad87288ba1fd45465b7d32eec1df130011fd3cd0b6415c2a%3A2%3A%7Bi%3A0%3Bs%3A2%3A%22xd%22%3Bi%3A1%3Bs%3A1%3A%221%22%3B%7D; aaaaHqNL_ef65_sid=MX23cQ; aaaaHqNL_ef65_lastact=1515738681%09tiku.php%09; Hm_lvt_5d70f3704df08b4bfedf4a7c4fb415ef=1515727909,1515738493,1515738647,1515738704; chid=d79688f1e7866722fd16866f40a252116287a86b4e6e2213e3150af3ba96e038a%3A2%3A%7Bi%3A0%3Bs%3A4%3A%22chid%22%3Bi%3A1%3Bs%3A1%3A%222%22%3B%7D; HqNL_ef65_sid=jrbubn; HqNL_ef65_lastact=1515738789%09index.php%09index; Hm_lpvt_0280ecaa2722243b1de4829d59602c72=1515738790; Hm_lpvt_5d70f3704df08b4bfedf4a7c4fb415ef=1515739187',
            'Referer':'https://zujuan.21cnjy.com/'
        }
        self.path = 'D:\\xiti10001\\21cnjy\\{0}\\categories_param\\'.format(time.strftime('%Y%m%d',time.localtime()))


        self.main_url = 'https://zujuan.21cnjy.com'
        self.xiaoXue = {'语文':'yuwen','数学':'shuxue','英语':'yingyu'}
        self.middle = {'语文':'chinese_middle','数学':'math_middle','英语':'english_middle','物理':'wuli_middle','化学':'huaxue_middle'}
    def start_requests(self):
        main_url = 'https://zujuan.21cnjy.com/'
        return [Request(url=main_url,headers = self.headers,callback=self.param_subject)]
    def param_subject(self,response):#解析阶段和科目的
        try:
            content = response.body.decode()
        except:
            content = response.body.decode('gbk')
        commentText = Selector(text=content)
        comment_dict = {}
        for x in range(1,3):
            per_comment_text = commentText.xpath('//div[@class="subject"][{}]/h3/text()'.format(x)).extract_first()
            per_text = commentText.xpath('//div[@class="subject"][{}]/div/ul/li/div/div[@class="subject-list"]/p[@class="list-txt1"]/a/text()'.format(x)).extract()
            per_text = [per.strip() for per in per_text]
            per_url = commentText.xpath('//div[@class="subject"][{}]/div/ul/li/div/div[@class="subject-list"]/p[@class="list-txt2"]/a[1]/@href'.format(x)).extract()
            per_text_url_dict = dict(zip(per_text,per_url))
            comment_dict[per_comment_text] =per_text_url_dict
        print('第一次解析的数据：',comment_dict)
        # {'小学资源导航': {'语文': '/question/index?chid=2&xd=1', '数学': '/question/index?chid=3&xd=1', '英语': '/question/index?chid=4&xd=1', '科学': '/question/index?chid=5&xd=1', '政治思品': '/question/index?chid=9&xd=1'}, '初中资源导航': {'语文': '/question/index?chid=2&xd=2', '数学': '/question/index?chid=3&xd=2', '英语': '/question/index?chid=4&xd=2', '科学': '/question/index?chid=5&xd=2', '物理': '/question/index?chid=6&xd=2', '化学': '/question/index?chid=7&xd=2', '历史': '/question/index?chid=8&xd=2', '政治思品': '/question/index?chid=9&xd=2', '地理': '/question/index?chid=10&xd=2', '历史与社会': '/question/index?chid=20&xd=2', '社会思品': '/question/index?chid=21&xd=2', '生物': '/question/index?chid=11&xd=2'}}
        for perComment in comment_dict:
            if(perComment =='小学资源导航'):
                totleData = comment_dict[perComment]
                for perData in self.xiaoXue:
                    metaData = {}
                    perUrl =self.main_url+totleData[perData]#拼接下次请求获取版本信息的url
                    address = self.path+self.xiaoXue[perData]
                    metaData['jieduan'] = perComment
                    metaData['param'] =address
                    metaData['subject']=perData
                    metaData['biaozhi'] = self.xiaoXue[perData]
                    #发送的url模板：https://zujuan.21cnjy.com/question?bookversion=14929&chid=3&xd=2
                    yield Request(url=perUrl,headers=self.headers,meta=metaData,callback=self.param_version)
            elif(perComment =='初中资源导航'):
                totleData = comment_dict[perComment]
                for perData in self.middle:
                    metaData = {}
                    perUrl = self.main_url + totleData[perData]  # 拼接下次请求获取版本信息的url
                    address = self.path + self.middle[perData]
                    metaData['jieduan'] = perComment
                    metaData['param'] = address
                    metaData['subject'] = perData
                    metaData['biaozhi'] = self.middle[perData]
                    # 发送的url模板：https://zujuan.21cnjy.com/question?bookversion=14929&chid=3&xd=2
                    yield Request(url=perUrl, headers=self.headers, meta=metaData, callback=self.param_version)
            else:
                pass

    def param_version(self,response):#解析版本
        # print(response.meta['param'])

        try:
            content = response.body.decode()
        except:
            content = response.body.decode('gbk')
        conmentText = Selector(text=content)
        bookversion = conmentText.xpath('//div/div[@class="type-items"][1]/div[2]/div/div/a/text()').extract()
        bookversion_url = conmentText.xpath('//div/div[@class="type-items"][1]/div[2]/div/div/a/@href').extract()
        versionComment = dict(zip(bookversion,bookversion_url))
        print(versionComment)
        #{'人教版': '/question?bookversion=11740&chid=3&xd=1', '青岛版六三制': '/question?bookversion=23087&chid=3&xd=1', '北师大版': '/question?bookversion=23313&chid=3&xd=1', '苏教版': '/question?bookversion=25571&chid=3&xd=1', '西师大版': '/question?bookversion=47500&chid=3&xd=1', '沪教版': '/question?bookversion=66214&chid=3&xd=1', '青岛版五四制': '/question?bookversion=70885&chid=3&xd=1', '浙教版': '/question?bookversion=106060&chid=3&xd=1'}
        #https://zujuan.21cnjy.com/question?bookversion=13132&chid=2&xd=1
        metaData = response.meta
        for text in versionComment:
            print(123)
            if ('牛津' in text):
                commentUrl = self.main_url + versionComment[text]
                metaData['version'] =text
                yield Request(url=commentUrl, headers=self.headers, meta=metaData, callback=self.parse_categories)
            # elif('人教' in text):
            #     commentUrl = self.main_url + versionComment[text]
            #     metaData['version'] = text
            #     yield Request(url=commentUrl, headers=self.headers, meta=metaData, callback=self.parse_categories)
            elif('苏教' in text):
                commentUrl = self.main_url + versionComment[text]
                metaData['version'] = text
                yield Request(url=commentUrl, headers=self.headers, meta=metaData, callback=self.parse_categories)
            elif ('沪教' in text):
                commentUrl = self.main_url + versionComment[text]
                metaData['version'] = text
                yield Request(url=commentUrl, headers=self.headers, meta=metaData, callback=self.parse_categories)
            elif('沪科' in text):
                commentUrl = self.main_url + versionComment[text]
                metaData['version'] = text
                yield Request(url=commentUrl, headers=self.headers, meta=metaData, callback=self.parse_categories)
            elif ('苏科' in text):
                commentUrl = self.main_url + versionComment[text]
                metaData['version'] = text
                yield Request(url=commentUrl, headers=self.headers, meta=metaData, callback=self.parse_categories)
            else:
                pass


    def parse_categories(self,response):
        try:
            content = response.body.decode()
        except:
            content = response.body.decode('gbk')
        conmentText = Selector(text=content)
        metaData = response.meta
        bookversion_text= conmentText.xpath('//div/div[@class="type-items"][2]/div[2]/div/div/a/text()').extract()
        bookversion_url = conmentText.xpath('//div/div[@class="type-items"][2]/div[2]/div/div/a/@href').extract()
        bookversion = dict(zip(bookversion_text,bookversion_url))
        print(bookversion)
        #打印的数据：{'一年级上册': '/question?categories=3807&bookversion=11740&nianji=3807&chid=3&xd=1', '一年级下册': '/question?categories=3808&bookversion=11740&nianji=3808&chid=3&xd=1', '二年级上册': '/question?categories=3809&bookversion=11740&nianji=3809&chid=3&xd=1', '二年级下册': '/question?categories=3810&bookversion=11740&nianji=3810&chid=3&xd=1', '三年级上册': '/question?categories=3811&bookversion=11740&nianji=3811&chid=3&xd=1', '三年级下册': '/question?categories=3812&bookversion=11740&nianji=3812&chid=3&xd=1', '四年级上册': '/question?categories=3813&bookversion=11740&nianji=3813&chid=3&xd=1', '四年级下册': '/question?categories=3814&bookversion=11740&nianji=3814&chid=3&xd=1', '五年级上册': '/question?categories=3815&bookversion=11740&nianji=3815&chid=3&xd=1', '五年级下册': '/question?categories=3816&bookversion=11740&nianji=3816&chid=3&xd=1', '六年级上册': '/question?categories=3817&bookversion=11740&nianji=3817&chid=3&xd=1', '六年级下册': '/question?categories=3818&bookversion=11740&nianji=3818&chid=3&xd=1'}
        #下一次请求的url:https://zujuan.21cnjy.com/question?categories=17421&bookversion=17417&nianji=17421&chid=3&xd=2
        for categories in bookversion:
            categoriesUrl = self.main_url+bookversion[categories]
            metaData['nianji'] = categories
            yield Request(url=categoriesUrl, headers=self.headers, meta=metaData, callback=self.parse_categories_content)
    def parse_categories_content(self,response):
        try:
            content = response.body.decode()
        except:
            content = response.body.decode('gbk')
        resu = Selector(text=content)
        sectionsText = resu.xpath('//div[@id="J_Tree"]/div/a/text()').extract()
        sectionsUrl = resu.xpath('//div[@id="J_Tree"]/div/a/@href').extract()
        sections = dict(zip(sectionsText, sectionsUrl))
        print(sections)
        #{'课文 1\r': '/question?categories=128316&tree_type=category&chid=2&xd=1', '课文 2\r': '/question?categories=128317&tree_type=category&chid=2&xd=1', '课文 3\r': '/question?categories=128318&tree_type=category&chid=2&xd=1', '课文 4\r': '/question?categories=128320&tree_type=category&chid=2&xd=1', '课文 5\r': '/question?categories=128321&tree_type=category&chid=2&xd=1', '课文 6\r': '/question?categories=128322&tree_type=category&chid=2&xd=1'}
        address = response.meta['param']
        self.make_file(address)
        sections_Text = []
        sections_number = []
        for text in sections:
            sections_Text.append(text)
            categoriesNumber = sections[text]
            print(type(categoriesNumber), categoriesNumber)
            ret = re.findall(r'categories=(\d*)&', categoriesNumber)
            sections_number.append(ret[0])
            print(123, ret)
            need_sections_dict = dict(zip(sections_Text, sections_number))
            nianji = response.meta['nianji']
            response.meta[nianji] = need_sections_dict
            tixing_text = resu.xpath('//div[@class="tag-conbox"]/div/div/a/text()').extract()
            tixing_logol = resu.xpath('///div[@class="tag-conbox"]/div/div/a/@data-value').extract()
            tixing = dict(zip(tixing_text,tixing_logol))
            response.meta['tixing'] = tixing
            need_sections_str = str(response.meta)
        with open(address+'\\{}.txt'.format(time.strftime('%Y%m%d',time.localtime())),'a') as f:
            f.write(need_sections_str)
            f.write('\n')
    def make_file(self,perPath):
        isExists = os.path.exists(perPath)
        if isExists:
            pass
        else:
            os.makedirs(perPath)




