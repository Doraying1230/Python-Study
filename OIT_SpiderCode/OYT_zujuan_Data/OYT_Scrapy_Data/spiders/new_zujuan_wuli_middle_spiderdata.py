# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request,FormRequest
from ..items import XitiloadItem
import urllib.request as  loadRequest
from ..common.BaseObject import BaseObject
from scrapy.selector import Selector
from fake_useragent import UserAgent
import json
import random
import time
import re
import os

class NewZijuanSpiderdataSpider(CrawlSpider,BaseObject):
    name = 'zujuan_wuli_middle_data'
    custom_settings = {
        'DOWNLOAD_DELAY': 3, 'CONCURRENT_REQUESTS_PER_IP': 5
    }
    def __init__(self):
        self.B = 10
        self.difficult_indexs = {'1': "容易", '2': "较易", '3': "普通", '4': "较难", '5': "困难"}
        ua = UserAgent()
        user_agent = ua.random
        self.filename = 'zujuan_wuli_middle_data'
        self.new_cookieVule = {'xd': '75519cb9f2bf90d001c0560f5c40520062a60ada9cb38350078f83e04ee38a31a%3A2%3A%7Bi%3A0%3Bs%3A2%3A%22xd%22%3Bi%3A1%3Bi%3A2%3B%7D',
                            'isdialog': 'bad3c21672f08107d1d921526d191f58bd47d79e7dbb432bd32624a836b42e85a%3A2%3A%7Bi%3A0%3Bs%3A8%3A%22isdialog%22%3Bi%3A1%3Bs%3A4%3A%22show%22%3B%7D',
                            '_csrf': 'a95e39e03cb45995e77a612059a9f24536e9f6961aeeba5b2bf8298acf875272a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22GbclAK_1W5JeGM_UOgjwIZQ4UGl3Qxq6%22%3B%7D',
                            'Hm_lvt_6de0a5b2c05e49d1c850edca0c13051f': '1515665792',
                            'device': '310bdaba05b30bb632f66fde9bf3e2b91ebc4d607c250c2e1a1d9e0dfb900f01a%3A2%3A%7Bi%3A0%3Bs%3A6%3A%22device%22%3Bi%3A1%3BN%3B%7D',
                            '_sync_login_identity': 'fa60465dad358e9c08d242aa05fb1795bb842657ab5fdf3a3f96bbaf138de6aba%3A2%3A%7Bi%3A0%3Bs%3A20%3A%22_sync_login_identity%22%3Bi%3A1%3Bs%3A50%3A%22%5B1276281%2C%22_G1JoJxH2ZHyneR57FviHxOFlwYdQ1ax%22%2C86400%5D%22%3B%7D',
                            'PHPSESSID': 'oamjo3f8lks47j6uisnn014rn1',
                            '_identity': 'fd7731d4c59ca01dbade34a90e316e7acea1147906a7fafd3652ae45fdf4e923a%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A50%3A%22%5B1276281%2C%22e6cd2529cd2a07f23dd22aa5511f08c5%22%2C86400%5D%22%3B%7D',
                            'chid': 'cfb34d37b40eefc2ccbe518532b4834f2a7aa0aa8db56dff2d2fd9a9a5c919dda%3A2%3A%7Bi%3A0%3Bs%3A4%3A%22chid%22%3Bi%3A1%3Bs%3A1%3A%226%22%3B%7D',
                            'Hm_lpvt_6de0a5b2c05e49d1c850edca0c13051f': '1515666114'}
        self.hearders = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Connection': 'keep - alive',
           #  'Host': 'www.zujuan.com',
           #  'X - Requested - With': 'XMLHttpRequest',
           #  'Referer': 'http: // www.zujuan.com / question?categories = 25577 & bookversion = 25571 & nianji = 25577 & chid = 3 & xd = 1',
           #  # 'Referer': 'http://www.zujuan.com/question /index?chid = 3 & xd = 1',
           # 'X - CSRF - Token': 'K2APCiSykxJ7KHdNIAJH9vS2IQejWL8oHfZAKSR97XJzATY7SefnQT9yI39DSxavvsQZS - 4f501wgS1lbSWFIg ==',
            'User-Agent': user_agent
        }
    #测试cookie值是否有效用
    # def start_requests(self):
    #     url = 'http://www.zujuan.com/question/detail-5981325.shtml'
    #     return [Request(url=url,headers=self.hearders,cookies=self.new_cookieVule,callback=self.parse_content)]
    # def parse_content(self,response):
    #
    #     # version = Field();  # 版本
    #     # grade = Field();  # 年级
    #     # course = Field();  # 学科
    #     # section = Field()  # 章节
    #     # title = Field()  # 题目
    #     # answer = Field()  # 答案
    #     # knowledgePoint = Field()  # 知识点
    #     # analysis = Field()  # 解析
    #
    #
    #     items = XitiloadItem()
    #     print(response.status)
    #     content = response.body.decode()
    #     queryContent = re.findall(r' var MockDataTestPaper = \[(.+)\]', content)[0]
    #     queryContentDict = json.loads(queryContent)
    #     queryQuestionsDict = queryContentDict['questions'][0]
    #     title = queryQuestionsDict['question_text']
    #     savePath = self.load_picture(title, 'title')
    #     items['title'] = savePath[0]
    #     items['originalTitleUrl'] = savePath[1]
    #     explanation = queryQuestionsDict['explanation']
    #     savePath = self.load_picture(explanation, 'explanation')
    #     items['analysis'] = savePath[0]
    #     items['originaAnalysisUrl'] = savePath[1]
    #     options = queryQuestionsDict['options']
    #     savePath = self.load_picture(options, 'options')
    #     items['selects'] = savePath[0]
    #     items['originaSelectsUrl'] = savePath[1]
    #     knowledge = queryQuestionsDict['knowledge']
    #     savePath = self.load_picture(knowledge, 'knowledge')
    #     items['knowledgePoint'] = savePath[0]
    #     items['originaKnowledgePoint'] = savePath[1]
    #     answer = queryQuestionsDict['answer']
    #     savePath = self.load_picture(answer, 'answer')
    #     items['answer'] = savePath[0]
    #     items['originaAnswerUrl'] =savePath[1]
    #     yield items
    #测试用


    def start_requests(self):
        with open('d:\\xiti10001\\zujuan\\{0}\\zujuan_wuli_middle_param\\categories_wuli_{0}.txt'.format(time.strftime('%Y%m%d',time.localtime(time.time())))) as f:
            needStr = f.read()
            needDict = needStr.split('\n')[:-1]
            try:
                for perXueQi in needDict:
                    perXueQiParamDict = eval(perXueQi)
                    # print(type(perXueQiParamDict),perXueQiParamDict)

                    xuuQi = perXueQiParamDict['nianji']
                    # print(xuuQi)
                    zhangJies = perXueQiParamDict[xuuQi]
                    # print(type(zhangJies),zhangJies)
                    for perZhangJieParam in zhangJies:
                        perXueQiParamDict['zhangjie'] = perZhangJieParam
                        numberNumber = zhangJies[perZhangJieParam]
                        perXueQiParamDict['zhangjieNumber'] =numberNumber
                        # perXueQiParamDict['zhangjie_number'] = numberNumber
                        # print(zhangJies[perZhangJieParam], perXueQiParamDict)
                        for i in range(1, 3):#题型类别
                            # for page in range(1,2):#爬去的页
                            timeStamp = int(time.time()) * 1000
                            start_url = 'http://www.zujuan.com/question/list?categories={0}&question_channel_type={1}&difficult_index=&exam_type=&kid_num=&grade_id%5B%5D=0&grade_id%5B%5D=7&grade_id%5B%5D=8&grade_id%5B%5D=9&sortField=time&page={2}&_={3}'.format(numberNumber, str(i), '1',str(timeStamp))
                            print(start_url)
                            if i == 1:
                                perXueQiParamDict['question_channel_index'] = str(1)
                                perXueQiParamDict['question_channel_type'] = '单选题'
                            else:
                                perXueQiParamDict['question_channel_index'] = str(2)
                                perXueQiParamDict['question_channel_type'] = '多选题'

                            yield Request(url=start_url,meta=perXueQiParamDict,cookies=self.new_cookieVule,headers=self.hearders,callback=self.param_item)
            except Exception as e:
                self.error(repr(e))
    def param_item(self,response):
        # print(response.status)
        # print(response.meta)
        # print(response.body.decode())
        self.param_question(response)
        content = json.loads(response.body.decode())
        totle = content['total']
        pages = totle // self.B
        mod = totle % self.B
        if (totle > 0):
            if (pages > 3):
                pages += 1
                for perPages in range(1, pages):
                    timeStamp = int(time.time()) * 1000
                    start_url = 'http://www.zujuan.com/question/list?categories={0}&question_channel_type={1}&difficult_index=&exam_type=&kid_num=&grade_id%5B%5D=0&grade_id%5B%5D=7&grade_id%5B%5D=8&grade_id%5B%5D=9&sortField=time&page={2}&_={3}'.format(
                        response.meta['zhangjieNumber'], response.meta['question_channel_index'], str(perPages), str(timeStamp))
                    yield Request(url=start_url, meta=response.meta, cookies=self.new_cookieVule, headers=self.hearders,
                                  callback=self.param_question)


            elif (pages < 3 and pages > 1):
                pages += 1
                for perPages in range(1, pages):
                    timeStamp = int(time.time()) * 1000
                    start_url = 'http://www.zujuan.com/question/list?categories={0}&question_channel_type={1}&difficult_index=&exam_type=&kid_num=&grade_id%5B%5D=0&grade_id%5B%5D=7&grade_id%5B%5D=8&grade_id%5B%5D=9&sortField=time&page={2}&_={3}'.format(
                        response.meta['zhangjieNumber'], response.meta['question_channel_index'], str(perPages),str(timeStamp))
                    yield Request(url=start_url, meta=response.meta, cookies=self.new_cookieVule, headers=self.hearders,
                                  callback=self.param_question)

            else:
                pass
        else:
            pass
    def param_question(self,response):
        content = json.loads(response.body.decode())
        # print('主列表信息：', content)
        # print('状态码：', type(response.status), response.status)
        if response.status == 200:
            ids = content['ids']
            try:
                for perDetailUrl in ids:
                    detailUrl = 'http://www.zujuan.com/question/detail-{}.shtml'.format(perDetailUrl)
                    # print('12345url:', detailUrl)
                    response.meta['detailUrl'] = detailUrl
                    yield Request(url=detailUrl, headers=self.hearders, cookies=self.new_cookieVule, meta=response.meta,
                                  callback=self.parse_detail)
            except Exception  as e:
                self.error(repr(e))
        else:
            pass

    def parse_detail(self, response):
        try:
            # print('meta信息:', response.meta)
            # print(response.status)
            items = XitiloadItem()
            items['version'] = response.meta['version']
            items['course'] = response.meta['course']
            items['grade'] = response.meta['nianji']
            items['section'] = response.meta['zhangjie']
            items['type'] = response.meta['question_channel_type']
            items['detailUrl'] = response.meta['detailUrl']
            content = response.body.decode()
            # print('详情页信息：', content)
            queryContent = re.findall(r' var MockDataTestPaper = \[(.+)\]', content)[0]
            queryContentDict = json.loads(queryContent)
            # print('提取的字典：', queryContentDict)
            queryQuestionsDict = queryContentDict['questions'][0]
            # print('精提取的数据：', queryQuestionsDict)

            if 'list' in queryQuestionsDict.keys():
                question_comment_list = []
                list_1 = queryQuestionsDict['list']
                for x in list_1:
                    comment_dict = {}
                    comment_dict['question_text'] = x['question_text']
                    comment_dict['options'] = x['options']
                    question_comment_list.append(comment_dict)
                title = queryQuestionsDict['question_text']
                titleComment = str(title) + str(question_comment_list)
                savePath = self.load_picture(titleComment, 'title')
                items['title'] = savePath[0]
                items['originalTitleUrl'] = savePath[1]
            else:
                title = queryQuestionsDict['question_text']
                savePath = self.load_picture(title, 'title')
                items['title'] = savePath[0]
                items['originalTitleUrl'] = savePath[1]
            explanation = queryQuestionsDict['explanation']
            savePath = self.load_picture(explanation, 'explanation')
            items['analysis'] = savePath[0]
            items['originaAnalysisUrl'] = savePath[1]
            options = queryQuestionsDict['options']
            savePath = self.load_picture(options, 'options')
            items['selects'] = savePath[0]
            items['originaSelectsUrl'] = savePath[1]
            knowledge = queryQuestionsDict['knowledge']
            savePath = self.load_picture(knowledge, 'knowledge')
            items['knowledgePoint'] = savePath[0]
            items['originaKnowledgePoint'] = savePath[1]
            answer = queryQuestionsDict['answer']
            savePath = self.load_picture(answer, 'answer')
            items['answer'] = savePath[0]
            items['originaAnswerUrl'] = savePath[1]
            difficultDindex = queryQuestionsDict['difficult_index']
            difficultDEgree = self.difficult_indexs[difficultDindex]
            items['difficultDEgree'] = difficultDEgree
            if items['originaAnswerUrl'] != 'None' or items['originaKnowledgePoint'] != 'None':
                self.saveSpecialItem(items)
            else:
                yield items
        except Exception as e:
            self.error(repr(e))

    def load_picture(self, url, fileName):
        # self.info(url)
        # print('数据的类型:', type(url), '数据:', url)
        TYSavePath = 'http://res.oitor.com:8089/upload/'
        try:
            if fileName == "knowledge" or fileName == "answer":
                pa = 'D:\\xiti10001\\SpecialPicture\\{}\\'.format(time.strftime('%Y%m%d', time.localtime()))
                isEixct = os.path.exists(pa)
                if isEixct:
                    pass
                else:
                    os.makedirs(pa)
                if (isinstance(url, str)):
                    if (url.startswith('http://') or url.startswith('https://')):
                        path = pa + 'picture_{0}_{1}_{2}.png'.format(fileName,
                                                                     time.strftime("%Y%m%d", time.localtime()),
                                                                     str(int((time.time()) * 1000)))
                        loadRequest.urlretrieve(url, path)
                        geshihua = path[3:].replace('\\', '/')
                        savePath = TYSavePath + geshihua
                        result = (savePath, url)
                        # self.info(result)
                        return result
                    elif ('img' in url):
                        srcLIst = []
                        imgs = Selector(text=url).xpath('//img/@src').extract()
                        for x in imgs:
                            # print('下载url:', x)
                            path = pa + 'picture_{0}_{1}_{2}.png'.format(fileName,
                                                                         time.strftime("%Y%m%d", time.localtime()),
                                                                         str(int((time.time()) * 1000)))
                            loadRequest.urlretrieve(x, path)
                            geshihua = path[3:].replace('\\', '/')
                            savePath = TYSavePath + geshihua
                            # print(type(x), x, type(savePath), savePath)
                            url = url.replace(x, savePath)
                            srcLIst.append(x)

                        if len(srcLIst) == 0:
                            result = (url, 'None')
                            return result
                        else:
                            result = (url, str(srcLIst))
                            # self.info(result)
                            return result

                    else:
                        result = (url, 'None')
                        # self.info(result)
                        return result
                elif (isinstance(url, dict)):
                    srcDict = {}
                    for perSelect in url:
                        path = pa + 'picture_{0}_{1}_{2}.png'.format(fileName,
                                                                     time.strftime("%Y%m%d", time.localtime()),
                                                                     str(int((time.time()) * 1000)))
                        if 'img' in url[perSelect]:
                            imgs_url = []
                            imgs = Selector(text=url[perSelect]).xpath('//img/@src').extract()
                            for img in imgs:
                                # print('选项URL:', img)
                                loadRequest.urlretrieve(img, path)
                                geshihua = path[3:].replace('\\', '/')
                                savePath = TYSavePath + geshihua
                                url[perSelect] = url[perSelect].replace(img, savePath)
                                imgs_url.append(img)
                            srcDict[perSelect] = imgs_url
                        else:
                            pass
                        time.sleep(0.2)
                    if srcDict == {}:
                        result = (str(url), 'None')
                        # self.info(result)
                        return result
                    else:
                        result = (str(url), str(srcDict))
                        # self.info(result)
                        return result



                else:
                    result = (str(url), 'None')
                    # self.info(result)
                    return result

            else:
                pa = 'D:\\xiti10001\\picture\\{}\\'.format(time.strftime('%Y%m%d', time.localtime()))
                isEixct = os.path.exists(pa)
                if isEixct:
                    pass
                else:
                    os.makedirs(pa)
                if (isinstance(url, str)):
                    if (url.startswith('http://') or url.startswith('https://')):
                        path = pa + 'picture_{0}_{1}_{2}.png'.format(fileName,
                                                                     time.strftime("%Y%m%d", time.localtime()),
                                                                     str(int((time.time()) * 1000)))
                        loadRequest.urlretrieve(url, path)
                        geshihua = path[3:].replace('\\', '/')
                        savePath = TYSavePath + geshihua
                        result = (savePath, url)
                        # self.info(result)
                        return result
                    elif ('img' in url):
                        srcLIst = []
                        imgs = Selector(text=url).xpath('//img/@src').extract()
                        for x in imgs:
                            # print('下载url:', x)
                            path = pa + 'picture_{0}_{1}_{2}.png'.format(fileName,
                                                                         time.strftime("%Y%m%d", time.localtime()),
                                                                         str(int((time.time()) * 1000)))
                            loadRequest.urlretrieve(x, path)
                            geshihua = path[3:].replace('\\', '/')
                            savePath = TYSavePath + geshihua
                            # print(type(x), x, type(savePath), savePath)
                            url = url.replace(x, savePath)
                            srcLIst.append(x)

                        if len(srcLIst) == 0:
                            result = (url, 'None')
                            return result
                        else:
                            result = (url, str(srcLIst))
                            # self.info(result)
                            return result

                    else:
                        result = (url, 'None')
                        # self.info(result)
                        return result
                elif (isinstance(url, dict)):
                    srcDict = {}
                    for perSelect in url:
                        path = pa + 'picture_{0}_{1}_{2}.png'.format(fileName,
                                                                     time.strftime("%Y%m%d", time.localtime()),
                                                                     str(int((time.time()) * 1000)))
                        if 'img' in url[perSelect]:
                            imgs_url = []
                            imgs = Selector(text=url[perSelect]).xpath('//img/@src').extract()
                            for img in imgs:
                                # print('选项URL:', img)
                                loadRequest.urlretrieve(img, path)
                                geshihua = path[3:].replace('\\', '/')
                                savePath = TYSavePath + geshihua
                                url[perSelect] = url[perSelect].replace(img, savePath)
                                imgs_url.append(img)
                            srcDict[perSelect] = imgs_url
                        else:
                            pass
                        time.sleep(0.2)
                    if srcDict == {}:
                        result = (str(url), 'None')
                        # self.info(result)
                        return result
                    else:
                        result = (str(url), str(srcDict))
                        # self.info(result)
                        return result



                else:
                    result = (str(url), 'None')
                    # self.info(result)
                    return result
        except Exception as e:
            self.error(repr(e))

    def saveSpecialItem(self, item):
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
            #6391673, 5996867, 5996857, 5798695, 5799259, 5423481, 5425721, 5426101, 5424807, 5422607