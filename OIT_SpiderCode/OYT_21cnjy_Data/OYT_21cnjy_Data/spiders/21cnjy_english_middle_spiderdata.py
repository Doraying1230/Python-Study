# #coding:utf-8
# from scrapy.spiders import CrawlSpider
# from scrapy.http import Request
# import urllib.request as  loadRequest
# from scrapy.selector import Selector
# from fake_useragent import UserAgent
# from ..common.BaseObject import BaseObject
# from ..items import XitiloadItem
# import json
# import random
# import time
# import re
# import os
# class SpiderMath(CrawlSpider,BaseObject):
#     name ='21cnjy_english_middle_data'
#     def __init__(self):
#         self.B = 10
#         self.difficult_indexs = {'1': "容易", '2': "较易", '3': "普通", '4': "较难", '5': "困难"}
#         ua = UserAgent()
#         user_agent = ua.random
#         self.cookie = {'Hm_lvt_0280ecaa2722243b1de4829d59602c72': '1505358351',
#                        'xd': 'f2e51c682b7972ee79c3e5e278111819a2a875abde801b145946725928925c52a%3A2%3A%7Bi%3A0%3Bs%3A2%3A%22xd%22%3Bi%3A1%3Bi%3A2%3B%7D',
#                        '_csrf': 'fdaf5dee649eb10ceffebb768b01ad083a191457144f2e37834236f1614a1e35a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22rr9lr0N7bcOh72BPsds2QDzV6p7L0flu%22%3B%7D',
#                        'chid': 'bd8313dfafcee0d97949afd2be099a6e5a44437eef1f94d21b0a7c33a4321f98a%3A2%3A%7Bi%3A0%3Bs%3A4%3A%22chid%22%3Bi%3A1%3Bs%3A1%3A%224%22%3B%7D',
#                        'Hm_lvt_5d70f3704df08b4bfedf4a7c4fb415ef': '1516006299',
#                        'Hm_lpvt_5d70f3704df08b4bfedf4a7c4fb415ef': '1516006321'}
#         # self.cookie = {'aaaaHqNL_ef65_saltkey': 'G7Kkkp1p',
#         #                'aaaaHqNL_ef65_lastvisit': '1515573337',
#         #                'UM_distinctid': '160df6ccd0a1c6-069961f6e93678-454c092b-1aeaa0-160df6ccd0b786',
#         #                '_qddaz': 'QD.myeb91.xj6lqb.jc8vdlxs',
#         #                'HqNL_ef65_saltkey': 'rXoG19po',
#         #                'HqNL_ef65_lastvisit': '1515573663',
#         #                'Hm_lvt_0280ecaa2722243b1de4829d59602c72': '1515576938,1515727104',
#         #                '_csrf': '2d53818b4605f7b8927b7ac5697b32f6b891d079a3872e07336d39ef514225fba%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22z7r-pnQhITVpiDOdLvUAfgnNvVCvWu47%22%3B%7D',
#         #                'aaaaHqNL_ef65_sid': 'MX23cQ',
#         #                'aaaaHqNL_ef65_lastact': '1515738681%09tiku.php%09',
#         #                'Hm_lvt_5d70f3704df08b4bfedf4a7c4fb415ef': '1515727909,1515738493,1515738647,1515738704',
#         #                'HqNL_ef65_sid': 's33318', 'HqNL_ef65_lastact': '1515749593%09index.php%09index',
#         #                'Hm_lpvt_0280ecaa2722243b1de4829d59602c72': '1515749594',
#         #                'chid': '9f22ba4715c9a6998a74ca46f669cbdf971fdc8e71df933fca465c01ce29d004a%3A2%3A%7Bi%3A0%3Bs%3A4%3A%22chid%22%3Bi%3A1%3Bs%3A1%3A%223%22%3B%7D',
#         #                'xd': '494a1f745cfdce14dad87288ba1fd45465b7d32eec1df130011fd3cd0b6415c2a%3A2%3A%7Bi%3A0%3Bs%3A2%3A%22xd%22%3Bi%3A1%3Bs%3A1%3A%221%22%3B%7D',
#         #                'Hm_lpvt_5d70f3704df08b4bfedf4a7c4fb415ef': '1515753358'}
#         self.heaeder = {
#             'Host':'zujuan.21cnjy.com',
#             'Connection':'keep-alive',
#             # 'Accept':'application/json, text/javascript, */*; q=0.01',
#             # 'Referer':'https://zujuan.21cnjy.com/question?categories=25572&bookversion=25571&nianji=25572&chid=3&xd=1',
#             'User-Agent':user_agent
#
#         }
#         self.Parampath = "D:\\xiti10001\\21cnjy\\{0}\\categories_param\\".format(time.strftime('%Y%m%d',time.localtime()))
#         self.SavePath = "D:\\xiti10001\\21cnjy\\{0}\\categories_data\\".format(time.strftime('%Y%m%d',time.localtime()))
#     #测试用
#     # def start_requests(self):
#     #     # main_url = 'https://zujuan.21cnjy.com/question/list?categories=25601&question_channel_type=1&difficult_index=&exam_type=&kid_num=&grade_id%5B%5D=0&grade_id%5B%5D=1&grade_id%5B%5D=2&grade_id%5B%5D=3&grade_id%5B%5D=4&grade_id%5B%5D=5&grade_id%5B%5D=6&sortField=time&filterquestion=0&page=1&page=1&_=1515750125170'
#     #     main_url = 'https://zujuan.21cnjy.com/question/detail/5425721'
#     #     return [Request(url=main_url,headers = self.heaeder,callback=self.param_itemsss,cookies=self.cookie)]
#     # def param_itemsss(self,response):
#     #     print(response.body.decode())
#
#         # content =json.loads(response.body.decode())
#         # print(type(content),content)
#         # ids = content['ids']
#         # print(ids)
#         # try:
#         #     if ids != None:
#         #         print('qer', type(ids), ids)
#         #         for perDetailUrl in ids:
#         #             detailUrl = 'http://www.zujuan.com/question/detail-{}.shtml'.format(perDetailUrl)
#         #             print('12345url:', detailUrl)
#         #             response.meta['detailUrl'] = detailUrl
#         #             # self.info('详情页的url:{}'.format(detailUrl))
#         #             yield Request(url=detailUrl, headers=self.hearders, cookies=self.new_cookieVule, meta=response.meta,
#         #                           callback=self.parse_detail)
#     def start_requests(self):
#         filesSet = os.walk(self.Parampath)
#         for rt, dirs, files in filesSet:
#             if dirs == []:
#                 if 'english_middle' in rt:
#                     perFile = os.path.join(rt, files[0])
#                     # print(perFile)
#                     with open(perFile,'r') as f:
#                         needStr = f.read()
#                         needDict = needStr.split('\n')[:-1]
#                         # print('输出的字符串：',len(needDict),needDict)
#                         try:
#                             # print(123)
#                             for perXueQi in needDict:
#                                 perXueQiParamDict = eval(perXueQi)
#                                 # print(type(perXueQiParamDict),perXueQiParamDict)
#                                 xuuQi = perXueQiParamDict['nianji']
#                                 # print(xuuQi)
#                                 zhangJies = perXueQiParamDict[xuuQi]
#                                 # print(type(zhangJies),zhangJies)
#                                 for perZhangJieParam in zhangJies:
#                                     perXueQiParamDict['zhangjie'] = perZhangJieParam
#                                     numberNumber = zhangJies[perZhangJieParam]
#                                     perXueQiParamDict['zhangjieNumber']=numberNumber
#                                     # perXueQiParamDict['zhangjie_number'] = numberNumber
#                                     # print(zhangJies[perZhangJieParam], perXueQiParamDict)
#                                     tixingDict = perXueQiParamDict['tixing']
#                                     for perTiXing in tixingDict:
#                                         # print(perTiXing)
#
#                                         if(perTiXing == '单选题'):
#                                             # print('qwerty',type(perXueQiParamDict) ,perXueQiParamDict)
#                                             # print('qw')
#                                             # for page in range(1, 3):  # 爬去的页
#                                             #     timeStamp = int(time.time()) * 1000
#                                             if (perXueQiParamDict['jieduan'] == '小学资源导航'):
#                                                 # for page in range(1, 3):  # 爬去的页
#                                                 timeStamp = int(time.time()) * 1000
#                                                 start_url = 'https://zujuan.21cnjy.com/question/list?categories={0}&question_channel_type={1}&difficult_index=&exam_type=&kid_num=&grade_id%5B%5D=0&grade_id%5B%5D=1&grade_id%5B%5D=2&grade_id%5B%5D=3&grade_id%5B%5D=4&grade_id%5B%5D=5&grade_id%5B%5D=6&sortField=time&filterquestion=0&page={2}&page={2}&_={3}'.format(
#                                                     numberNumber, tixingDict[perTiXing], '1', str(timeStamp))
#
#                                                 perXueQiParamDict['question_channel_type'] = perTiXing
#                                                 perXueQiParamDict['question_type_index'] =tixingDict[perTiXing]
#                                                 yield Request(url=start_url, meta=perXueQiParamDict,
#                                                               cookies=self.cookie, headers=self.heaeder,
#                                                               callback=self.param_item)
#                                             elif(perXueQiParamDict['jieduan'] == '初中资源导航'):
#                                                 # print(456)
#                                                 # for page in range(1, 3):  # 爬去的页
#                                                 timeStamp = int(time.time()) * 1000
#                                                 start_url = 'https://zujuan.21cnjy.com/question/list?categories={0}&question_channel_type={1}&difficult_index=&exam_type=&kid_num=&grade_id%5B%5D=0&grade_id%5B%5D=7&grade_id%5B%5D=8&grade_id%5B%5D=9&sortField=time&filterquestion=0&page={2}&page={2}&_={3}'.format(
#                                                     numberNumber, tixingDict[perTiXing], '1', str(timeStamp))
#                                                 perXueQiParamDict['question_channel_type'] = perTiXing
#                                                 perXueQiParamDict['question_type_index'] = tixingDict[perTiXing]
#                                                 yield Request(url=start_url, meta=perXueQiParamDict,
#                                                                   cookies=self.cookie, headers=self.heaeder,
#                                                                   callback=self.param_item)
#                                         elif(perTiXing == '多选题'):
#                                             print("题型解析")
#                                             # if (perXueQiParamDict['jieduan'] == '小学资源导航'):
#                                             #     # for page in range(1, 3):  # 爬去的页
#                                             #     timeStamp = int(time.time()) * 1000
#                                             #     # start_url = 'https://zujuan.21cnjy.com/question/list?categories={0}&question_channel_type={1}&difficult_index=&exam_type=&kid_num=&grade_id%5B%5D=0&grade_id%5B%5D=1&grade_id%5B%5D=2&grade_id%5B%5D=3&grade_id%5B%5D=4&grade_id%5B%5D=5&grade_id%5B%5D=6&sortField=time&filterquestion=0&page={2}&page={2}&_={3}'.format( numberNumber, tixingDict[perTiXing], page, str(timeStamp))
#                                             #     start_url = 'https://zujuan.21cnjy.com/question/list?categories={0}&question_channel_type={1}&difficult_index=&exam_type=&kid_num=&grade_id%5B%5D=0&grade_id%5B%5D=1&grade_id%5B%5D=2&grade_id%5B%5D=3&grade_id%5B%5D=4&grade_id%5B%5D=5&grade_id%5B%5D=6&sortField=time&filterquestion=0&page={2}&page={2}&_={3}'.format( numberNumber, tixingDict[perTiXing], '1', str(timeStamp))
#                                             #     # start_url = 'http://www.zujuan.com/question/list?categories={0}&question_channel_type={1}&difficult_index=&exam_type=&kid_num=&grade_id%5B%5D=0&grade_id%5B%5D=1&grade_id%5B%5D=2&grade_id%5B%5D=3&grade_id%5B%5D=4&grade_id%5B%5D=5&grade_id%5B%5D=6&sortField=time&page={2}&_={3}'.format(
#                                             #     #     numberNumber, tixingDict[perTiXing], page, str(timeStamp))
#                                             #     perXueQiParamDict['question_channel_type'] = perTiXing
#                                             #     perXueQiParamDict['question_type_index'] = tixingDict[perTiXing]
#                                             #     yield Request(url=start_url, meta=perXueQiParamDict,
#                                             #                       cookies=self.cookie, headers=self.heaeder,
#                                             #                       callback=self.param_item)
#                                             # elif (perXueQiParamDict['jieduan'] == '中学资源导航'):
#                                             #     print(4567)
#                                             #     # for page in range(1, 3):  # 爬去的页
#                                             #     timeStamp = int(time.time()) * 1000
#                                             #     start_url = 'https://zujuan.21cnjy.com/question/list?categories={0}&question_channel_type={1}&difficult_index=&exam_type=&kid_num=&grade_id%5B%5D=0&grade_id%5B%5D=7&grade_id%5B%5D=8&grade_id%5B%5D=9&sortField=time&filterquestion=0&page={2}&page={2}&_={3}'.format( numberNumber, tixingDict[perTiXing], '1', str(timeStamp))
#                                             #     # start_url = 'http://www.zujuan.com/question/list?categories={0}&question_channel_type=1&difficult_index=&exam_type=&kid_num=&grade_id%5B%5D=0&grade_id%5B%5D=7&grade_id%5B%5D=8&grade_id%5B%5D=9&sortField=time&page={1}&_={2}'.format(
#                                             #     #     numberNumber, tixingDict[perTiXing], page, str(timeStamp))
#                                             #     perXueQiParamDict['question_channel_type'] = perTiXing
#                                             #     perXueQiParamDict['question_type_index'] = tixingDict[perTiXing]
#                                             #     yield Request(url=start_url, meta=perXueQiParamDict,
#                                             #                       cookies=self.cookie, headers=self.heaeder,
#                                             #                       callback=self.param_item)
#                                             # else:
#                                             #     pass
#                                             # print('qwerty',perXueQiParamDict)
#
#                                         else:
#                                             pass
#
#
#                                             # for i in range(1, 3):  # 题型类别
#                                             #     for page in range(1, 3):  # 爬去的页
#                                             #         timeStamp = int(time.time()) * 1000
#                                             #         start_url = 'http://www.zujuan.com/question/list?categories={0}&question_channel_type={1}&difficult_index=&exam_type=&kid_num=&grade_id%5B%5D=0&grade_id%5B%5D=1&grade_id%5B%5D=2&grade_id%5B%5D=3&grade_id%5B%5D=4&grade_id%5B%5D=5&grade_id%5B%5D=6&sortField=time&page={2}&_={3}'.format(
#                                             #             numberNumber, i, page, str(timeStamp))
#                                             #         print(start_url)
#                                             #         if i == 1:
#                                             #             perXueQiParamDict['question_channel_type'] = '单选题'
#                                             #         else:
#                                             #             perXueQiParamDict['question_channel_type'] = '多选题'
#                                             #
#                                             #         yield Request(url=start_url, meta=perXueQiParamDict,
#                                             #                       cookies=self.cookie, headers=self.heaeder,
#                                             #                       callback=self.param_question)
#                         except Exception as e:
#                             self.error(repr(e))
#                             # print('报错信息',e)
#
#     def param_item(self, response):
#         # print(response.status)
#         # print(response.meta)
#         # print(response.body.decode())
#         self.param_question(response)
#         content = json.loads(response.body.decode())
#         totle = content['total']
#         pages = totle // self.B
#         mod = totle % self.B
#         print('totle总数：', totle)
#         print('pages总数', pages)
#         print('mod的值：', mod)
#         if (totle > 0):
#             if (pages > 3):
#                 for perPages in range(1, 4):
#                     timeStamp = int(time.time()) * 1000
#                     start_url = 'https://zujuan.21cnjy.com/question/list?categories={0}&question_channel_type={1}&difficult_index=&exam_type=&kid_num=&grade_id%5B%5D=0&grade_id%5B%5D=7&grade_id%5B%5D=8&grade_id%5B%5D=9&sortField=time&filterquestion=0&page={2}&page={2}&_={3}'.format(
#                         response.meta['zhangjieNumber'], response.meta['question_type_index'], str(perPages), str(timeStamp))
#                     yield Request(url=start_url, meta=response.meta, cookies=self.cookie, headers=self.heaeder,
#                                   callback=self.param_question)
#
#             elif(pages < 3 and pages > 1):
#                 pages += 1
#                 for perPages in range(1, pages):
#                     timeStamp = int(time.time()) * 1000
#                     start_url = 'https://zujuan.21cnjy.com/question/list?categories={0}&question_channel_type={1}&difficult_index=&exam_type=&kid_num=&grade_id%5B%5D=0&grade_id%5B%5D=7&grade_id%5B%5D=8&grade_id%5B%5D=9&sortField=time&filterquestion=0&page={2}&page={2}&_={3}'.format(
#                         response.meta['zhangjieNumber'], response.meta['question_type_index'], str(perPages),str(timeStamp))
#                     yield Request(url=start_url, meta=response.meta, cookies=self.cookie, headers=self.heaeder,
#                                   callback=self.param_question)
#
#             else:
#                 pass
#         else:
#             pass
#     def param_question(self, response):
#         if response.status == 200:
#             content = json.loads(response.body.decode())
#             # print('主列表信息：', content)
#             ids = content['ids']
#             try:
#                 if ids != None:
#                     # print('qer', type(ids), ids)
#                     for perDetailUrl in ids:
#                         detailUrl = 'https://zujuan.21cnjy.com/question/detail/{}'.format(perDetailUrl)
#                         # print('12345url:', detailUrl)
#                         response.meta['detailUrl'] = detailUrl
#                         #[6413489, 6413437, 6413323, 6413561, 6412615, 6413235, 6413653, 6391673, 6278275, 6276447]
#                         #https://zujuan.21cnjy.com/question/detail/6413437
#                         # self.info('详情页的url:{}'.format(detailUrl))
#                         yield Request(url=detailUrl, headers=self.heaeder, cookies=self.cookie, meta=response.meta,
#                                       callback=self.parse_detail)
#             except Exception  as e:
#                 self.error(repr(e))
#
#
#     def parse_detail(self,response):
#         try:
#             # print('meta信息:', response.meta)
#             # print(response.status)
#             items = XitiloadItem()
#             items['version'] = response.meta['version']
#             items['course'] = response.meta['subject']
#             items['grade'] = response.meta['nianji']
#             items['section'] = response.meta['zhangjie']
#             items['type'] = response.meta['question_channel_type']
#             items['detailUrl'] = response.meta['detailUrl']
#             content = response.body.decode()
#             # print('详情页信息：', content)
#             queryContent = re.findall(r' var MockDataTestPaper = \[(.+)\]', content)[0]
#             queryContentDict = json.loads(queryContent)
#             # print('提取的字典：', queryContentDict)
#             queryQuestionsDict = queryContentDict['questions'][0]
#             # print('精提取的数据：', queryQuestionsDict)
#
#             if 'list' in queryQuestionsDict.keys():
#                 question_comment_list = []
#                 list_1 = queryQuestionsDict['list']
#                 for x in list_1:
#                     comment_dict = {}
#                     comment_dict['question_text'] = x['question_text']
#                     comment_dict['options'] = x['options']
#                     question_comment_list.append(comment_dict)
#                 title = queryQuestionsDict['question_text']
#                 titleComment = str(title) + str(question_comment_list)
#                 savePath = self.load_picture(titleComment, 'title')
#                 items['title'] = savePath[0]
#                 items['originalTitleUrl'] = savePath[1]
#             else:
#                 title = queryQuestionsDict['question_text']
#                 savePath = self.load_picture(title, 'title')
#                 items['title'] = savePath[0]
#                 items['originalTitleUrl'] = savePath[1]
#             explanation = queryQuestionsDict['explanation']
#             savePath = self.load_picture(explanation, 'explanation')
#             items['analysis'] = savePath[0]
#             items['originaAnalysisUrl'] = savePath[1]
#             options = queryQuestionsDict['options']
#             savePath = self.load_picture(options, 'options')
#             items['selects'] = savePath[0]
#             items['originaSelectsUrl'] = savePath[1]
#             knowledge = queryQuestionsDict['knowledge']
#             savePath = self.load_picture(knowledge, 'knowledge')
#             items['knowledgePoint'] = savePath[0]
#             items['originaKnowledgePoint'] = savePath[1]
#             answer = queryQuestionsDict['answer']
#             savePath = self.load_picture(answer, 'answer')
#             items['answer'] = savePath[0]
#             items['originaAnswerUrl'] = savePath[1]
#             difficultDindex = queryQuestionsDict['difficult_index']
#             difficultDEgree = self.difficult_indexs[difficultDindex]
#             items['difficultDEgree'] = difficultDEgree
#             if items['originaAnswerUrl'] != 'None' or items['originaKnowledgePoint'] != 'None':
#                 self.saveSpecialItem(items)
#             else:
#                 yield items
#         except Exception as e:
#             self.error(repr(e))
#
#     def load_picture(self, url, fileName):
#         # self.info(url)
#         # print('数据的类型:', type(url), '数据:', url)
#         TYSavePath = 'http://res.oitor.com:8089/upload/'
#         try:
#             if fileName == "knowledge" or fileName =="answer":
#                 pa = 'D:\\xiti10001\\SpecialPicture\\{}\\'.format(time.strftime('%Y%m%d', time.localtime()))
#                 isEixct = os.path.exists(pa)
#                 if isEixct:
#                     pass
#                 else:
#                     os.makedirs(pa)
#                 if (isinstance(url, str)):
#                     if (url.startswith('http://') or url.startswith('https://')):
#                         path = pa + 'picture_{0}_{1}_{2}.png'.format(fileName,
#                                                                      time.strftime("%Y%m%d", time.localtime()),
#                                                                      str(int((time.time()) * 1000)))
#                         loadRequest.urlretrieve(url, path)
#                         geshihua = path[3:].replace('\\', '/')
#                         savePath = TYSavePath + geshihua
#                         result = (savePath, url)
#                         # self.info(result)
#                         return result
#                     elif ('img' in url):
#                         srcLIst = []
#                         imgs = Selector(text=url).xpath('//img/@src').extract()
#                         for x in imgs:
#                             # print('下载url:', x)
#                             path = pa + 'picture_{0}_{1}_{2}.png'.format(fileName,
#                                                                          time.strftime("%Y%m%d", time.localtime()),
#                                                                          str(int((time.time()) * 1000)))
#                             loadRequest.urlretrieve(x, path)
#                             geshihua = path[3:].replace('\\', '/')
#                             savePath = TYSavePath + geshihua
#                             # print(type(x), x, type(savePath), savePath)
#                             url = url.replace(x, savePath)
#                             srcLIst.append(x)
#
#                         if len(srcLIst) == 0:
#                             result = (url, 'None')
#                             return result
#                         else:
#                             result = (url, str(srcLIst))
#                             # self.info(result)
#                             return result
#
#                     else:
#                         result = (url, 'None')
#                         # self.info(result)
#                         return result
#                 elif (isinstance(url, dict)):
#                     srcDict = {}
#                     for perSelect in url:
#                         path = pa + 'picture_{0}_{1}_{2}.png'.format(fileName,
#                                                                      time.strftime("%Y%m%d", time.localtime()),
#                                                                      str(int((time.time()) * 1000)))
#                         if 'img' in url[perSelect]:
#                             imgs_url = []
#                             imgs = Selector(text=url[perSelect]).xpath('//img/@src').extract()
#                             for img in imgs:
#                                 # print('选项URL:', img)
#                                 loadRequest.urlretrieve(img, path)
#                                 geshihua = path[3:].replace('\\', '/')
#                                 savePath = TYSavePath + geshihua
#                                 url[perSelect] = url[perSelect].replace(img, savePath)
#                                 imgs_url.append(img)
#                             srcDict[perSelect] = imgs_url
#                         else:
#                             pass
#                         time.sleep(0.2)
#                     if srcDict == {}:
#                         result = (str(url), 'None')
#                         # self.info(result)
#                         return result
#                     else:
#                         result = (str(url), str(srcDict))
#                         # self.info(result)
#                         return result
#
#
#
#                 else:
#                     result = (str(url), 'None')
#                     # self.info(result)
#                     return result
#
#             else:
#                 pa = 'D:\\xiti10001\\picture\\{}\\'.format(time.strftime('%Y%m%d', time.localtime()))
#                 isEixct = os.path.exists(pa)
#                 if isEixct:
#                     pass
#                 else:
#                     os.makedirs(pa)
#                 if (isinstance(url, str)):
#                     if (url.startswith('http://') or url.startswith('https://')):
#                         path = pa + 'picture_{0}_{1}_{2}.png'.format(fileName,
#                                                                      time.strftime("%Y%m%d", time.localtime()),
#                                                                      str(int((time.time()) * 1000)))
#                         loadRequest.urlretrieve(url, path)
#                         geshihua = path[3:].replace('\\', '/')
#                         savePath = TYSavePath + geshihua
#                         result = (savePath, url)
#                         # self.info(result)
#                         return result
#                     elif ('img' in url):
#                         srcLIst = []
#                         imgs = Selector(text=url).xpath('//img/@src').extract()
#                         for x in imgs:
#                             # print('下载url:', x)
#                             path = pa + 'picture_{0}_{1}_{2}.png'.format(fileName,
#                                                                          time.strftime("%Y%m%d", time.localtime()),
#                                                                          str(int((time.time()) * 1000)))
#                             loadRequest.urlretrieve(x, path)
#                             geshihua = path[3:].replace('\\', '/')
#                             savePath = TYSavePath + geshihua
#                             # print(type(x), x, type(savePath), savePath)
#                             url = url.replace(x, savePath)
#                             srcLIst.append(x)
#
#                         if len(srcLIst) == 0:
#                             result = (url, 'None')
#                             return result
#                         else:
#                             result = (url, str(srcLIst))
#                             # self.info(result)
#                             return result
#
#                     else:
#                         result = (url, 'None')
#                         # self.info(result)
#                         return result
#                 elif (isinstance(url, dict)):
#                     srcDict = {}
#                     for perSelect in url:
#                         path = pa + 'picture_{0}_{1}_{2}.png'.format(fileName,
#                                                                      time.strftime("%Y%m%d", time.localtime()),
#                                                                      str(int((time.time()) * 1000)))
#                         if 'img' in url[perSelect]:
#                             imgs_url = []
#                             imgs = Selector(text=url[perSelect]).xpath('//img/@src').extract()
#                             for img in imgs:
#                                 # print('选项URL:', img)
#                                 loadRequest.urlretrieve(img, path)
#                                 geshihua = path[3:].replace('\\', '/')
#                                 savePath = TYSavePath + geshihua
#                                 url[perSelect] = url[perSelect].replace(img, savePath)
#                                 imgs_url.append(img)
#                             srcDict[perSelect] = imgs_url
#                         else:
#                             pass
#                         time.sleep(0.2)
#                     if srcDict == {}:
#                         result = (str(url), 'None')
#                         # self.info(result)
#                         return result
#                     else:
#                         result = (str(url), str(srcDict))
#                         # self.info(result)
#                         return result
#
#
#
#                 else:
#                     result = (str(url), 'None')
#                     # self.info(result)
#                     return result
#         except Exception as e:
#             self.error(repr(e))
#     def saveSpecialItem(self,item):
#             path = 'D:\\xiti10001\\specialData\\{}\\'.format(time.strftime("%Y%m%d", time.localtime()))
#             # path = 'd:\\OITData\\zujuan\\{0}\\{1}\\'.format(time.strftime("%Y%m%d", time.localtime()), spider.name)
#             isExists = os.path.exists(path)
#             if isExists:
#                 pass
#             else:
#                 os.makedirs(path)
#             with open(path + self.name + '.json', 'a', encoding='utf-8')as f:
#                 lines = json.dumps(dict(item), ensure_ascii=False)
#                 f.write(lines)
#                 f.write('\n')
