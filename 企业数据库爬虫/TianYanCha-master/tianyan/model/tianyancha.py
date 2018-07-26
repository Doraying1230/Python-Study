#!/usr/bin/python
# -*-coding:utf-8-*- 
"""
@author: yugengde
@contact: yugengde@163.com
@file : tianyancha.py
@time: 2017/12/22 10:26
"""
from sqlalchemy import Column, String, DateTime, Integer

from . import Base


class Tianyancha(Base):
    __tablename__ = 'tianyancha'

    id = Column(Integer, primary_key=True)
    title = Column(String)  # 公司名称
    url = Column(String)  # 链接地址
    update_time = Column(DateTime)  # 更新时间

    def __init__(self, _id, title, url, update_time):
        self._id = _id
        self.title = title
        self.url = url
        self.update_time = update_time

