# -*- coding: utf-8 -*-
import requests
import  re

'''
txtpath=r"proxy.txt"
fp=open(txtpath)
arr=[]
for lines in fp.readlines():
    lines=lines.replace("\n","")
    arr.append(lines)
fp.close()
proxies = {
        "http": ""
}

url = "http://httpbin.org/ip"
url2 = "http://epub.sipo.gov.cn/gjcx.jsp"
agent = 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'

headers = {
    "User-Agent": agent
}
for each in arr:
    proxy = each
    print("测试"+proxy)
    proxies["http"] =proxy
    try:
        resp = requests.get(url2, proxies=proxies,headers=headers,timeout=5).status_code
        print(resp)
    except Exception as e:
        print(e)
        print("测设出错")
