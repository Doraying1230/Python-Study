# C:\Users\asus\Desktop
# f = open('aaa.txt')txt
# f.read()
import sys
import re
import os
import time
import webbrowser
import xlwt
import requests
import xlrd
from xlutils.copy import copy
from selenium import webdriver
i = 0
pathaaa =r"C:\Users\asus\Desktop\dd.xls"
filePath = r"C:\Users\asus\Desktop\bookmarks_2018_3_19.html"
# filePath = r"C:\Users\asus\Desktop\aaa.txt"
f = open(filePath,'r',encoding="utf-8").read()
# print(f)
regexStr = r"(?<=HREF=\").+?(?=\")|(?<=HREF=\').+?(?=\')|(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
refList = re.findall(regexStr, f)
# print(refList)

# driver = webdriver.Chrome()
# driver.maximize_window()  # 最大化浏览器
# driver.implicitly_wait(2) # 设置隐式时间等待
i = 0

pathaaa =r"C:\Users\asus\Desktop\dd.xls"
workbook = xlwt.Workbook(encoding='utf-8')
booksheet = workbook.add_sheet('存储URL', cell_overwrite_ok=True)
for url in refList:
    print(url)
    i += 1
    print (i)
    # time.sleep(1)

    booksheet.write(i, 0, url)
    # webbrowser.open(url)
    # webbrowser.Chrome.open_new_tab(url)
    # webdriver.Chrome.close(url)
    # driver.close()
# print(fileStr)

workbook.save(pathaaa)