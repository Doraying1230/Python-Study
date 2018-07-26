# -*- coding:utf-8 -*-

from urllib.parse import quote
import xlrd, arrow, urllib, re, os, requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random, time
from sqlalchemy import create_engine
import pandas as pd
import datetime
import importlib,sys
importlib.reload(sys)
import pymysql
import urllib3
from fontTools.ttLib import TTFont
from time import sleep

engine = create_engine('mysql+pymysql://root:123456@127.0.0.1/demo?charset=utf8')
path = '/home/wu/PycharmProjects/tyc/'
name = 'tyc-num.ttf'
#自行更改路径

def browserdriver():
    ua = "Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36"
    profile = webdriver.FirefoxProfile()
    profile.set_preference(
        "general.useragent.override", ua)
    driver = webdriver.Firefox(profile, executable_path=r'/usr/local/bin/geckodriver')
    return driver


def request(url):
    header = {
        "Referer": "https://www.baidu.com/",
        "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36"
    }
    r = requests.get(url, headers=header)
    return r.text


def tyc_data(driver, url, keyword, maping):
    fails = 1
    while fails < 31:
        try:
            driver.set_page_load_timeout(10)
            driver.get("about:blank")
            driver.get(url)
            break
        except Exception as e:
            print(e)
            driver.quit()
            sys.exit()
    else:
        raise Exception
    try:
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CLASS_NAME, "footerV2"))
        )
    except Exception as e:
        print(e)
    finally:
        source = driver.page_source.encode("utf-8")
        tycsoup = BeautifulSoup(source, 'html.parser')
        name = tycsoup.select(
            "div > div > div > div > a.query_name > span")
        if len(name)>0:
            zcxx = tycsoup.select('div > div > div > div > div > div > div.title > span')
            zczb = zcxx[0].get_text() if len(zcxx) > 0 else None,
            zcsj = zcxx[1].get_text() if len(zcxx) > 1 else None,
            cmname = name[0].text if len(name) > 0 else None
            company_url = "https://m.tianyancha.com" + tycsoup.select('div > div > div > div > a.query_name')[0].get(
                'href')
            fails = 1
            while fails < 31:
                try:
                    driver.set_page_load_timeout(10)
                    driver.get("about:blank")
                    driver.get(company_url)
                    break
                except Exception as e:
                    print(e)
                    driver.quit()
                    sys.exit()
            else:
                raise
            try:
                WebDriverWait(driver, 60).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "footerV2"))
                )
            except Exception as e:
                print(e)
            finally:
                noinfo = ""
                source = driver.page_source.encode("utf-8")
                tycdata = BeautifulSoup(source, 'html.parser')
                reginfo = tycdata.select("div.item-line > span")
                bsocplist = tycdata.select("div.item-line > span > span > span.hidden > div")
                cpname = tycdata.select("div.company-mobile-container416 > div > div > div > div.f18.new-c3.float-left")
                cpname = cpname[0].get_text() if len(bsocplist) > 0 else None
                bscop = recode(maping, bsocplist[0].get_text()) if len(bsocplist) > 0 else None
                concat = tycdata.select('div > div > div > div > div > span.title-right417')
                web = tycdata.select('div > div > div > div > div a.title-right417.overflow-width')
                web = web[0].text if len(web) > 0 else None
                phone = concat[0].text if len(concat) > 0 else None
                email = concat[1].text if len(concat) > 1 else None
                address = concat[2].text if len(concat) > 2 else None
                if address == None:
                    pass
                elif len(address) == 0:
                    address = concat[3].text if len(concat) > 3 else None
                try:
                    binfo = [
                        keyword,
                        cpname,
                        phone,
                        email,
                        web,
                        reginfo[9].get_text() if len(reginfo[9].get_text()) > 0 else None,
                        address.replace('附近公司',''),
                        reginfo[27].get_text() if len(reginfo[27].get_text()) > 0 else None,
                        reginfo[3].get_text() if len(reginfo[3].get_text()) > 0 else None,
                        reginfo[1].get_text() if len(reginfo[1].get_text()) > 0 else None,
                        zczb,
                        zcsj,
                        reginfo[23].get_text() if len(reginfo[23].get_text()) > 0 else None,
                        reginfo[13].get_text() if len(reginfo[13].get_text()) > 0 else None,
                        reginfo[15].get_text() if len(reginfo[15].get_text()) > 0 else None,
                        reginfo[17].get_text() if len(reginfo[17].get_text()) > 0 else None,
                        reginfo[11].get_text() if len(reginfo[11].get_text()) > 0 else None,
                        reginfo[19].get_text() if len(reginfo[19].get_text()) > 0 else None,
                        reginfo[21].get_text() if len(reginfo[21].get_text()) > 0 else None,
                        reginfo[25].get_text() if len(reginfo[25].get_text()) > 0 else None,
                        bscop
                    ]
                    return binfo
                except:
                    print('查询无结果')
                    binfo = [keyword, "查询无结果"]
                    return binfo

        else:
            print('查询无结果')
            binfo = [keyword, "查询无结果"]
            return binfo


def getrep():
    font = TTFont(path + name)
    cmaps = font.getBestCmap()
    orders = font.getGlyphOrder()

    a = {value:key for key,value in cmaps.items()}
    b=list(pd.Series(orders).replace(a))

    l = [eval(r"u'\u" + hex(i)[2:] + "'").encode('utf-8') for i in b[11:]]
    l = [dec.decode('utf-8') for dec in l]

    print(len(l))

    l2 = []
    #l2为字体文件里的中文
	



    print(len(l2))
    mapfont = dict(zip(l,l2))
    return mapfont


def recode(mapfont, regstr):
    strlist = list(regstr)
    regdata = []
    for stra in strlist:
        if stra in mapfont.keys():
            regdata.append(mapfont[stra])
        else:
            regdata.append(stra)
    return "".join(regdata)


def main(cpnames,cptables):
    try:
        driver = browserdriver()
    except Exception as e:
        print(e)
    maping = getrep()
    index = [
        "查询公司名称", "公司名称", "电话号码", "邮箱", "公司主页", "行业", "实际地址", "注册地址", "公司状态", "法人名称",
        "注册资本", "注册时间", "核准时间", "工商注册号", "组织机构代码", "信用识别代码",
        "公司类型", "纳税人识别号", "营业期限", "登记机关", "经营范围"
    ]

    max = pd.read_sql("select max(id_cmp) from %s"%cptables, engine).ix[0, 0]
    max = 0 if max == None else max

    cmnames = pd.read_sql("select * from %s"%cpnames, engine)
    all = len(cmnames)
    cmnames = cmnames[cmnames['id'] > max]

    starttime = datetime.datetime.now()
    t=0
    for i in range(max, all):
        cmyname = cmnames['cmname'][i]
        if cmyname == None:
            pass
        else:
            print('正在搜索第%s个：%s'%(i,cmyname))
            keyword = quote(cmyname.encode("utf-8"))
            tycurl = "https://m.tianyancha.com/search?key=" + keyword + "&checkFrom=searchBox"
            # gettycfont()
            binfo = tyc_data(driver, tycurl, cmyname, maping)
            if binfo is None:
                print("Error" + binfo + "is None")
                pass
            else:
                if len(binfo) < 10:
                    print('未保存')
                else:
                    df = pd.DataFrame(binfo,index=index)
                    df = df.T

                    df['id_cmp'] = cmnames['id'][i]
                    try:
                        df.to_sql("%s"%cptables, engine, if_exists='append', index=False)
                    except:
                        pass
        a = random.randint(0, 0)
        t += 1
        endtime = datetime.datetime.now()
        s = (endtime - starttime).seconds
        print("采集第%s个完毕，用时%s秒， 等待"%(t,s) + str(a) + "秒\n\n")
        time.sleep(a)
    driver.quit()


if __name__ == '__main__':
    main('company_name', 'tyc_data')
