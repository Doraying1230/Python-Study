#coding:utf-8
import time
import logging
import random
# r = random.sample('1234567890',13)
# print(r)
# a = random.randint(0,99999999)
# number = str(a)
# # url = 'http://www.zujuan.com/question/list?categories={0}&question_channel_type={1}&difficult_index=&exam_type=&kid_num=&grade_id%5B%5D=0&grade_id%5B%5D=1&grade_id%5B%5D=2&grade_id%5B%5D=3&grade_id%5B%5D=4&grade_id%5B%5D=5&grade_id%5B%5D=6&sortField=time&page={2}&_=15150{4}'
# list_1 = []
# with open('d:\\OITData\\zujuan\\categories_math_{}.txt'.format(time.strftime('%Y%m%d',time.localtime(time.time()))),'r') as f:
# #     ad = f.read()
#     ad = ad.split('\n')
#     for  x in  ad:
#         if x :
#             list_1.append(x)
#     print(type(list_1), len(list_1))
#     for x in list_1:
#         x = eval(x)
#         xc = x['nianji']
#         vd = x[xc]
#         for c in vd:
#             print(vd[c])
#         print(type(vd),vd)
        # print(type(x),x)
        # print(123)

# 1515043193598 1515043318738
# 31885483
# import random
# a = random.randint(0,99999999)
# a = str(a)
# print(type(a),a)
# random.seed(int(''.join([str(rand8()) for i in xrange(8)])))
# rand7 = lambda: random.randint(0, 7)


# def text():
#     with open( 'd:\\OITData\\zujuan\\categories_math_{}.txt'.format(time.strftime('%Y%m%d', time.localtime(time.time()))),'r') as f:
#         needStr = f.read()
#         needDict = needStr.split('\n')[:-1]
#         for perXueQi in needDict:
#             perXueQiParamDict = eval(perXueQi)
#             # print(type(perXueQiParamDict),perXueQiParamDict)
#
#             xuuQi = perXueQiParamDict['nianji']
#             # print(xuuQi)
#             zhangJies = perXueQiParamDict[xuuQi]
#             # print(type(zhangJies),zhangJies)
#             for perZhangJieParam in zhangJies:
#                 perXueQiParamDict['zhangjie'] =perZhangJieParam
#                 numberNumber = zhangJies[perZhangJieParam]
#                 # perXueQiParamDict['zhangjie_number'] = numberNumber
#                 print(zhangJies[perZhangJieParam],perXueQiParamDict)
#                 for i in range(1,3):
#                     for page in range(1,11):
#                         a = random.randint(0, 99999999)
#                         numbert = str(a)
#                         urls = 'http://www.zujuan.com/question/list?categories={0}&question_channel_type={1}&difficult_index=&exam_type=&kid_num=&grade_id%5B%5D=0&grade_id%5B%5D=1&grade_id%5B%5D=2&grade_id%5B%5D=3&grade_id%5B%5D=4&grade_id%5B%5D=5&grade_id%5B%5D=6&sortField=time&page={2}&_=15150{3}'.format(numberNumber,i,page,numbert)
#                         print(urls)
#
# text()
if __name__ =="__main__":
    w = '1513606612,1515076313'
    a ="PHPSESSID=t6ka3qnr3c1r1i80g4p2l9ubb4; pgv_pvi=971794432; pgv_si=s757466112; IESESSION=alive; tencentSig=1219419136; _qddaz=QD.ic8x9a.yb0pya.jcu9im6y; _qdda=3-1.10gm0l; _qddab=3-8pf78a.jcub4t6b; jiami_userid=Njk0MjM0fDVjYTQ3NTdlZDA2OGYzNjhiMzQzNjQzZjdmNDgwYWJm; account=18221013967; password=MTIzNDU2; ytkuser=%7B%22id%22%3A%22694234%22%2C%22deadline%22%3A%220%22%2C%22feature%22%3A%2246b0e1720094c569d777770a6b211962%22%7D; Hm_lvt_ba430f404e1018c19017fd7d6857af83=1516870476,1516873190; Hm_lpvt_ba430f404e1018c19017fd7d6857af83=1516875966"
    b = a.replace('; ','。').replace('=',':')
    print(123,b)
    c  = b.split('。')
    # print(c)
    # for x in c :
    #     print()
    # for x in c :
    #     v = x.split(':')
    #     print(c)
    dict_1 = {}
    for x in c:
        v = x.split(':')
        key_1 = v[0]
        value_1 = v[1]

        dict_1[key_1] = value_1
    print(1234567,type(dict_1),dict_1)



    a =(123,456)
    b= str(a)
    print(type(b),b)
# print(c)
# c = eval(b)
# print(c)

# print(c)
#1514862047,1515031679
# a  = time.strftime("%Y%m%d",time.localtime())
# print(time.strftime('%Y%m%d',time.localtime()))
# se = int(time.time()* 1000)#获取13位的时间戳
# print('se',se)
# a = '123'
# b   = 123
# if isinstance(b,str):
#     print('success')
# else:
#     print('false')
#
# from scrapy.selector import Selector
#
# a = 12
# B = Selector(text=a).xpath('//img').extract()
# for x in B:
#     print(x)
# print(B)

#coding:utf-8
# from fake_useragent import UserAgent
# ua = UserAgent()
# print(ua.random)
# print(ua.random)
# print(ua.random)
# print(ua.random)
# c = {'_sync_login_identity': '52dbfe5f11a285543557b4f3bea9119ec192c9f4137fac0aaf0c14855d19278ca%3A2%3A%7Bi%3A0%3Bs%3A20%3A%22_sync_login_identity%22%3Bi%3A1%3Bs%3A50%3A%22%5B1236678%2C%223InwgUTNhX5T4-R1ACg_gCHOyX1wJ8QT%22%2C86400%5D%22%3B%7D', '_identity': '58c14c05c924b81b6d3f45456b78313e53d075bc4db1a95f0bc64358d6ba2fafa%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A50%3A%22%5B1236678%2C%22f2828bc8e0832bb1d0de103ad9c60a5b%22%2C86400%5D%22%3B%7D', 'PHPSESSID': 'vvv6m91o0qffg767n41pd7efl4', 'chid': 'edb26e513d9f6c5b27f481f2930c0f29b22e216a8813fde3b300c0c1883d7d9ba%3A2%3A%7Bi%3A0%3Bs%3A4%3A%22chid%22%3Bi%3A1%3Bi%3A3%3B%7D', 'xd': '75519cb9f2bf90d001c0560f5c40520062a60ada9cb38350078f83e04ee38a31a%3A2%3A%7Bi%3A0%3Bs%3A2%3A%22xd%22%3Bi%3A1%3Bi%3A2%3B%7D', 'isdialog': 'bad3c21672f08107d1d921526d191f58bd47d79e7dbb432bd32624a836b42e85a%3A2%3A%7Bi%3A0%3Bs%3A8%3A%22isdialog%22%3Bi%3A1%3Bs%3A4%3A%22show%22%3B%7D', '_csrf': '5f0821bf1ec353c99e311228fb4a9661c13eba69298d82b612fb0b70b65d71cea%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22H_kCNSfahlmVZpabjEWXZXk5Oimm_McZ%22%3B%7D',
#      'Hm_lvt_6de0a5b2c05e49d1c850edca0c13051f': '1515117036,1515133822,1515475032,1515569874',
#      'Hm_lpvt_6de0a5b2c05e49d1c850edca0c13051f': '1515570260'}
# path = "d:\\htfdss\\fund\\approval\\test\\{0}".format(time.strftime('%Y%m%d', time.localtime(time.time())))
# def text ():
#     logging.basicConfig(level=logging.INFO,
#                                 format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                                 datefmt='%a, %d %b %Y %H:%M:%S',
#                                 filename=path + '\\{}.log'.format(time.strftime('%Y%m%d', time.localtime(time.time()))),
#                                 filemode='w')
#     return logging
# c = text()
# print('123',c.info('dfghjk'))
{"version": "牛津译林版", "course": "英语", "grade": "七年级上", "section": "Unit 7 Shopping", "type": "单选题", "detailUrl": "http://www.zujuan.com/question/detail-2852587.shtml", "title": "-- ________ there any sheep on the hill?<br/>-- ________.", "originalTitleUrl": "None", "analysis": "d:\\OITData\\zujuan\\20180110\\zujuan_english_middle_data\\picture\\picture_explanation_20180110_1515583317971.png", "originaAnalysisUrl": "http://webshot.zujuan.com/q/23/45/aff2e744f3f0436b8abca558eb8d_2852587ex.png?hash=9b5b96bec0c7f1edaa512cba9920ad5b&sign=6b2f9d376099791183ec025823bf02fa&from=2", "selects": "{'A': 'Is; Yes, there are', 'B': 'Are; Yes, there are&nbsp;', 'C': 'Is; No, there isn’t', 'D': 'Are; No, there isn’t'}", "originaSelectsUrl": "None", "knowledgePoint": "d:\\OITData\\zujuan\\20180110\\zujuan_english_middle_data\\picture\\picture_knowledge_20180110_1515583318837.png", "originaKnowledgePoint": "http://webshot.zujuan.com/q/23/45/aff2e744f3f0436b8abca558eb8d_2852587kn.png?hash=5169d30085d78422913e249407a64ca9&sign=3f9665e34a6f4eeb62d1c4111173715c&from=2", "answer": "d:\\OITData\\zujuan\\20180110\\zujuan_english_middle_data\\picture\\picture_answer_20180110_1515583318891.png", "originaAnswerUrl": "http://webshot.zujuan.com/q/23/45/aff2e744f3f0436b8abca558eb8d_2852587an.png?hash=e5d1a4aa0b2ff88c4f988a973824a586&sign=11155c35d61869e70321f27c5d7f9a77&from=2"}