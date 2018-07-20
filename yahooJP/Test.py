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
# coding=utf-8
import requests
from bs4 import BeautifulSoup
# 获取html文档
def get_html(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    return response.text
# 获取笑话
def get_certain_joke(html):
    soup = BeautifulSoup(html, 'lxml')
    joke_content = soup.select('div.content')[0].get_text()
    return joke_content
exePath = r'C:\Users\asus\Anaconda3'
driver = webdriver.Firefox(exePath)
driver.implicitly_wait(3)  #这里设置智能等待10s
driver.get('https://www.baidu.com')
print (driver.title)
driver = webdriver.Firefox
driver.get("https://user.qzone.qq.com/1399636853/blog/")
print (driver)
# 给用户名的输入框标红
js1 = "var q=document.getElementById(\"user_name\");q.style.border=\"1px solid red\";"
js2 = "QZBlog.Util.PageIndexManager.goDirectPage(5);"
js3 = "var q=document.getElementsByClassName(\"c_tx \")[0];q.onclick()=\"QZBlog.Util.PageIndexManager.goDirectPage(5)\";q.onclick();"
# 调用js
driver.execute_scriptcript(js2)
print (driver)
driver.find_element_by_id("user_name").send_keys("username")
driver.find_element_by_id("user_pwd").send_keys("password")
driver.find_element_by_id("dl_an_submit").click()
url = "https://www.baidu.com"
driver.get(url);
driver.manage().window().setSize((600, 600));
time.sleep(30)
aaa = driver.find_element_by_class_name("")
driver.execute_script(js3)
aaa.click()
print (driver.page_source)
driver.quit();