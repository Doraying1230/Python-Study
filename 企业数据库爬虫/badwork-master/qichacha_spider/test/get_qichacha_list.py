# -*- coding: utf-8 -*-
from lxml.html import fromstring
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class GetList:
    def __init__(self,html):
        self.tree = fromstring(html.decode('utf-8'))
    @property
    def get_url(self):
        get_url = self.tree.xpath('//*[@id="searchlist"]/table/tbody/tr[1]/td[2]/a')[0]
        url = 'http://www.qichacha.com'+get_url.get('href')
        return url

with open('winndoo_list.html','r') as f:
    html = f.read()
getlsit = GetList(html)
url = getlsit.get_url
print(url)