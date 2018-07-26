#自动爬取代理，自动用代理爬公司的三类专利的总的数量
# -*- coding: utf-8 -*-
import requests
import re
import xlrd
import time
import random
from lxml import etree


agent = 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'
#专利网站header
headers = {
    "User-Agent": agent,
    "Host": "epub.sipo.gov.cn",
    "Origin": "http://epub.sipo.gov.cn",
    "Referer": "http://epub.sipo.gov.cn/gjcx.jsp"
}

proxy = {
        "http": "",
}


url_login = 'http://epub.sipo.gov.cn/patentoutline.action'

postdata1 = {
        "showType": "1",
        "strWord": "",
        "numSortMethod": "",
        "strLicenseCode": "",
        "slected": "",
        "numFMGB": "",
        "numFMSQ":"0",
        "numSYXX": "0",
        "numWGSQ": "0",
        "pageSize": "3",
        "pageNow": "1",
        }
def fff(url,headers):
    try:
        html = requests.get(url,headers=headers,timeout=60).text
        return html
    except Exception as e:
        html = fff(url,headers)
        return html







def crawlproxy():
    global proxies
    proxies = []
    url = "http://www.xicidaili.com/nn/"
    urltest = "http://httpbin.org/ip"
    agent = 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'
    headers = {
        "User-Agent": agent,
    }
    html = fff(url,headers)
    selector = etree.HTML(html)
    record1 = selector.xpath('//*[@id="ip_list"]/tr[starts-with(@class,"odd")]/td[2]')
    record2 = selector.xpath('//*[@id="ip_list"]/tr[starts-with(@class,"odd")]/td[3]')
    for i in range(0,len(record1)):  #注意修改
        httpproxy = record1[i].xpath('string(.)')
        port = record2[i].xpath('string(.)')
        test = {"http":"http://"+httpproxy+":"+port}
        print("http://"+httpproxy+":"+port)
        proxies.append(test)
    return proxies



def gettext(url,postdata,headers,proxies):
    if proxies:
        proxy = random.choice(proxies)
    else:
        print("代理ip已用完")
        proxies = crawlproxy()
        proxy =random.choice(proxies)
    try:
        html = requests.post(url,data=postdata,headers=headers,timeout=60,proxies=proxy).text
        pattern0 =r'错误页面'
        pattern1 =r'发明授权：(.*?)件'
        record0 = re.search(pattern0,html,re.S)
        record1 = re.search(pattern1,html,re.S)
        if (not record1) and (not record0):   #判断页面是否正常
            print(record0[0])
        return html
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)
        proxies.remove(proxy)
        html = gettext(url, postdata, headers,proxies)
        return html
def crawl(company):
     print("爬取"+company+"各类记录数")
     postdata = postdata1
     postdata["strWord"] ="申请（专利权）人='%"+company+"%'"
     html = gettext(url_login,postdata,headers,proxies)
     pattern0 =r'错误页面'
     pattern1 =r'发明授权：(.*?)件'
     pattern2 =r'实用新型：(.*?)件'
     pattern3 =r'外观设计：(.*?)件'
     record0 = re.search(pattern0,html,re.S)
     if record0:
         result = company +";错误页面"
     else:
         record1 = re.findall(pattern1,html,re.S)
         if record1:
            record2 = re.findall(pattern2,html,re.S)
            record3 = re.findall(pattern3,html,re.S)
            result = company+";"+record1[0]+";"+record2[0]+";"+record3[0]
         else:
             result = html
     f = open('firmprimaryrecord.txt','a',encoding='utf-8')
     f.write(result)
     f.write("\n")
     f.close()
     print(result)

data = xlrd.open_workbook("firm2.xlsx")
table = data.sheets()[0]   #0表示excel第一张sheet表
companylist = table.col_values(0)  #获取excel第一列中的所有值并保存为列表
proxies = crawlproxy()
for each in companylist:
    crawl(each)










