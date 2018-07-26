#已知各个公司的三类专利的数量，自动爬取代理，使用代理爬取专利
# -*- coding: utf-8 -*-
import requests
import re
import xlrd
import time
import random
import math
from lxml import etree

agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
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
        "numSYXX": "",
        "numWGSQ": "",
        "pageSize": "10",
        "pageNow": "1",
        }

postdata2 = {
        "showType": "1",
        "strWord": "",
        "numSortMethod": "",
        "strLicenseCode": "",
        "slected": "",
        "numFMGB": "",
        "numFMSQ":"",
        "numSYXX": "0",
        "numWGSQ": "",
        "pageSize": "10",
        "pageNow": "1",
        }
postdata3 = {
        "showType": "1",
        "strWord": "",
        "numSortMethod": "",
        "strLicenseCode": "",
        "slected": "",
        "numFMGB": "",
        "numFMSQ":"",
        "numSYXX": "",
        "numWGSQ": "0",
        "pageSize": "10",
        "pageNow": "1",
        }
def addstructure(html):
    #类型
    pattern=r'\[(.*?)\]'
    resp = re.findall(pattern,html,re.S)
    final = " "+resp[0]
    #标题
    pattern = r'\] (.*?)授权公告号：'
    resp = re.findall(pattern,html,re.S)
    if resp:
        final = final+" 标题："+resp[0]
    else:
        final = final+" 标题："
    #授权公告号
    pattern=r'授权公告号：(.*?) '
    resp = re.findall(pattern,html,re.S)
    if resp:
        final = final+" 授权公告号："+resp[0]
    else:
        final = final+" 授权公告号："
    #授权公告日
    pattern=r'授权公告日：(.*?) '
    resp = re.findall(pattern,html,re.S)
    if resp:
        final = final+" 授权公告日："+resp[0]
    else:
        final = final+" 授权公告日："
    #申请号
    pattern=r'申请号：(.*?) '
    resp = re.findall(pattern,html,re.S)
    if resp:
        final = final+" 申请号："+resp[0]
    else:
        final = final+" 申请号："
    #申请日
    pattern=r'申请日：(.*?) '
    resp = re.findall(pattern,html,re.S)
    if resp:
        final = final+" 申请日："+resp[0]
    else:
        final = final+" 申请日："
    #专利权人
    pattern=r'专利权人：(.*?) '
    resp = re.findall(pattern,html,re.S)
    if resp:
        final = final+" 专利权人："+resp[0]
    else:
        final = final+" 专利权人："
    #发明人
    pattern=r'发明人：(.*?) '
    resp = re.findall(pattern,html,re.S)
    if resp:
        final = final+" 发明人："+resp[0]
    else:
        final = final+" 发明人："
    #地址
    pattern=r'地址：(.*?) '
    resp = re.findall(pattern,html,re.S)
    if resp:
        final = final+" 地址："+resp[0]
    else:
        final = final+" 地址："
    #分类号
    pattern=r'分类号：(.*?) '
    resp = re.findall(pattern,html,re.S)
    if resp:
        final = final+" 分类号："+resp[0]
    else:
        final = final+" 分类号："
    #专利代理机构
    pattern=r'专利代理机构：(.*?) '
    resp = re.findall(pattern,html,re.S)
    if resp:
        final = final+" 专利代理机构："+resp[0]
    else:
        final = final+" 专利代理机构："
    #代理人
    pattern=r'代理人：(.*?) '
    resp = re.findall(pattern,html,re.S)
    if resp:
        final = final+" 代理人："+resp[0]
    else:
        final = final+" 代理人："
    #对比文件
    pattern=r'对比文件：(.*?) '
    resp = re.findall(pattern,html,re.S)
    if resp:
        final = final+" 对比文件："+resp[0]
    else:
        final = final+" 对比文件："
    #摘要
    pattern=r'摘要：(.*?) '
    resp = re.findall(pattern,html,re.S)
    if resp:
        final = final+" 摘要："+resp[0]
    else:
        final = final+" 摘要："
    #备注
    pattern = r'同样的发明创造已同日申请发明专利'
    resp = re.findall(pattern,html,re.S)
    if resp:
        final = final+" 备注："+"同样的发明创造已同日申请发明专利"
    else:
        final = final+" 备注："
    return final


def dealstructure(link2):
    link2 = re.sub(r'全部\r', '', link2)
    link2 = re.sub('\s','',link2)
    link2 = re.sub(r'\n', '', link2)
    link2 = re.sub(r'\r', '', link2)
    link2 = re.sub(r'【全部数据】', '', link2)
    link2 = re.sub(r'授权公告号：', ' 授权公告号：', link2)
    link2 = re.sub(r'授权公告日：', ' 授权公告日：', link2)
    link2 = re.sub(r'申请号：', ' 申请号：', link2)
    link2 = re.sub(r'申请日：', ' 申请日：', link2)
    link2 = re.sub(r'专利权人：', ' 专利权人：', link2)
    link2 = re.sub(r'发明人：', ' 发明人：', link2)
    link2 = re.sub(r'地址：', ' 地址：', link2)
    link2 = re.sub(r'分类号：', ' 分类号：', link2)
    link2 = re.sub(r'专利代理机构：', ' 专利代理机构：', link2)
    link2 = re.sub(r'代理人：', ' 代理人：', link2)
    link2 = re.sub(r'对比文件：', ' 对比文件：', link2)
    link2 = re.sub(r'摘要：', ' 摘要：', link2)
    link2 = re.sub(r'【发明专利】', ' 【发明专利】', link2)
    link2 = re.sub(r'申请公布号：', ' 申请公布号：', link2)
    link2 = re.sub(r'申请公布日：', ' 申请公布日：', link2)
    link2 = re.sub(r'申请人：', ' 申请人：', link2)
    link2 = re.sub(r'【实用新型专利】', ' ', link2)
    link2 = re.sub(r'【外观设计专利】', ' ', link2)
    link2 = re.sub(r'【发明专利】', ' ', link2)
    link2 = re.sub(r'【发明专利申请】', ' ', link2)
    link2 = re.sub("\[发明授权\]", '[发明授权] ', link2)
    link2 = re.sub("\[实用新型\]", '[实用新型] ', link2)
    link2 = re.sub("\[外观设计\]", '[外观设计] ', link2)
    link2 = re.sub(r'事务数据', '', link2)
    link2 = re.sub(r'简要说明：', ' 摘要：', link2)
    link2 = re.sub(r'设计人：', ' 发明人：', link2)
    link2 = re.sub(r'进入国家阶段日：', ' 进入国家阶段日：', link2)
    link2 = re.sub(r'申请数据：', ' 申请数据：', link2)
    link2 = re.sub(r'公布数据：', ' 公布数据：', link2)
    link2 = re.sub(r'原申请：', ' 原申请：', link2)
    link2 = re.sub(r'本国优先权：', ' 本国优先权：', link2)
    link2 = re.sub(r'优先权：', ' 优先权：', link2)
    link2 = re.sub(r'同样的发明创造已同日申请发明专利', ' 同样的发明创造已同日申请发明专利', link2)
    link2 = addstructure(link2)
    return link2

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
        html = requests.post(url,data=postdata,headers=headers,proxies=proxy,timeout=60).text
        findpattern = r'<div class="cp_linr">(.*?)</div>'
        find = re.search(findpattern,html,re.S)
        if not find:
            print(find[0])
        return html
    except Exception as e:
        print(e)
        proxies.remove(proxy)
        html = gettext(url,postdata,headers,proxies)
        return html

def crawldata(company,information,pagenum):
    company = company
    postdata = information
    postdata["strWord"] ="申请（专利权）人='%"+company+"%'"
    for i in range(1,pagenum+1):
        #设定最大爬取页数
        print(company+"第%s页"%i)
        postdata["pageNow"] = i
        html = gettext(url_login,postdata,headers,proxies)
        selector = etree.HTML(html)
        link1 = selector.xpath('//div[starts-with(@class,"cp_linr")]')
        if link1:
            for each in link1:
                link2 =each.xpath('string(.)')
                link2=str(link2)
                link2=dealstructure(link2)
                link2 = company+" "+link2
                link2 = str(link2)
                #print(link2)
                result.append(link2)
                time.sleep(1)
        else:
            print("该项该公司已经抓取完毕")
            time.sleep(1)
            break




#主体
data = xlrd.open_workbook("firm.xlsx")
table = data.sheets()[0]   #0表示excel第一张sheet表
companylist = table.col_values(0)  #获取excel第一列中的所有值并保存为列表
FMSQ = table.col_values(1)
SYXX = table.col_values(2)
WGSJ = table.col_values(3)
proxies = crawlproxy()
for i in range(0,len(companylist)):
    if FMSQ[i] == "错误页面":
        f = open('firm.txt','a',encoding='utf-8')
        f.write(companylist[i])
        f.write("\n")
        f.close()
        time.sleep(5)
    else:
        record_fmsq = int(FMSQ[i])
        record_syxx = int(SYXX[i])
        record_wgsj = int(WGSJ[i])
        if record_fmsq > 0:  # 发明授权
            print(companylist[i]+"发明授权")
            result = []
            record_fmsq = math.ceil(record_fmsq/10)
            crawldata(companylist[i],postdata1,record_fmsq)
            f = open('firm.txt','a',encoding='utf-8')
            for every in result:
                f.write(every)
                f.write("\n")
            f.close()
            time.sleep(5)
        if record_syxx > 0:  # 实用新型
            print(companylist[i]+"实用新型")
            result = []
            record_syxx = math.ceil(record_syxx/10)
            crawldata(companylist[i],postdata2,record_syxx)
            f = open('firm.txt','a',encoding='utf-8')
            for every in result:
                f.write(every)
                f.write("\n")
            f.close()
            time.sleep(5)
        if record_wgsj > 0:  # 外观设计
            print(companylist[i]+"外观设计")
            result = []
            record_wgsj = math.ceil(record_wgsj/10)
            crawldata(companylist[i],postdata3,record_wgsj)
            f = open('firm.txt','a',encoding='utf-8')
            for every in result:
                f.write(every)
                f.write("\n")
            f.close()
            time.sleep(5)














