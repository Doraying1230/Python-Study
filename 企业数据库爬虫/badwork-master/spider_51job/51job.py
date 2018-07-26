#coding:utf-8
import requests
import MySQLdb
import config
from lxml.html import fromstring
from lxml import etree
from bs4 import BeautifulSoup
from download_center.store.store_mysql_pool import StoreMysqlPool
import sys
reload(sys)
sys.setdefaultencoding('utf8')

db = StoreMysqlPool(**config.EHCO_DB)

def get_txt_content(name):
    with open(name,'r') as f:
        content = f.read()
    return content

def get_url_content(url):
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 65.0.3325.146Safari / 537.36'
    }
    r = requests.get(url,headers=headers)
    r.encoding = 'gb2312'
    return r.text

def get_province():
    list_citys = []
    content = get_txt_content('citys.txt')
    tree = fromstring(content.decode('utf-8'))
    # content = get_url_content('http://jobs.51job.com')
    # tree = etree.HTML(content)

    citys = tree.xpath('.//div[@class="e e4"][1]/div[@class="lkst"]')[0]
    urls = citys.xpath('./a/@href')
    city_names = citys.xpath('./a/text()')
    for u, c in zip(urls, city_names):
        list_citys.append((u,c))
    # print(list_citys)
    return list_citys

def a_get_landmark_subway(url):
    all_landmark,all_subway = [],[]
    content = get_url_content(url)
    # content = get_txt_content('landmark_subway.txt')
    soup = BeautifulSoup(content,'html.parser')

    landmarks_list = soup.select('.lkst')[1]
    subway_list = soup.select('.lkst')[2]
    # print(subway_list)
    subways = subway_list.select('a')
    # print(subways)
    subway_urls = list(map(lambda x:x.get('href'),subways))
    subway_names = list(map(lambda x:x.text,subways))
    for u,s in zip(subway_urls,subway_names):
        all_subway.append((u,s))
    # print(subway_names)
    landmarks = landmarks_list.select('a')
    urls = list(map(lambda x:x.get('href'),landmarks))
    landmark_place = list(map(lambda x:x.text,landmarks))
    for u,l in zip(urls,landmark_place):
        all_landmark.append((u,l))
    return all_landmark,all_subway
# landmark,subway = a_get_landmark_subway('http://jobs.51job.com/guangzhou/')
# print(landmark)
# print(subway)

# def b_get_landmark_subway(url):
#     all_landmark, all_subway = [], []
#     content = get_url_content(url)
#     tree = fromstring(content.decode('utf-8'))
#     landmark_list = tree.xpath("/html/body/div[3]/div[2]/div[3]/div[1]")
#     for land in landmark_list:
#         print(land)

# b_get_landmark_subway('http://jobs.51job.com/beijing/')


def content_to_db(url,city,province):
    landmark, subway = a_get_landmark_subway(url)

    for l in landmark:
        t, d, k = a_get_tdk(city=city, land=l[1])
        sql = "insert into `51job` (`province`,`city`,`landmark`,`title`,`description`,`keywords`,`url`) values ('{}','{}','{}','{}','{}','{}','{}')".format(province,city,MySQLdb.escape_string(str(l[1])),t,d,k,str(l[0]))
        print(sql)
        print("-----------------------")
        db.do(sql)
    for s in subway:
        t,d,k = a_get_tdk(city=city,land=s[1])
        sql = "insert into `51job`(`province`,`city`,`subway`,`title`,`description`,`keywords`,`url`) values ('{}','{}','{}','{}','{}','{}','{}')".format(province,city,MySQLdb.escape_string(str(s[1])),t,d,k,str(s[0]))
        db.do(sql)
    print('done')
def a_get_tdk(city='',land=''):
    t = '【{}招聘_最新{}招聘信息】-前程无忧'.format(city+land,city+land)
    d = '前程无忧为您提供最新最全的{}招聘、求职信息，找工作、找人才就上{}前程无忧招聘专区！掌握前程，职场无忧！'.format(city+land,city)
    k = '{},{}招聘,最新{}招聘信息'.format(city+land,city+land,city+land)
    return t,d,k




def insert_db(url,province):
    all_citys = []
    content = get_url_content(url)
    soup = BeautifulSoup(content, 'html.parser')
    city_list = soup.select('.lkst')[0]
    citys = city_list.select('a')
    city_names = list(map(lambda x: x.text, citys))
    city_urls = list(map(lambda x: x.get('href'), citys))
    for n,u in zip(city_names,city_urls):
        all_citys.append((u,n))
    for city in all_citys[1:]:
        sql = """insert into `51job` (`province`,`city`,`url`) values ('{}','{}','{}')""".format(province,city[1],city[0])
        db.do(sql)
    print('done')
content_to_db('http://jobs.51job.com/tianjin/','天津','')
# insert_db('http://jobs.51job.com/xining/','青海')