# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class XitiloadItem(scrapy.Item):
    version = Field();#版本
    grade = Field();#年级
    course = Field();#学科
    section = Field()#章节
    type = Field()#题型
    title = Field()#题目
    originalTitleUrl = Field()#题目中的原始url
    selects = Field()#选项
    originaSelectsUrl= Field()#选项的原始url
    answer = Field()#答案
    originaAnswerUrl= Field()#答案的原始url
    knowledgePoint = Field()#知识点
    originaKnowledgePoint= Field()#知识点的原始url
    analysis  = Field()#解析
    originaAnalysisUrl= Field()
    detailUrl = Field()#详情页的URL
    difficultDEgree = Field()#试题的难易程度

