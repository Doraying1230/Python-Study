#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/25 22:07
# @Author  : Derek.S
# @Site    : 
# @File    : fileencode.py

import chardet
import codecs


def convert(filename):
    """
    convert file encode to utf-8
    :param filename: filename
    :return: newfile
    """
    content = open(filename, "rb").read()
    source_Encoding = chardet.detect(content)['encoding']
    if source_Encoding == "GB2312":
        with codecs.open(filename, "r", encoding="GB18030") as source_File:
            source_Data = source_File.read()
    else:
        with codecs.open(filename, "r", encoding=source_Encoding) as source_File:
            source_Data = source_File.read()
    with codecs.open(filename, "w", encoding="utf-8") as new_utf8_File:
        new_utf8_File.write(source_Data)
