#coding:utf-8
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from scrapy.selector import Selector
import time
import os



def make_file(perPath):
    isExists = os.path.exists(perPath)
    if isExists:
        pass
    else:
        os.makedirs(perPath)




main_url = "http://www.jyeoo.com"
path = 'D:\\xiti10001\\qingyou\\{0}\\categories_param\\'.format(time.strftime('%Y%m%d',time.localtime()))
jieduan = ['小学','初中']
kemuset = ['数学','物理','化学','英语','语文']
middle_paramDict = {'数学':'qingyouwang_math_middle_param', '物理':'qingyouwang_wuli_middle_param', '化学':'qingyouwang_math_huaxue_param', '英语':'qingyouwang_english_middle_param', '语文':'qingyouwang_chinese_middle_param'}
xiaoxue_paramDict = {'数学':'qingyouwang_shuxue_param','语文':'qingyouwang_yuwen_param','英语':'qingyouwang_yingyu_param'}
Chrome_path = 'D:\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe'
banben = ['牛津译林新版','牛津译林版（三年级起点））','部编版','语文版','人教新版','上海新版','上海版','苏教版','沪教版','沪科新版','苏科版','沪科版','苏科新版','沪科新版','沪教新版','苏教新版']
xueqi = ['三年级上','三年级下','四年级上','四年级下','五年级上','五年级下','六年级上','六年级下','七年级上','七年级下','八年级上','八年级下','九年级上','九年级下','七年级','八年级','九年级']
try:
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap['phantomjs.page.settings.userAgent'] = (
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36')
    browser = webdriver.PhantomJS(executable_path=Chrome_path, desired_capabilities=dcap,service_args=['--ignore-ssl-errors=true'])
    browser.get('http://www.jyeoo.com/')
    comment = browser.page_source
    spiderText = Selector(text=comment)
    list_Sub_title = [1,3]
    for per_subTitle in list_Sub_title:
        subTitle = spiderText.xpath('//div[@class="sub-group"]/ul/li[{0}]/div[1]/b/text()'.format(str(per_subTitle))).extract_first()
        subTitle_text = spiderText.xpath('//div[@class="sub-group"]/ul/li[{0}]/div[@class="sub-list"]/ul/li/span/text()'.format(str(per_subTitle))).extract()
        subTitle_url = spiderText.xpath('//div[@class="sub-group"]/ul/li[{0}]/div[@class="sub-list"]/ul/li/a[1]/@href'.format(str(per_subTitle))).extract()
        subTitleDict = dict(zip(subTitle_text,subTitle_url))
        print(123,subTitle,subTitleDict)
        if subTitle:
            for perSubTitle in subTitleDict.keys():
                print(1)
                print(perSubTitle)

                if perSubTitle in kemuset:
                    urlHouZhui = subTitleDict[perSubTitle]
                    Furl = main_url+urlHouZhui
                    print(Furl)
                    browser.get(Furl)
                    time.sleep(1)
                    comment = browser.page_source
                    sourse = Selector(text=comment)
                    spider_banben = sourse.xpath('//div[@id="cont"]/table/tbody/tr[2]/td/ul/li/a/text()').extract()
                    qs_ed = sourse.xpath('//div[@id="cont"]/table/tbody/tr[2]/td/ul/li/a/@data-id').extract()
                    version_qs_edDict = dict(zip(spider_banben,qs_ed))
                    for per_banben in spider_banben:
                        if per_banben in banben:
                            browser.find_element_by_link_text(per_banben).click()
                            # browser.manage().timeouts().pageLoadTimeout(10, TimeUnit.SECONDS)
                            # handles = browser.window_handles
                            # print('所有的数据句柄1：',handles)
                            comment1 = browser.page_source
                            sourse1 = Selector(text=comment1)
                            spider_xueqi = sourse1.xpath('//div[@id="cont"]/table/tbody/tr[3]/td/ul/li/a/text()').extract()
                            for per_xueqi in spider_xueqi:
                                try:
                                    if per_xueqi in xueqi:
                                        browser.find_element_by_link_text(per_xueqi).click()
                                        time.sleep(2)
                                        # browser.save_screenshot('./yuwen_{}.png'.format(str(int(time.time() * 1000))))
                                        commment2 = browser.page_source
                                        sourse2 = Selector(text=commment2)
                                        spider_xueqi_text = sourse2.xpath('//ul[@class="treeview"]/li/a/text()').extract()
                                        spider_xueqi_url = sourse2.xpath('//ul[@class="treeview"]/li/a/@pk').extract()
                                        spider_Dict = dict(zip(spider_xueqi_text,spider_xueqi_url))
                                        saveDict = {'jieduan':subTitle,'kemu':perSubTitle,'version':per_banben,'version_qs_edDict':version_qs_edDict,'xueqi':per_xueqi,'param':spider_Dict}
                                        saveData = str(saveDict)
                                        print(saveData)
                                        if '初 中' == subTitle:
                                            perPath = path+middle_paramDict[perSubTitle]
                                            print(perPath)
                                            make_file(perPath)
                                            with open(perPath+'\\{}.txt'.format(time.strftime('%Y%m%d', time.localtime())),'a') as f:
                                                f.write(saveData)
                                                f.write('\n')
                                        else:
                                            perPath = path + xiaoxue_paramDict[perSubTitle]
                                            print(perPath)
                                            make_file(perPath)
                                            with open(perPath + '\\{}.txt'.format(time.strftime('%Y%m%d', time.localtime())), 'a') as f:
                                                f.write(saveData)
                                                f.write('\n')


                                        #
                                             # print(subTitle,perSubTitle,per_banben,per_xueqi,spider_Dict,'需要的数据')
                                except Exception as e:
                                    pass


except Exception as e:
    print(e)



