# coding:utf-8
from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from fake_useragent import UserAgent
from ..common.BaseObject import BaseObject
from ..items import XitiloadItem
import requests
import json
import time
import re
import os


class Spider_comment_text(CrawlSpider,BaseObject):
    name = "yitiku_middle_wuli_data"

    def __init__(self):
        ua = UserAgent()
        user_agent = ua.random
        self.cookie = {'PHPSESSID': 'fau6dd44mhejvkjfr92i1fhlo7', 'pgv_pvi': '124541952', 'pgv_si': 's7548876800', 'IESESSION': 'alive', '_qddamta_800024201': '3-0', 'tencentSig': '4229086208', 'jiami_userid': 'Njk0MjM1fDc1M2E1YmRhNTFmZTAwYWRkOGJmY2VhY2IxYTZjMDQ3', 'account': '15221053927', 'password': 'MTIzNDU2', 'ytkuser': '%7B%22id%22%3A%22694235%22%2C%22deadline%22%3A%220%22%2C%22feature%22%3A%22830c55fad29e4e8fd0b2ced7de7d0c9c%22%7D', 'Hm_lvt_ba430f404e1018c19017fd7d6857af83': '1516957359', 'Hm_lpvt_ba430f404e1018c19017fd7d6857af83': '1516957415', '_qddaz': 'QD.9eu0y.rt4n5d.jcvp8u6k', '_qdda': '3-1.1', '_qddab': '3-pm0igx.jcvp8u6n'}
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
            'Host': 'www.yitiku.cn',
            'Connection': 'keep-alive'

        }
        self.Picture_headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
        }
        self.diffultDegree = {'1.00-0.86': '容易', '0.85-0.71': '较易', '0.70-0.56': '中等', '0.55-0.41': '较难',
                              '0.40-0.26': '困难'}
        self.main_url = 'http://www.yitiku.cn'
        self.Parampath = 'D:\\xiti10001\\yitiku\\{0}\\categories_param\\'.format(time.strftime('%Y%m%d', time.localtime()))
    def start_requests(self):
        filesSet = os.walk(self.Parampath)
        for rt, dirs, files in filesSet:
            if dirs == []:
                if 'wuli' in rt:
                    perFile = os.path.join(rt, files[0])
                    with open(perFile, 'r') as f:
                        needStr = f.read()
                        needDict = needStr.split('\n')[:-1]
                        print(type(needDict), needDict)
                        try:
                            for perXueQi in needDict:
                                perXueQiParamDict = eval(perXueQi)
                                print(perXueQiParamDict)
                                # 取出总章节参数
                                zhangjies = perXueQiParamDict['section']
                                print('章节类型', type(zhangjies), zhangjies)
                                # for循环取出每章中的小的章节，请求，获得请求后的详情页做解析详情页的数据
                                for perzhangjie in zhangjies.keys():
                                    print('每章的名字：', perzhangjie)
                                    perAllComment = zhangjies[perzhangjie]
                                    print('每章的全部内容：', perAllComment)
                                    for perComment in perAllComment.keys():
                                        perUrl = perAllComment[perComment]
                                        print('每小节的url', perUrl)
                                        requestUrl = self.main_url + perUrl
                                        perXueQiParamDict['currentSection'] = perzhangjie
                                        perXueQiParamDict['currentSmallSection'] = perComment
                                        perXueQiParamDict['main_url'] = requestUrl
                                        yield Request(url=requestUrl, headers=self.headers, meta=perXueQiParamDict,callback=self.param_page)
                        except Exception as e:
                            print(e)
                            self.error(repr(e))
    def param_page(self, response):
        try:
            try:
                comment = response.body.decode()
            except:
                comment = response.body.decode('gbk')
            if '下一页' not in comment:
                print('没有数据')
                pass
            else:
                self.param_detail(response)
                a = Selector(text=comment)
                aTextS = a.xpath('//div[@class="page"]/a/text()').extract()
                if (len(aTextS)) != 0:
                    biaoJi = a.xpath('//div[@class="page"]/a[last()]/text()').extract_first()
                    if biaoJi =="下一页":
                        page = a.xpath('//div[@class="page"]/a[last()-1]/text()').extract_first()
                        print(type(page), page)
                        time.sleep(20)
                        page = int(page)
                        if page > 3 :
                            for perpage in range(2, 4):
                                # http://www.yitiku.cn/tiku/tbsx/banben/8886/tb_tixing/1/jid/8910?page=2
                                mainUrl1 = response.meta['main_url']
                                requestUrl = mainUrl1 + '?page={}'.format(perpage)
                                yield Request(url=requestUrl,meta=response.meta, headers=self.headers, cookies=self.cookie, callback=self.param_detail)
                        else:
                            for perpage in range(2, page + 1):
                                # http://www.yitiku.cn/tiku/tbsx/banben/8886/tb_tixing/1/jid/8910?page=2
                                mainUrl1 = response.meta['main_url']
                                requestUrl = mainUrl1 + '?page={}'.format(perpage)
                                yield Request(url=requestUrl,meta=response.meta, headers=self.headers, cookies=self.cookie, callback=self.param_detail)
                    else:
                        self.param_detail(response)
                else:
                    pass
        except Exception as e:
            # print(e)
            self.error(repr(e))
    def param_detail(self,response):
        try:
            try:
                comment = response.body.decode()
            except:
                comment = response.body.decode('gbk')
            a = Selector(text=comment)
            allDetailUrl = a.xpath('//li[@class="icon5"]/a/@href').extract()
            # print('123详情页的url;', allDetailUrl)
            # 详情url
            # http://www.yitiku.cn/shiti/872851.html/
            for perDetailUrl in allDetailUrl:
                requestUrl = self.main_url + perDetailUrl
                response.meta['request_Url'] = requestUrl
                yield Request(url=requestUrl, headers=self.headers, meta=response.meta, cookies=self.cookie,
                              callback=self.param_detail_comment)
        except Exception as e:
            print(repr(e))
    def param_detail_comment(self, response):
        try:
            items = XitiloadItem()
            items['version'] = 'None'  # 版本
            items['grade'] = 'None'  # 年级
            items['course'] = 'None'  # 学科
            items['section'] = 'None'  # 章节
            items['type'] = 'None'  # 题型
            items['title'] = 'None'  # 题目
            items['originalTitleUrl'] = 'None'  # 题目中的原始url
            items['selects'] = 'None'  # 选项
            items['originaSelectsUrl'] = 'None'  # 选项的原始url
            items['answer'] = 'None'  # 答案
            items['originaAnswerUrl'] = 'None'  # 答案的原始url
            items['knowledgePoint'] = 'None'  # 知识点
            items['originaKnowledgePoint'] = 'None'  # 知识点的原始url
            items['analysis'] = 'None'  # 解析
            items['originaAnalysisUrl'] = 'None'
            items['detailUrl'] = 'None'  # 详情页的URL
            items['difficultDEgree'] = 'None'  # 试题的难易程度

            items['version'] = response.meta['versions']
            items['course'] = response.meta['course']
            items['grade'] = response.meta['grade']
            items['section'] = response.meta['currentSection']
            items['section_child'] = response.meta['currentSmallSection']
            items['type'] = response.meta['tixing']
            try:
                comment = response.body.decode()
            except:
                comment = response.body.decode('gbk')

            # print('请求详情页的url：',response.meta['request_Url'])
            try:
                comment = re.findall(r'<strong>试题详情</strong></div><div class="clear"></div></div></div>(.*)#footerpanel', comment)[0]
            except:
                time.sleep(5)
                comment = re.findall(r'<strong>试题详情</strong></div><div class="clear"></div></div></div>(.*)#footerpanel', comment)[0]

            # print('解析到的数据：', comment)
            a = Selector(text=comment)
            timu = a.xpath('//h1/img/@src').extract_first()
            res = self.load_Picture(timu, 'title')
            # print('加载图片返回的数据',type(res),res)
            items['title'] = res[0]
            items['originalTitleUrl'] = res[1]
            nanduxishu = a.xpath('//u[1]/i/text()').extract_first()
            items['difficultDEgree'] = self.diffultDegree.get(nanduxishu)
            kaodian = a.xpath('//ul[1]/li/div/a/text()').extract_first()
            kaodianTuple = self.load_Picture(kaodian, 'knowledgePoint')
            items['knowledgePoint'] = kaodianTuple[0]
            items['originaKnowledgePoint'] = kaodianTuple[1]
            shitijiexi = a.xpath('//ul[2]/li[1]/div').extract_first()
            # print(shitijiexi)

            jiexiTuple = self.load_Picture(shitijiexi, 'analysis')
            items['analysis'] = jiexiTuple[0]
            items['originaAnalysisUrl'] = jiexiTuple[1]
            # print(jiexiTuple)

            daan = a.xpath('//ul[2]/li[2]/b').extract_first()
            daanTuple = self.load_Picture(daan, 'answer')
            items['answer'] = daanTuple[0]
            items['originaAnswerUrl'] = daanTuple[1]  # 答案的原始url
            # print(timu, 123, nanduxishu, 123, kaodian, 123, '答案解析;', shitijiexi, 123, daan)
            if items['originaKnowledgePoint'] != "None" or items['originaAnswerUrl'] != "None":
                self.saveSpecialItem(items)
            else:
                yield items
        except Exception as e:
            self.error(repr(e))
            # print(repr(e))

    def load_Picture(self, url, fileName):
        try:
            TYSavePath = 'http://res.oitor.com:8089/upload/'
            pa = 'D:\\xiti10001\\SpecialPicture\\{}\\'.format(time.strftime('%Y%m%d', time.localtime()))
            isEixct = os.path.exists(pa)
            if fileName =='knowledgePoint' or fileName =='answer':
                pa = 'D:\\xiti10001\\yitikuSpecial123Picture\\{}\\'.format(time.strftime('%Y%m%d', time.localtime()))

            if isEixct:
                pass
            else:
                os.makedirs(pa)
            if (isinstance(url, str)):
                if (url.startswith('http://') or url.startswith('https://')):
                    path = pa + 'picture_{0}_{1}_{2}.png'.format(fileName,
                                                                 time.strftime("%Y%m%d", time.localtime()),
                                                                 str(int((time.time()) * 1000)))
                    picture = requests.get(url=url, headers=self.Picture_headers)
                    with open(path, 'wb')as f:
                        f.write(picture.content)
                    geshihua = path[3:].replace('\\', '/')
                    savePath = TYSavePath + geshihua
                    result = (savePath, url)
                    return result
                elif ('<img' in url):
                    srcLIst = []
                    imgs = Selector(text=url).xpath('//img/@src').extract()
                    for x in imgs:
                        if (x.startswith('http://') or x.startswith('https://')):
                            path = pa + 'picture_{0}_{1}_{2}.png'.format(fileName,
                                                                         time.strftime("%Y%m%d", time.localtime()),
                                                                         str(int((time.time()) * 1000)))
                            picture = requests.get(url=x, headers=self.headers)
                            with open(path, 'wb')as f:
                                f.write(picture.content)
                            geshihua = path[3:].replace('\\', '/')
                            savePath = TYSavePath + geshihua
                            # print(type(x), x, type(savePath), savePath)
                            url = url.replace(x, savePath)
                            srcLIst.append(x)
                        else:
                            path = pa + 'picture_{0}_{1}_{2}.png'.format(fileName,
                                                                         time.strftime("%Y%m%d", time.localtime()),
                                                                         str(int((time.time()) * 1000)))
                            requestUrl = self.main_url + x
                            picture = requests.get(url=requestUrl, headers=self.headers)
                            with open(path, 'wb')as f:
                                f.write(picture.content)
                            geshihua = path[3:].replace('\\', '/')
                            savePath = TYSavePath + geshihua
                            # print(type(x), x, type(savePath), savePath)
                            url = url.replace(x, savePath)
                            srcLIst.append(requestUrl)


                    if len(srcLIst) == 0:
                        result = (url, 'None')
                        return result
                    else:
                        result = (url, str(srcLIst))
                        return result


                else:
                    res = re.findall(r'<(.*)>(.*)<(.*)>(.*)</(.*)>', url)
                    if res:
                        return (url, 'None')
                    else:
                        url = Selector(text=url).xpath('//text()').extract_first()
                        return (url, 'None')
            else:
                result = (str(url), 'None')
                return result
        except Exception as e:
            self.error(repr(e))
            # print(e)
    def saveSpecialItem(self,item):
        try:
            path = 'D:\\xiti10001\\specialData\\{}\\'.format(time.strftime("%Y%m%d", time.localtime()))
            # path = 'd:\\OITData\\zujuan\\{0}\\{1}\\'.format(time.strftime("%Y%m%d", time.localtime()), spider.name)
            isExists = os.path.exists(path)
            if isExists:
                pass
            else:
                os.makedirs(path)
            with open(path + self.name + '.json', 'a', encoding='utf-8')as f:
                lines = json.dumps(dict(item), ensure_ascii=False)
                f.write(lines)
                f.write('\n')
        except Exception as e:
            self.error(e)
            # print(e)
