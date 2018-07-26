# encoding=utf-8
__author__ = 'Jonny'
__location__ = '北京'
__date__ = '2018/6/14 14:54'

import pymongo
from testCode.tianyacha.tianyacha import settings

def link_mongodb():
    mongo = pymongo.MongoClient(host=settings.MONGODB_HOST,port=settings.MONGODB_PORT,)
    mongodb  = mongo[settings.MONGODB_DANAME]
    sheet = mongodb[settings.MONGODB_COLLECTION]
    return sheet
