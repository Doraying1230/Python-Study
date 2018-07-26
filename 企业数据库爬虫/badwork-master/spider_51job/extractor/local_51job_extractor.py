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
import json
import HTMLParser
import requests
import uuid
import time
from download_center.store.store_oss import StoreOSS

from store_new.util_store import SourceStore
import config

reload(sys)
sys.setdefaultencoding('utf8')


class JobExtractor(SpiderExtractor):
    """
    解析 搜狗微信文章
    """

    def __init__(self):
        super(JobExtractor, self).__init__()
        self.html_parser = HTMLParser.HTMLParser()
        # self.oss = StoreOSS(**config.EHCO_OSS)

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

    def list_extractor(self, html):
        """
        解析搜狗微信文章页面搜索的数据
        Args:
            html: 文本内容
            keyword: 关键词
            keyword_id : 关键词id
        Returns:
            数组: 每条为一个完整记录，记录由字典格式保存
        """
        list_results = list()
        try:
            tree = fromstring(html.decode('utf-8'))
            citys = tree.xpath('.//div[@class="e e4"][1]/div[@class="lkst"]')[0]
            urls = citys.xpath('./a/@href')
            city_names = citys.xpath('./a/text()')
            for u,c in zip(urls,city_names):

                list_results.append(
                    {
                        'city': c,
                        'url': u
                    })
        except Exception, e:
            # print traceback.format_exc()
            return -1
        return list_results

    def get_image_respone(self, url):
        '''
        下载指定url二进制的文件
        '''
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        }
        try:
            r = requests.get(url, timeout=20, stream=True, headers=headers)
            r.raise_for_status()
            # print '图片下载成功！url: {}'.format(url)
            time.sleep(1)
            return r.content
        except:
            print '图片下载失败！url: {}'.format(url)
            time.sleep(1)
            return None

    def up_to_server(self, respone, filename):
        '''
        将原图下载，并上传到阿里云服务器
        Args:
            url :图片的源地址
            filename:图片文件名
        '''
        # 设置文件目录
        web_folder = "brand/" + filename
        try:
            status = self.oss.put(web_folder, respone).status
            if status != 200:
                print '图片上传失败了'
            else:
                pass
        except:
            pass
        else:
            pass

    def format_img_url(self):
        img_head = 'http://website201710.oss-cn-shanghai.aliyuncs.com/brand/'
        img_name = '{}.jpg'.format(uuid.uuid1())
        aliyun_url = '{}{}'.format(img_head, img_name)
        return aliyun_url, img_name

    def detail_extractor(self, html, list_info):
        """
        解析头条文章的详情页
        html: 文章详情页
        """
        detail_results = dict()
        try:
            text = html.split("BASE_DATA")[1].split(";</script>")[0].strip()
            if text:
                category = text.split("chineseTag: '")[1].split("'")[0].strip()
                title = text.split("title: '")[1].split("'")[0].strip()
                content = text.split("content: '")[1].split("'")[0].strip()
                publish_time = text.split("time: '")[1].split("'")[0].strip()
                abstract = text.split("abstract: '")[1].split("'")[0].strip()
                tags = json.loads(text.split("tags: ")[1].split("],")[0].strip() + "]")

                html_content = self.html_parser.unescape(content)
                # etree =  fromstring(html_content)
                con = self.get_text(html_content)
                print(con)
                if len(con) < 50:
                    return -1

                # self.strip_a_tag(content)
                # imgs = content_ele.xpath('.//img')
                # for img in imgs:
                #     img.getparent().remove(img)

                # content = self.strip_atag_img_up_to_server(html_content)
                # content = etree.tostring(content_ele, encoding='utf-8', method='html').strip()

                detail_results['category'] = category
                detail_results['title'] = title
                detail_results['publish_time'] = publish_time
                detail_results['content'] = self.html_parser.unescape(content)
                detail_results['abstract'] = abstract
                detail_results['tags'] = ",".join([v['name'] for v in tags])

                # detail_results['url'] = list_info['url']
                # detail_results['title'] = list_info['title']
            detail_results.update(list_info)

        except:
            print traceback.format_exc()
            return -1
        return detail_results

    def strip_atag_img_up_to_server(self, html):
        """
        替换文中的所有img标签中的地址为自己的地址，并把文件上传到阿里云
        params html : 文本内容
        return : 修改好的文本内容
        """
        # images = {}
        try:
            tree = etree.HTML(html)
            # 修改a标签 **********
            links = tree.xpath('.//a')
            for link in links:
                text = link.text
                if text:
                    link.attrib.clear()
                    link.tag = 'b'
                else:
                    link.set("href", "")
            # 修改img链接*************
            img_urls = tree.xpath('.//img')
            img_urls = list(map(lambda x: x.get('src'), img_urls))
            # print(img_urls)
            ali_urls = []
            for img in img_urls:
                aliyun_url, filename = self.format_img_url()
                response = self.get_image_respone(img)
                if response:
                    self.up_to_server(response, filename)
                ali_urls.append(aliyun_url)
            img_ali_dict = {}
            for k, v in zip(img_urls, ali_urls):
                img_ali_dict[k] = v
            # print(img_ali_dict)
            for k, v in img_ali_dict.items():
                html = html.replace(k, v)
            return html
        except:
            pass
            # return images, tree

    def get_text(self, html):
        rc = []
        elem = etree.HTML(html)
        for node in elem.itertext():
            rc.append(node.strip())
        return ''.join(rc)

    # def get_text(self, elem):
    #     rc = []
    #     for node in elem.itertext():
    #         rc.append(node.strip())
    #     return ''.join(rc)

    def strip_a_tag(self, html):
        """
        去除html结构中的所有超链接

        返回去除后的html结构的字符串格式
        """
        # 清除所有的超链接
        try:
            tree = etree.HTML(html)
            links = tree.xpath('.//a')
            for link in links:
                text = link.text
                if text:
                    link.attrib.clear()
                    link.tag = 'b'
                else:
                    link.set("href", "")
            return tree
        except:
            return tree

    def judge_china(self, c_text):
        zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
        match = zhPattern.search(u"" + str(c_text))
        if match:
            return True
            # print '有中文：%s' % (match.group(0),)
        else:
            return False


def atest():
    from store_new import util_store
    from store_new.util_store import SourceStore

    # weixin_spider = {
    #     'host': '115.159.158.157',
    #     # 'host': '10.105.209.116',
    #     'user': 'sunxiang',
    #     'password': 'sx2017@',
    #     'db': 'spider_center'
    #
    # }

    with open('city_names.txt', 'r') as f:
        h = f.read()
    w = JobExtractor()
    r = w.list_extractor(h)
    for i in r[:-27]:
        print i
    # with open('city_names.txt', 'r') as f:
    #     h = f.read()
    # w = ToutiaoExtractor()
    # r = w.detail_extractor(h,{})
    # for i in r:
    #     print i, r[i]
    # for one in i:
    #     print one, i[one]
    # s = SourceStore(config.toutiao_content)
    # s.store_table_one(r, "news_0")

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
