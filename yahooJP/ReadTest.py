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
import urllib
from xlutils.copy import copy
from selenium import webdriver
import lib
import  os
import pymysql
# chromedriver = r"C:\Users\asus\AppData\Local\Google\Chrome\Application\chromedriver.exe"
# os.environ["webdriver.chrome.driver"] = chromedriver  geckodriver
exePath = r'C:\Users\asus\Anaconda3'
# driver = webdriver.Chrome(exePath)
driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.implicitly_wait(3)  #这里设置智能等待10s
print(driver.page_source)
print(driver.title)
