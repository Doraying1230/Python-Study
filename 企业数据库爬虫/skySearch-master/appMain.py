__author__='callMeBin'
#-*-coding:utf-8-*-

'''
程序主方法
'''

import dataBaseTools
import skyEyesSearchAddress
import skyEyesSearchContent
import time

class appMain(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.tabelName = 'urlList'
		self.dbTool = dataBaseTools.dataBaseTool()


	#循环每一页得出每一页的URL
	def searchUrl(self):
		for i in range(1,3):#这里设置爬取多少页的URL
			try:
				spider = skyEyesSearchAddress.skyEyesSearchAddress(i)
				dataC = spider.getPage()
				libaray = spider.getContentAddress(dataC)
				spider.saveToDB(libaray)
				time.sleep(2)
			except Exception as e:
				raise e
		print('===================保存URL成功,开始爬取内容======================')



	#从数据库拿出所有url,并爬取内容
	def searchContent(self):
		try:
			url_str = "SELECT url from "+self.tabelName
			url_list = self.dbTool.execute(url_str)
			for i in url_list:
				spider = skyEyesSearchContent.skyEyesSearchContent(i[0])
				spider.getContentContent(spider.getPage())
				time.sleep(2)
			print('============================成功爬取内容==========================')
		except Exception as e:
			raise e


def main():
	app_start = appMain()
	app_start.searchUrl()
	app_start.searchContent()

if __name__=='__main__':
	main()
			
		
		