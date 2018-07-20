#coding:utf-8
from scrapy.spiders import CrawlSpider
from fake_useragent import UserAgent
from scrapy.selector import Selector
from scrapy.http import Request
import json
import time
import os
import re

class SpiderMath(CrawlSpider):
    name = 'yiTiKu_param'
    custom_settings = {
        'ITEM_PIPELINES': {'OIT_21cnjy_Param.pipelines.Oyt21CnjyParamPipeline': None, }



    }
    def __init__(self):
        ua = UserAgent()
        user_agent = ua.random
        self.cookie = {'pgv_pvi': '8869029888', 'tencentSig': '8349357056', 'PHPSESSID': '21rbna3k500ic89ga8qjmqhjs3', 'pgv_si': 's8352073728', 'IESESSION': 'alive', '_qddamta_800024201': '3-0', 'jiami_userid': 'NjkzMzE0fDk1NzM5YmM5MzIwYjY1ZmViZmE3NDQ3ZmVkY2E4NTY3', 'account': '18621942417', 'password': 'MTIzNDU2', 'ytkuser': '%7B%22id%22%3A%22693314%22%2C%22deadline%22%3A%220%22%2C%22feature%22%3A%22f5ee54afd56eef93b9db72a134881074%22%7D', '_qddaz': 'QD.s08ddj.bmtxtt.jcbcp2wi', '_qdda': '3-1.1', '_qddab': '3-se1uzy.jcslbnnd', 'Hm_lvt_ba430f404e1018c19017fd7d6857af83': '1515726959,1516586108,1516605643,1516759114', 'Hm_lpvt_ba430f404e1018c19017fd7d6857af83': '1516769535'}
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'User-Agent': user_agent,
            'Host': 'www.yitiku.cn',

        }
        self.comment_headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'User-Agent': user_agent,
            'Host': 'www.yitiku.cn',
            # 'cookie':'pgv_pvi=8869029888; tencentSig=8349357056; PHPSESSID=3116tv878og1hj281a5gs2prc3; pgv_si=s5982021632; IESESSION=alive; ytkuser=%7B%22id%22%3A%22693314%22%2C%22deadline%22%3A%220%22%2C%22feature%22%3A%22f5ee54afd56eef93b9db72a134881074%22%7D; _qddamta_800024201=3-0; Hm_lvt_ba430f404e1018c19017fd7d6857af83=1515726959,1516586108,1516605643; Hm_lpvt_ba430f404e1018c19017fd7d6857af83=1516610974; _qddaz=QD.s08ddj.bmtxtt.jcbcp2wi; _qdda=3-1.30biim; _qddab=3-7bpjhv.jcpyfmi7',
            # 'Referer':'https://zujuan.21cnjy.com/'
        }
        self.path = 'D:\\xiti10001\\yitiku\\{0}\\categories_param\\'.format(time.strftime('%Y%m%d',time.localtime()))

        self.main_url = 'http://www.yitiku.cn'
        self.middle = {'语文':'yiTiKu_chinese_middle','数学':'yiTiKu_math_middle','英语':'yiTiKu_english_middle','物理':'yiTiKu_wuli_middle','化学':'yiTiKu_huaxue_middle'}
        self.selectVersion = ['沪教版', '沪教苏科版', '苏科版', '牛津译林新版']
        self.selectTixing = ['单选题','多选题']
    def start_requests(self):
        main_url = 'http://www.yitiku.cn'
        return [Request(url=main_url,headers = self.headers,callback=self.param_subject)]
    def param_subject(self,response):#解析阶段和科目的
        try:
            content = response.body.decode()
        except:
            content = response.body.decode('gbk')
        a = Selector(text=content)
        metaDict = {}
        jieduan = a.xpath('//div[@class="nav"]/ul/li[2]/div/ul[2]/p/text()').extract()
        print(jieduan)
        kemu_list = a.xpath('//div[@class="nav"]/ul/li[2]/div/ul[2]/li/a/text()').extract()
        print(kemu_list)
        kemu_url = a.xpath('//div[@class="nav"]/ul/li[2]/div/ul[2]/li/a/@href').extract()
        kemuUrl = dict(zip(kemu_list,kemu_url))
        print('主科目的url：',kemuUrl)
        deliverUrl = {}
        for perKemuUrl in self.middle.keys():
            if perKemuUrl == '生物':
                per = kemuUrl[perKemuUrl]
                pert = re.findall(r"javascript:abx(.*);", per)
                per = pert[0]
                tupl = eval(per)
                quryString = tupl[0].split('/')
                pinString =quryString[-1]
                postfixUrl = '/' + quryString[-2] + '/' + pinString
                deliverUrl[perKemuUrl] = postfixUrl
            else:
                per = kemuUrl[perKemuUrl]
                pert = re.findall(r"javascript:abx(.*);", per)
                per = pert[0]
                tupl = eval(per)
                quryString = tupl[0].split('/')
                pinString = 'tb' + quryString[-1]
                postfixUrl = '/' + quryString[-2] + '/' + pinString
                deliverUrl[perKemuUrl] = postfixUrl
        print('科目的url：',deliverUrl)
        metaDict['zhuUrl'] =deliverUrl
        for per in deliverUrl:
            #获取科目和主页面的各科的url，请求获取详细信息
            metaDict = {'course':per}#'course': '化学'
            requestUrl =self.main_url+deliverUrl[per]
            address =self.path+self.middle[per]
            metaDict['address']=address
            yield Request(url=requestUrl,headers=self.headers,meta=metaDict,callback=self.parse_version)
    def parse_version(self,response):
        try:
            content = response.body.decode()
        except:
            content = response.body.decode('gbk')
        #获取每个科目下的版本号及url：#'版本': {'人教版': '/tiku/tbhx/banben/10097', '北京课改版': '/tiku/tbhx/banben/17817', '人教版(旧)': '/tiku/tbhx/banben/7053', '鲁教版': '/tiku/tbhx/banben/9419', '沪教版（旧）': '/tiku/tbhx/banben/9900', '粤教版': '/tiku/tbhx/banben/9946', '沪教苏科版': '/tiku/tbhx/banben/18044', '仁爱版': '/tiku/tbhx/banben/18645', '沪教版': '/tiku/tbhx/banben/19673'}, '年级': {'九年级上': '/tiku/tbhx/jid/10098', '九年级下': '/tiku/tbhx/jid/10099'}
        versions = Selector(text=content).xpath('//div[@class="tongbu"]/dl[1]/dt/text()').extract_first()
        versions = versions[:-1]
        versionsTexts = Selector(text=content).xpath('//div[@class="tongbu"]/dl[1]/dd/a/text()').extract()
        versionsUrls = Selector(text=content).xpath('//div[@class="tongbu"]/dl[1]/dd/a/@href').extract()
        versionDict = dict(zip(versionsTexts,versionsUrls))
        for perVersion in self.selectVersion:
            per = versionDict.get(perVersion)
            #http://www.yitiku.cn/tiku/tbyy/banben/7580
            deliverVersion = {}
            deliverVersion[perVersion] =per
            if per:
                requestUrl =self.main_url+per
                # response.meta[versions] =deliverVersion
                response.meta['versions'] = perVersion
                yield Request(url=requestUrl, headers=self.headers, meta=response.meta, callback=self.parse_grade)
    def parse_grade(self,response):
        try:
            content = response.body.decode()
        except:
            content = response.body.decode('gbk')
        #获取每个科目下的年级及url：'年级': {'七年级上': '/tiku/tbyw/jid/17222', '七年级下': '/tiku/tbyw/jid/9984', '八年级上': '/tiku/tbyw/jid/9985', '八年级下': '/tiku/tbyw/jid/9986', '九年级上': '/tiku/tbyw/jid/9987', '九年级下': '/tiku/tbyw/jid/9988'}
        grade = Selector(text=content).xpath('//div[@class="tongbu"]/dl[2]/dt/text()').extract_first()
        grade = grade[:-1]
        gradeTexts = Selector(text=content).xpath('//div[@class="tongbu"]/dl[2]/dd/a/text()').extract()
        gradeUrls = Selector(text=content).xpath('//div[@class="tongbu"]/dl[2]/dd/a/@href').extract()
        gradeDict = dict(zip(gradeTexts, gradeUrls))
        for perGrade in gradeDict.keys():
            deliverGrade = {}
            per = gradeDict[perGrade]
            requestUrl = self.main_url + per
            deliverGrade[perGrade] = per
            # response.meta[grade] = deliverGrade
            response.meta['grade'] = perGrade
            yield Request(url=requestUrl, headers=self.headers, meta=response.meta, callback=self.parse_tixing)
    def parse_tixing(self,response):
        try:
            content = response.body.decode()
        except:
            content = response.body.decode('gbk')
        #获取各科的题型及其url：'题型': {'全部': '/tiku/tbsx', '单选题': '/tiku/tbsx/tb_tixing/1', '解答题': '/tiku/tbsx/tb_tixing/2', '填空题': '/tiku/tbsx/tb_tixing/4', '计算题': '/tiku/tbsx/tb_tixing/5', '证明题': '/tiku/tbsx/tb_tixing/7', '作图题': '/tiku/tbsx/tb_tixing/10', '判断题': '/tiku/tbsx/tb_tixing/12'},
        tixing = Selector(text=content).xpath('//div[@class="choice"]/div[1]/dl/dt/text()').extract_first()
        tixingTexts = Selector(text=content).xpath('//div[@class="choice"]/div[1]/dl/dd/a/text()').extract()
        tixingUrls = Selector(text=content).xpath('//div[@class="choice"]/div[1]/dl/dd/a/@href').extract()
        tixingUrlseDict = dict(zip(tixingTexts, tixingUrls))
        for perTixong in self.selectTixing:
            per = tixingUrlseDict.get(perTixong)
            deliverTixing = {}
            if per:
                requestUrl = self.main_url + per
                deliverTixing[perTixong] = per
                # response.meta[tixing] = deliverTixing
                response.meta['tixing'] = perTixong
                yield Request(url=requestUrl, headers=self.headers, meta=response.meta, callback=self.parse_zhangjie)
    def parse_zhangjie(self,response):
        try:
            content = response.body.decode()
        except:
            content = response.body.decode('gbk')
        # 获取各科试题的难易程度及其url：'难度系数': {'全部': '/tiku/tbsx', '1.00-0.86(容易)': '/tiku/tbsx/nanduxishu/1', '0.85-0.71(较易)': '/tiku/tbsx/nanduxishu/2', '0.70-0.56(中等)': '/tiku/tbsx/nanduxishu/3', '0.55-0.41(较难)': '/tiku/tbsx/nanduxishu/4', '0.40-0.26(困难)': '/tiku/tbsx/nanduxishu/5'},
        difficultDegree = Selector(text=content).xpath('//div[@class="choice"]/div[2]/dl/dt/text()').extract_first()
        difficultDegreeTexts = Selector(text=content).xpath('//div[@class="choice"]/div[2]/dl/dd/a/text()').extract()
        difficultDegreeUrls = Selector(text=content).xpath('//div[@class="choice"]/div[2]/dl/dd/a/@href').extract()
        difficultDegreeUrlseDict = dict(zip(difficultDegreeTexts, difficultDegreeUrls))
        response.meta['difficultDegree'] = difficultDegreeUrlseDict
        #获取章节下小章节的的标题及其URL:'dazhangjieName': '第一单元','xiaozhangjieDict': {'课题1 物质的变化和性质': '/tiku/tbhx/jid/10113', '课题2 化学是一门以实验为基础的科学': '/tiku/tbhx/jid/10114', '课题3 走进化学实验室': '/tiku/tbhx/jid/10115'}
        zhnagjie = Selector(text=content).xpath('//div[@class="leftbottom2"]/ul/li').extract()
        print(len(zhnagjie))
        address = response.meta['address']
        self.make_file(address)
        zhangjieDict = {}
        bigzhangjie = {}
        for per in range(1,len(zhnagjie)+1):
            zhnagjieName = Selector(text=content).xpath('//div[@class="leftbottom2"]/ul/li[{}]/label/a/text()'.format(per)).extract_first()
            zhnagjieUrl = Selector(text=content).xpath('//div[@class="leftbottom2"]/ul/li[{}]/label/a/@href'.format(per)).extract_first()
            print('章节名字：',zhnagjieName)
            xiaozhangjieText = Selector(text=content).xpath('//div[@class="leftbottom2"]/ul/li[{}]/ul/li/label/a/text()'.format(per)).extract()
            xiaozhangjieUrl = Selector(text=content).xpath('//div[@class="leftbottom2"]/ul/li[{}]/ul/li/label/a/@href'.format(per)).extract()
            xiaozhnagjieseDict = dict(zip(xiaozhangjieText, xiaozhangjieUrl))
            zhangjieDict[zhnagjieName] = xiaozhnagjieseDict
            bigzhangjie[zhnagjieName] =zhnagjieUrl
        response.meta['section'] =zhangjieDict
        response.meta['zhnagjie_text_url'] = bigzhangjie
        need_sections_str = str(response.meta)
        with open(address + '\\{}.txt'.format(time.strftime('%Y%m%d', time.localtime())), 'a') as f:
            f.write(need_sections_str)
            f.write('\n')

    def make_file(self, perPath):
        isExists = os.path.exists(perPath)
        if isExists:
            pass
        else:
            os.makedirs(perPath)





