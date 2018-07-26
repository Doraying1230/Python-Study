import requests
import re
import xlrd
from lxml import etree
agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/171.37.193.68 Safari/537.36'
headers = {
    "User-Agent":agent
}
url="http://www.chinacopyright.org.cn/findsoftjosn.aspx"
postdata={
    "softnum":"",
    "softname":"",
    "softcopy":"%u817E%u8BAF"
}
html=requests.post(url,data=postdata,headers=headers).text
pattern = re.findall('\{(.*?)\}',html,re.S)
for each in pattern:
    print(each)
