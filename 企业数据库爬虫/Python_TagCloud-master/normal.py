#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/20 16:25
# @Author  : Derek.S
# @Site    : 
# @File    : normal.py

import jieba
import re
import jieba.analyse
import codecs
from pytagcloud import create_tag_image, make_tags, LAYOUT_HORIZONTAL
from operator import itemgetter
import sys
from optparse import OptionParser
import os
import docx
from openpyxl.workbook import Workbook
import io
from fileencode import convert



sys.path.append("../")

USAGE = "python normal.py [Normal Text File] -k [top k]"

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


def worddate(filename):
    """
    proc docx data
    :param filename: docx file name
    :return: txt file
    """
    doc = docx.Document(filename)
    parag_num = 0
    with codecs.open("temp.txt", "a+", encoding="utf-8") as W:
        for para in doc.paragraphs:
            text = re.sub(
                r"""，|、|。|；|;|：|（|）|《|》|﹝|﹞|（|）|《|》""", "", para.text
            ).replace(" ", "").replace("\n", "")
            W.writelines(text)
            parag_num += 1
    W.close()

def txtdata(filename):
    """
    proc txt data
    :param filename: source file
    :return: None
    """
    convert(filename)
    with open(filename, "r", encoding="utf-8") as R:
        readfile = R.readlines()
    R.close()
    parag_num = 0
    with open("temp.txt", "a") as W1:
        for para in readfile:
            text = re.sub(
                r"""，|、|。|；|;|：|（|）|《|》|﹝|﹞|（|）|《|》|\s""", "", para
            ).replace(" ", "").replace("\n", "").replace("\r\n", "")
            W1.writelines(text)
            parag_num += 1
    W1.close()

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
    jieba.analyse.set_stop_words("lib/normal_stop_word.txt") #加载停用词
    tags = jieba.analyse.extract_tags(content, topK=topK, withWeight=1) # 提取关键词
    for tag in tags:
        print("tag: %s\t\t weight: %f" % (tag[0], tag[1]))
        ws.append([
            tag[0], tag[1]
        ])
    wb.save(filename="frequentness.xlsx")
    return tags

def custom_word(filename):
    """
    cut str
    :return: custom cut word temp txt file filename=temp_cut.txt
    """
    convert(filename)
    with open(filename, "r", encoding="utf-8") as W:
        wait_cut_word = W.read()
    W.close()
    sentence = jieba.cut(wait_cut_word, cut_all=False)
    with open("test.txt", "a+", encoding="utf-8") as test:
        test.write("\n".join((sentence)))

if __name__ == "__main__":

    filename = args[0]
    if str(filename).split(".")[-1] == "doc":
        print("Please Cover Doc to Docx")
    elif str(filename).split(".")[-1] == "docx":
        worddate(filename)
    elif str(filename).split(".")[-1] == "txt":
        txtdata(filename)
    else:
        print("Input File Error")
        sys.exit(1)
    custom_word("temp.txt")
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
    os.remove("test.txt")
