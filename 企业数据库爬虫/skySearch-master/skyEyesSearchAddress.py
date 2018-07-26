__author__='callMeBin'
#encoding=utf-8

'''
目标：利用天眼查查询公司的相关信息
'''

import requests
from bs4 import BeautifulSoup
import re
import codecs
import dataBaseTools
import time

class skyEyesSearchAddress(object):
	def __init__(self,id=1):
		self.page = 'p'+str(id)
		self.BASE_URL = r'https://shaoguan.tianyancha.com/search/'+self.page+'?key=%E9%9F%B6%E5%85%B3'
		self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
						'Host':'www.tianyancha.com',
						'Connection':'keep-alive',
						'Cache-Control':'max-age=0',
						'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
						'Referer':'https://www.tianyancha.com/search?key=%E9%9F%B6%E5%85%B3',
						'Accept-Encoding':'gzip, deflate, sdch, br',
						'Accept-Language':'zh-CN,zh;q=0.8',
						#'Cookie':'aliyungf_tc=AQAAAHmj61ioogEAnCcP2vYdkAKxojqQ; csrfToken=3nEJ94JQJWO7qK2YsWJikj27; TYCID=c8216b7083db11e89c00e9be8f48d4f7; undefined=c8216b7083db11e89c00e9be8f48d4f7; ssuid=974676856; token=941f17a186b9459b8426a982bbbaa785; _utm=613873172ed24a1fa7e297039b2d6309; RTYCID=2cc9d3fa3a0b43c1a27d651ea5270a7b; bannerFlag=true; tyc-user-info=%257B%2522isExpired%2522%253A%25220%2522%252C%2522claimDetailLevel%2522%253A%252220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTExNTg0ODQzNSIsImlhdCI6MTUzMTc5NzA5MCwiZXhwIjoxNTQ3MzQ5MDkwfQ.hPO5Hhb5O3HmNLkiBzBEPJMgBWboBGWeYxl03OwSQI1RtXtxhNMpFfnXlS-RBRG0sGK18ge_jTqZN8H_BLHixw%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25225%2522%252C%2522surday%2522%253A%2522361%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%252229%2522%252C%2522mobile%2522%253A%252215115848435%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTExNTg0ODQzNSIsImlhdCI6MTUzMTc5NzA5MCwiZXhwIjoxNTQ3MzQ5MDkwfQ.hPO5Hhb5O3HmNLkiBzBEPJMgBWboBGWeYxl03OwSQI1RtXtxhNMpFfnXlS-RBRG0sGK18ge_jTqZN8H_BLHixw; _ga=GA1.2.861720786.1531701302; _gid=GA1.2.483185215.1531701302; _gat_gtag_UA_122238368_3=1; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1531701300,1531701317,1531791124,1531793895; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1531797098'

						}
		self.dbTool = dataBaseTools.dataBaseTool()
		self.tabelName = 'urlList'
		print(self.BASE_URL)

	#返回页面内容
	def getPage(self):
		data = requests.get(self.BASE_URL,headers=self.headers)
		dataContent = str(data.content,'utf-8')
		#print(data.encoding)
		#print(str(data.content,'utf-8'))
		return dataContent

	#传入页面，筛选Address	
	def getContentAddress(self,dataContent):
		#初始化SOUP实例对象
		soup = BeautifulSoup(dataContent,'lxml')
		#找出result-list
		result_list_soup = soup.find('div',attrs={'class':'result-list'})
		#print(result_list_soup)
		libarayAddress = []
		for item in result_list_soup.find_all('div',attrs={'class':'search-result-single'}):
			#从div中逐层下找
			div_content = item.find('div',attrs={'class':'content'})
			div_header = div_content.find('div',attrs={'class':'header'})
			div_url = div_header.find('a').get('href')
			libarayAddress.append(div_url)
			print(div_url)
		return libarayAddress

	#保存到数据库
	def saveToDB(self,libarayAddress):
		print("进入数据库")
		try:
			for item in libarayAddress:
				print(item)
				timeStr = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
				insert_str = "INSERT INTO "+self.tabelName+"(url,time) VALUES('%s','%s')"%(str(item),timeStr)
				print(insert_str)
				self.dbTool.execute_insert(insert_str)
			print("保存成功")
		except Exception as e:
			raise e

	#控制爬取进度
	#def process(self):




def main():
	#getContentAddress(getPage(BASE_URL))
	spider = skyEyesSearchAddress(id=2)
	dataC = spider.getPage()
	libaray = spider.getContentAddress(dataC)
	spider.saveToDB(libaray)

if __name__=='__main__':
	main()