# -*- coding: utf-8 -*-
import requests
import  re
from lxml import etree
url = "http://www.xicidaili.com/nn/"
agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
headers = {
    "User-Agent": agent,
}
html = requests.get(url,headers=headers).text
selector = etree.HTML(html)
record1 = selector.xpath('//*[@id="ip_list"]/tr[starts-with(@class,"odd")]/td[2]')
record2 = selector.xpath('//*[@id="ip_list"]/tr[starts-with(@class,"odd")]/td[3]')
for i in range(0,len(record1)):
    httpproxy = record1[i].xpath('string(.)')
    port = record2[i].xpath('string(.)')
    result = "http://"+httpproxy+":"+port
    f = open('proxy.txt','a',encoding='utf-8')
    f.write(result)
    f.write("\n")
    f.close()
