# C:\Users\asus\Desktop
# f = open('aaa.txt')txt
# f.read()
# -*- coding: utf-8 -*-
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
    """get the content of the url"""
    response = requests.get(url)
    response.encoding = 'utf-8'
    
    return response.text
# 获取笑话
def get_certain_joke(html):
    """get the joke of the html"""
    soup = BeautifulSoup(html, 'lxml')
    joke_content = soup.select('div.content')[0].get_text()
    return joke_content
i = 0
pathaaa =r"C:\Users\asus\Desktop\dd.xls"
workbook = xlwt.Workbook(encoding='utf-8')
booksheet = workbook.add_sheet('存储URL', cell_overwrite_ok=True)
baseDomain = "https://tieba.baidu.com/p/2343541131?see_lz=1&pn="
for index in range(1, 7):
    url = baseDomain + str(index)
    print(url)
    html = get_html(url)
    link_list = re.findall(r"(《.*?》)", html)
    for title in link_list:
        i = i + 1
        print(title)
        booksheet.write(i, 0, title)
workbook.save(pathaaa)
