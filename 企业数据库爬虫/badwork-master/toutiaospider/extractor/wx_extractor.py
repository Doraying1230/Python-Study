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

    def list_extractor(self, html, keyword, keyword_id):
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
            tree = fromstring(html.decode('utf-8', 'ignore'))

            ul = tree.xpath('.//ul[@class="news-list"]/li')
            if ul:
                pass
            else:
                ul = tree.xpath('//*[@id="main"]/div[4]/ul//li')

            for li in ul:
                url = li.xpath('./div[@class="txt-box"][1]/h3/a/@href')[0]
                # url = li.xpath('descendant::div[@class="txt-box"][1]/h3/a/@href')[0]

                title = li.xpath('.//div[@class="txt-box"][1]/h3')[0].xpath('string(.)').strip()
                we_name = li.xpath('./div[@class="txt-box"][1]/div/a/text()')[0]
                try:
                    summary = li.xpath('.//p[@class="txt-info"][1]')[0].xpath(
                        'string(.)').strip().replace('\n', '').replace(' ', '')
                except:
                    summary = ''
                results.append({'url': str(url),
                                "we_name": str(we_name),
                                "title": str(title),
                                'summary': str(summary),
                                'keyword': keyword,
                                'keyword_id': keyword_id, })
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
            tree = fromstring(html.decode('utf-8'))
            title = tree.xpath(
                '//*[@id="activity-name"]/text()')[0].replace(' ', '').replace('\n', '')
            is_original = len(tree.xpath('//*[@id="copyright_logo"]'))
            publish_time = tree.xpath('//*[@id="post-date"]/text()')[0]
            wechat_name = tree.xpath('//*[@id="post-user"]/text()')[0]

            wechat_num = ""
            try:
                wechat_num = tree.xpath('//*[@id="js_profile_qrcode"]/div/p[1]/span/text()')[0]
            except:
                pass
            content_ele = tree.xpath('//*[@id="js_content"]')[0]
            con = self.get_text(content_ele)

            if len(con) < 50:
                return -1

            self.strip_a_tag(content_ele)
            imgs = content_ele.xpath('.//img')
            for img in imgs:
                img.getparent().remove(img)

            # self.strip_img(content_ele)
            content = etree.tostring(content_ele, encoding='utf-8', method='html').strip()

            res = {'title': str(title),
                   'is_original': is_original,
                   'publish_time': str(publish_time),
                   'wechat_name': str(wechat_name),
                   'wechat_num': str(wechat_num),
                   'content': content
                   }
            res.update(info)
            return res
        except:
            # print traceback.format_exc()
            return -1

    def strip_img(self, tree):
        """
        替换文中的所有img标签中的地址为自己的地址
        return dict {'old_url':'new_ulr'}
               tree html element
        """
        # images = {}
        # try:
        #     imgs = tree.xpath('.//img')
        #     print len(imgs)
        #     for img in imgs:
        #         tree.remove(img)
                # img.clear()
                # img.remove()
            #     temp_src = img.get('src')
            #     new_url = Image_to_server().get_new_url()
            #     img.set('src', new_url)
            #     images[temp_src] = new_url
            # return images, tree
        except:
            pass
            # return images, tree

    def get_text(self, elem):
        rc = []
        for node in elem.itertext():
            rc.append(node.strip())
        return ''.join(rc)

    def strip_a_tag(self, tree):
        """
        去除html结构中的所有超链接

        返回去除后的html结构的字符串格式
        """
        # 清除所有的超链接
        try:
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


def test():
    from store_new import util_store

    # weixin_spider = {
    #     'host': '115.159.158.157',
    #     # 'host': '10.105.209.116',
    #     'user': 'sunxiang',
    #     'password': 'sx2017@',
    #     'db': 'spider_center'
    #
    # }

    with open('detail.txt', 'r') as f:
        h = f.read()
    w = Wx_extractor()
    r = w.detail_extractor(h, {})
    for i in r:
        print i, r[i]
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
    test()
