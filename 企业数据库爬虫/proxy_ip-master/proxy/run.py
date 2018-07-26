#coding:utf-8
import time
import os
name_list=['kuaidaili','kxdaili','66ipcn','ip181','xicidaili','haodaili','goubanjia']

#scrapy crawl kuaidaili
#scrapy crawl kxdaili
#scrapy crawl 66ipcn
#scrapy crawl ip181


for name in name_list:
    os.system('scrapy crawl %s' % name)
    time.sleep(10)
