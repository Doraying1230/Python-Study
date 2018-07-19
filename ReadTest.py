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

i = 0
def redStr(fileStr):
    link_list = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", fileStr)
    for url in link_list:
        i=i+1
        time.sleep(3)
        print(url)
        webbrowser.open(url)
        booksheet.write(i,0,url)

pathaaa =r"C:\Users\asus\Desktop\dd.xls"
# filePath = r"C:\Users\asus\Desktop\bookmarks_2018_3_19.html"
filePath = r"C:\Users\asus\Desktop\aaa.txt"
workbook = xlwt.Workbook(encoding='utf-8')
booksheet = workbook.add_sheet('存储URL', cell_overwrite_ok=True)
f = open(filePath).read()
refList = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", f)
for url in refList:
    time.sleep(3)
    webbrowser.open(url)
def readOpenFile(filePath):
    with open(filePath, 'rb') as f:
     fileStr = f.read()
     link_list = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", fileStr)
     for url in link_list:
        i = i + 1
        time.sleep(3)
        print(url)
        webbrowser.open(url)
        booksheet.write(i, 0, url)

    # redStr(fileStr)
    # line = f.readline()  # 调用文件的 readline()方法
    # while line:
    #     # print line
    #     # 后面跟 ',' 将忽略换行符
    #     # print(line, end = '')　　　# 在 Python 3中使用
    #     redStr(line)
    #     line = f.readline()
    #
    # f.close()
    # redStr(f.read())
    # for line in f:
    #     print (line)
    #     self.redStr(line)
    workbook.save(pathaaa)
def getUrl(html):
    reg = r'href="(*.?)" add'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist
def write_xls(self,path,text,nrow,ncol):
    rb=xlrd.open_workbook(path)
    rs = rb.sheet_by_index(0)
    wb = copy(rb)
    ws = wb.get_sheet(0)
    ws.write(nrow, ncol,text)
    wb.save(path)
# print(fileStr)