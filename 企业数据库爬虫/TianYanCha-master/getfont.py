# -*- coding:utf-8 -*-
# 得到网址后自行下载tycfont文件


import requests
from bs4 import BeautifulSoup
import importlib,sys
importlib.reload(sys)




def request(url):
    header = {
        "Referer": "https://www.baidu.com/",
        "User-Agent": "Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36"
    }
    r = requests.get(url, headers=header)
    return r.text

def gettycfont():
    fails = 1
    while fails < 31:
        try:
            source = request("https://m.tianyancha.com/")
            break
        except Exception as e:
            print(e)
    else:
        raise Exception
    pagesouup = BeautifulSoup(source, 'html.parser')
    csssheet = pagesouup.find_all("link", rel="stylesheet")
    for link in csssheet:
        csshref = link.get('href')
        if 'fonts-styles' in csshref:
            fails = 1
            while fails < 31:
                try:
                    csscode = request(csshref)
                    break
                except Exception as e:
                    print(e)
            else:
                raise Exception
            print(csscode)


gettycfont()
