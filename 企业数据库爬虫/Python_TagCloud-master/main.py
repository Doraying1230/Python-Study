#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/1/17 15:43
# @Author  : Derek.S
# @Site    :
# @File    : main.py

import jieba
import xlrd
import re
import jieba.analyse
import codecs
from pytagcloud import create_tag_image, make_tags, LAYOUT_HORIZONTAL
from operator import itemgetter
import sys
from optparse import OptionParser
from openpyxl.workbook import Workbook
import os

sys.path.append("../")

USAGE = "python main.py [Excel File] -k [top k]"

parser = OptionParser(USAGE)
parser.add_option("-k", dest="topK")
opt, args = parser.parse_args()

if len(args) < 1:
    print(USAGE)
    sys.exit(1)

if opt.topK is None:
    topK = 10
else:
    topK = int(opt.topK)



def exceldata(file):
    """
    open excel file and read sheets
    :param file: excel file
    :return: string
    """
    try:
        book = xlrd.open_workbook(file)
        sheets = book.sheets()[0]
        dataset = []
        n = 0
        for row in range(sheets.nrows):
            col = sheets.cell(row, n).value
            recol = re.sub(r"""，|、|。|；|\.\.\.|#|（.*）|【.*】|;||\[.*\]|“|\(.*\)”""", "", col) #清洗汉字标点
            if row != 0:
                dataset.append(recol)
        return dataset
    except Exception as e:
        print(e)


def custom_word(str):
    """
    custiom dict cut str
    :param str: string
    :return: cut
    """
    jieba.load_userdict("lib/normal_dict.txt")  #加载自定义字典清洗数据
    sentence = jieba.cut(str, cut_all=False)
    with open("temp.txt", "a+", encoding="utf-8") as F:
        F.writelines("".join(sentence))


def keyword(filenname):
    """
    TF-IDF extract keyword
    :param filename: content file
    :return: tags
    """
    wb = Workbook()
    ws = wb.active
    with open(filenname, "rb") as F:
        content = F.read()
    jieba.analyse.set_stop_words("lib/stop_word.txt") #加载停用词
    tags = jieba.analyse.extract_tags(content, topK=topK, withWeight=1) # 提取关键词
    for tag in tags:
        print("tag: %s\t\t weight: %f" % (tag[0], tag[1]))
        ws.append([
            tag[0], tag[1]
        ])
    wb.save(filename="frequentness.xlsx")
    return tags



if __name__ == "__main__":
    excelname = args[0]
    seg_list = exceldata(excelname)
    for sentence in seg_list:
         custom_word(sentence)
    with codecs.open("kv.txt", "a+", "utf-8") as F:
        for tag in keyword("temp.txt"):
            kvstr = ("%s %f" % (tag[0], tag[1]))
            F.writelines(kvstr + "\n")
    F.close()
    with codecs.open("kv.txt", "r", "utf-8") as F:
        all_lines = F.readlines()
    F.close()
    wd = {}
    for eachline in all_lines:
        line = eachline.split(" ")
        wd[line[0]] = float(line[1].replace("\n", ""))

    swd = sorted(wd.items(), key=itemgetter(1), reverse=True)
    tags = make_tags(swd, minsize=50, maxsize=240)
    create_tag_image(tags, 'keyword.png', background=(0, 0, 0, 255), size=(3000, 1000), layout=LAYOUT_HORIZONTAL, fontname="YaHei")
    os.remove("kv.txt")
    os.remove("temp.txt")
