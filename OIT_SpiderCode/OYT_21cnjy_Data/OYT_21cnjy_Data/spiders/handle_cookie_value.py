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
if __name__ == "__main__":
    w = '1513606612,1515076313'
    a ='pgv_pvi=8263609344; tencentSig=980247552; PHPSESSID=1qaumicrn7rgdue06krm0vuud0; pgv_si=s6408843264; IESESSION=alive; _qddamta_800024201=3-0; jiami_userid=Njk0MzE0fDc3NmJhNjMzNWQ3YTlhMDdiNDczMzk5NjZkNjgyZGU5; account=18913192830; password=MTIzNDU2; ytkuser=%7B%22id%22%3A%22694314%22%2C%22deadline%22%3A%220%22%2C%22feature%22%3A%22ab3bf35ba595e3d526686273dd4cffd7%22%7D; _qddac=3-1.1.8ip7kt.jcvnsqo9; Hm_lvt_ba430f404e1018c19017fd7d6857af83=1515642911,1516954929; Hm_lpvt_ba430f404e1018c19017fd7d6857af83=1516955006; _qddaz=QD.41x9sm.550iah.jc9ynmya; _qdda=3-1.1; _qddab=3-8ip7kt.jcvnsqo9'

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
    c ={'pgv_pvi': '8869029888', 'tencentSig': '8349357056', 'PHPSESSID': '21rbna3k500ic89ga8qjmqhjs3', 'pgv_si': 's8352073728', 'IESESSION': 'alive', 'jiami_userid': 'NjkzMzE0fDk1NzM5YmM5MzIwYjY1ZmViZmE3NDQ3ZmVkY2E4NTY3', 'account': '18621942417', 'password': 'MTIzNDU2', 'ytkuser': '%7B%22id%22%3A%22693314%22%2C%22deadline%22%3A%220%22%2C%22feature%22%3A%22f5ee54afd56eef93b9db72a134881074%22%7D', '_qddamta_800024201': '3-0', 'Hm_lvt_ba430f404e1018c19017fd7d6857af83': '1515726959,1516586108,1516605643,1516759114', 'Hm_lpvt_ba430f404e1018c19017fd7d6857af83': '1516781155', '_qddaz': 'QD.s08ddj.bmtxtt.jcbcp2wi', '_qdda': '3-1.40rskb', '_qddab': '3-jigb7l.jcsqod1w'}
    c = {'pgv_pvi': '8869029888', 'tencentSig': '8349357056', 'PHPSESSID': '21rbna3k500ic89ga8qjmqhjs3', 'pgv_si': 's8352073728', 'IESESSION': 'alive', 'jiami_userid': 'NjkzMzE0fDk1NzM5YmM5MzIwYjY1ZmViZmE3NDQ3ZmVkY2E4NTY3', 'account': '18621942417', 'password': 'MTIzNDU2', 'ytkuser': '%7B%22id%22%3A%22693314%22%2C%22deadline%22%3A%220%22%2C%22feature%22%3A%22f5ee54afd56eef93b9db72a134881074%22%7D', '_qddamta_800024201': '3-0', 'Hm_lvt_ba430f404e1018c19017fd7d6857af83': '1515726959,1516586108,1516605643,1516759114', 'Hm_lpvt_ba430f404e1018c19017fd7d6857af83': '1516781292', '_qddaz': 'QD.s08ddj.bmtxtt.jcbcp2wi', '_qdda': '3-1.40rskb', '_qddab': '3-jigb7l.jcsqod1w'}
