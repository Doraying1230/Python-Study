# -*- coding: utf-8 -*-
"""
Created 2017-11-21
@author: Ehco1996
"""

import sys
import os
import re
from download_center.new_spider.spider.spider import SpiderExtractor
from lxml import etree
import traceback
from lxml.html import fromstring
from get_qichacha_detail import GetAllInfo
from get_qichacha_list import GetList
from store_new.util_store import SourceStore
import config


reload(sys)
sys.setdefaultencoding('utf8')


class Wx_extractor(SpiderExtractor):
    """
    解析 搜狗微信文章
    """

    def __init__(self):
        super(Wx_extractor, self).__init__()

    def page_extractor(self, html):
        """
        解析搜狗微信搜索文章结果的页数
        Args:
            html: 文本内容
        Returns:
            int： 结果页码数量
                  -1 时错误
        """
        try:
            tree = fromstring(html.decode('utf-8'))
            pageNum = tree.xpath('//*[@id="pagebar_container"]//a')
            return len(pageNum)
        except:
            return -1

    def list_extractor(self, html, keyword):
        """
        解析搜狗微信文章页面搜索的数据
        Args:
            html: 文本内容
            keyword: 关键词
            keyword_id : 关键词id
        Returns:
            数组: 每条为一个完整记录，记录由字典格式保存
        """
        results = list()
        try:
            get_list = GetList(html)
            url = get_list.get_url
            results.append({'url': str(url),
                            'keyword': keyword
                            })
        except Exception, e:
            # print traceback.format_exc()
            return -1
        return results

    def detail_extractor(self, html, info):
        """
        解析微信文章的详情页
        info: list页面解析出来的信息
        """
        try:
            get_allinfo = GetAllInfo(html)
            detail_dict = get_allinfo.get_detail
            detail_dict.update(info)
            return detail_dict
        except:
            # print traceback.format_exc()
            return -1

def atest():
    # from store_new import util_store
    import requests
    # weixin_spider = {
    #     'host': '115.159.158.157',
    #     # 'host': '10.105.209.116',
    #     'user': 'sunxiang',
    #     'password': 'sx2017@',
    #     'db': 'spider_center'
    #
    # }

    with open('xiaomi.html', 'r') as f:
        h = f.read()
    # headers = {
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    # }
    # h = requests.get('http://www.qichacha.com/firm_9cce0780ab7644008b73bc2120479d31.html',headers=headers)
    w = Wx_extractor()
    r = w.detail_extractor(h, {})
    for i in r:
        print i,':', r[i]
        # for one in i:
        #     print one, i[one]

    # create_table_sql = """
    # CREATE TABLE `news_{}` (
    #       `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
    #       `title` VARCHAR(512) NOT NULL COMMENT '标题',
    #       `summary` TEXT NOT NULL COMMENT '概要',
    #       `content` LONGTEXT NOT NULL COMMENT '文章内容html',
    #       `wechat_name` VARCHAR(255) NOT NULL COMMENT '微信名称',
    #       `wechat_num` VARCHAR(255) NOT NULL COMMENT '微信公众号',
    #       `keyword` VARCHAR(100) NOT NULL COMMENT '关键词',
    #       `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    #       PRIMARY KEY (`id`)
    #     ) ENGINE=INNODB DEFAULT CHARSET=utf8;
    # """.format(1)
    # print create_table_sql


if __name__ == '__main__':
    atest()
