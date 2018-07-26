#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/22 10:07
# @Author  : Derek.S
# @Site    :
# @File    : similarity.py

import jieba.posseg
import re
import codecs
import sys
import os
import docx
from optparse import OptionParser
from gensim import corpora, models, similarities
import logging

from fileencode import convert

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

sys.path.append("../")

USAGE = "python similarity.py [File1] [File2]"

parser = OptionParser(USAGE)
opts, args = parser.parse_args()

#print(args[1][0]) #测试

if len(args) < 2:
    print(USAGE)
    sys.exit(1)


def worddata(filename, tempname):
    """
    proc docx data
    :param filename: docx file name
    :param tempanme: docx cover to normal text
    :return: None
    """
    doc = docx.Document(filename)
    parag_num = 0
    with codecs.open(tempname, "a+", encoding="utf-8") as W1:
        for para in doc.paragraphs:
            text = re.sub(
                r"""，|、|。|；|;|：|（|）|《|》|﹝|﹞|（|）|《|》""", "", para.text
            ).replace(" ", "").replace("\n", "")
            W1.writelines(text)
            parag_num += 1
    W1.close()


def cutword(filename):
    """
    jieba cut word
    :param filename: worddate normal text file
    :param tempname: cut result file
    :return: cut word list
    """
    result = []
    convert(filename)
    with codecs.open(filename, "r", encoding="utf-8") as W:
        wait_cut_word = W.read()
    W.close()
    with codecs.open("lib/similarity_stop_word.txt", "r", encoding="utf-8") as W:
        stop_word = W.readlines()
    W.close()
    stop_flag = ['x', 'c', 'u','d', 'p', 't', 'uj', 'm', 'f', 'r']

    words = jieba.posseg.cut(wait_cut_word)
    for word, flag in words:
        if flag not in stop_flag and word not in stop_word:
            result.append(word)
    return result


def txtdata(filename, tempname):
    """
    proc txt data
    :param filename: source file
    :param tempname: rinse file
    :return: None
    """
    convert(filename)
    with codecs.open(filename, "r", encoding="utf-8") as R:
        readfile = R.readlines()
    R.close()
    parag_num = 0
    with codecs.open(tempname, "a", encoding="utf-8") as W1:
        for para in readfile:
            text = re.sub(
                r"""，|、|。|；|;|：|（|）|《|》|﹝|﹞|（|）|《|》|\s""", "", para
            ).replace(" ", "").replace("\n", "").replace("\r\n", "")
            W1.writelines(text)
            parag_num += 1
    W1.close()


def similarityproc(file1name, temp1name, file2name, temp2name):
    """
    similarity proc
    :param file1name: source file 1 name
    :param temp1name: temp file 1 name
    :param file2name: source file 2 name
    :param temp2name: temp file 2 name
    :return: similarity
    """
    file1_expanded_name = str(file1name).split(".")[-1]
    file2_expanded_name = str(file2name).split(".")[-1]
    if file1_expanded_name == "docx":
        worddata(file1name, temp1name)
    elif file1_expanded_name == "txt":
        txtdata(file1name, temp1name)
    else:
        return "Input File error"
    if file2_expanded_name == "docx":
        worddata(file2name, temp2name)
    elif file2_expanded_name == "txt":
        txtdata(file2name, temp2name)
    else:
        return "Input File error"
    corpus.append(cutword(temp1name))
    corpus.append([''])
    dictionary = corpora.Dictionary(corpus)  # 生成字典
    doc_vectors = [dictionary.doc2bow(text) for text in corpus]  # 转向量
    tfidf = models.TfidfModel(doc_vectors)
    tfidf_vectors = tfidf[doc_vectors]
    query = cutword(temp2name)
    query_bow = dictionary.doc2bow(query)
    index = similarities.MatrixSimilarity(tfidf_vectors)
    # index = similarities.Similarity("/", tfidf_vectors[0], 106)
    sims = index[query_bow]
    return list(enumerate(sims))[0]


if __name__ == "__main__":
    file1name = args[0]
    file2name = args[1]
    file1split = str(file1name).split(".")[-1]
    file2split = str(file2name).split(".")[-1]
    temp1name = str(file1name).split(".")[0] + ".temp.txt"
    temp2name = str(file2name).split(".")[0] + ".temp.txt"
    corpus = []
    if file1split == "doc" or file2split == "doc":
        print("Please Cover Doc to Docx")
    elif file1split == "docx" or file2split == "docx" or file1split == "txt" or file2split == "txt":
        print(similarityproc(file1name, temp1name, file2name, temp2name))
    for file in (temp1name, temp2name):
        os.remove(file)
