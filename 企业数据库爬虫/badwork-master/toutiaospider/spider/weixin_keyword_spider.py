# -*- coding: utf-8 -*-
"""
 @Time: 2017-11-20
 @Author: Ehco1996
"""
import os
import sys
import traceback
import random
import time
from urllib import quote
from datetime import datetime

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(PROJECT_PATH)
sys.path.append(os.path.join(PROJECT_PATH, 'website_wx'))

import config
from download_center.new_spider.util.util_md5 import UtilMD5
from download_center.new_spider.downloader.downloader import SpiderRequest
from download_center.util.util_log import UtilLogger
from download_center.new_spider.util.util_useragent import UtilUseragent
from download_center.store.store_mysql import StoreMysql

from basespider_sign import BaseSpiderSign
from extractor.wx_extractor import Wx_extractor
from store_new.util_store import SourceStore
import re
from spider.decorator import fn_timer

reload(sys)
sys.setdefaultencoding('utf8')


class WxSpider(BaseSpiderSign):

    """
    爬取微信文章
    流程：
        1 从数据库检索出不同的关键词
        2 从入口：搜狗微信搜索搜索关键词并解析列表页
            入口url：http://weixin.sogou.com/weixin?type=2&s_from=input&query=%E4%BD%A0%E5%93%88&ie=utf8&_sug_=y&_sug_type_=&w=01019900&sut=2889&sst0=1511337321983&lkt=0%2C0%2C0
        3 解析列表业码后得出该关键词对应文章的 页码数量  从而拼出剩下的页码url
        4 解析列表页内的文章 链接、摘要，传入 详情页的解析器
        5 解析微信内的文章最后存入数据库

    """

    def __init__(self):
        super(WxSpider, self).__init__()
        # 必须指定self.log
        self.log = UtilLogger('WxSpider',
                              os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log_WxSpider.log'))

        self.log_record = UtilLogger('SourceSpider',
                              os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log_SourceSpider.log'))

        self.ext = Wx_extractor()
        # self.new_store = SourceStore(config.TEST_DB)
        self.step = 1000
        self.sended_queue_maxsize = 2000

        self.spider_count = 0
        self.repeat_count = 0

    def get_user_password(self):
        return 'zhouhao', 'zhspider'
        # return 'xuliang', 'xlspider'

    def send_get_spider(self, urls):
        """
        封装好 GET request请求，并发送到下载队列
        """
        basic_request = SpiderRequest(headers={'User-Agent': random.choice(self.pc_user_agents)},
                                      urls=urls, config={"redirect": 1})
        self.sending_queue.put_nowait(basic_request)

    def start_requests(self):
        try:
            while 1:
                if self.sended_queue.qsize() < self.sended_queue_maxsize and self.sending_queue.qsize() < self.sended_queue_maxsize \
                        and self.response_queue.qsize() < self.sended_queue_maxsize and self.store_queue.qsize() < self.sended_queue_maxsize:
                    db = StoreMysql(**config.weixin_content)
                    source = SourceStore(config.weixin_content)
                    update_time = str(datetime.now()).split(".")[0]
                    sql = "select id, keyword from content_center.keywords order by update_time asc,  priority desc  limit 0, {};".format(self.step)
                    rows = db.query(sql)
                    self.log.info("datetime:{},task_results length:{}".format(datetime.now(), len(rows)))
                    ids = list()
                    if rows:
                        for word in rows:
                            task_id = word[0]
                            ids.append({"id": task_id, "update_time": update_time})

                            keyword = word[1]
                            send_url = 'http://weixin.sogou.com/weixin?type=2&s_from=input&query={}&ie=utf8&_sug_=y&_sug_type_='.format(
                                keyword)
                            urls = [{"url": send_url, "type": 1, "ext_type": 3, 'keyword': keyword, 'task_id': task_id,
                                     'unique_key': self.get_unique_key()}]
                            self.send_get_spider(urls)

                        source.store_table(ids, "keywords", type=2, field="id")
                    db.close()
                time.sleep(60 * 2)
        except Exception:
            print traceback.format_exc()

    def get_stores(self):
        """
        可定义多个数据源
        :return:
        """
        stores = list()
        stores.append(SourceStore(config.weixin_spider))
        self.stores = stores
        return stores

    def deal_response_results_status(self, task_status, url, result, request):
        """
            处理 task_status 是2,3的任务  重试返回数组， 若重试需切换headers内容需自行定义
        :param task_status:
        :param url:
        :param result:
        :param request:
        :return:
        """
        if task_status == '2':
            ext_type = url["ext_type"]
            if ext_type == 3:
                self.deal_response_page(url, result['result'])
            elif ext_type == 1:
                self.deal_response_list(url, result['result'])
            elif ext_type == 2:
                self.deal_response_detail(url, result['result'])
        else:
            self.log.info("status is 3 url:{}; headers:{}; config:{}".format(url["url"], request.headers, request.config))

    def deal_response_page(self, url, html):
        try:
            keyword = url['keyword']
            task_id = url['task_id']
            page = self.ext.page_extractor(html)
            if page == -1:
                self.log.info("deal_response_page  exception url:{}".format(url["url"]))
            else:
                # 最多10 页
                page_c = 10
                if page < 10:
                    page_c = page
                for i in range(1, page_c + 1):
                    send_url = "http://weixin.sogou.com/weixin?query={}&_sug_type_=&s_from=input&_sug_=n&type=2&page={}&ie=utf8".format(keyword, i)
                    urls = [{"url": send_url, "type": 1, "ext_type": 1, 'keyword': keyword, 'task_id': task_id,
                             'unique_key': self.get_unique_key() }]
                    self.send_get_spider(urls)
        except:
            print 'ext page count error!{}'.format(url)

    # @fn_timer
    def deal_response_list(self, url, html):
        try:
            keyword = url['keyword']
            task_id = url['task_id']
            # 解析列表页逻辑：
            info_list = self.ext.list_extractor(html, keyword, task_id)
            if info_list == -1:
                self.log.info("deal_response_list  exception url:{}".format(url["url"]))
            else:
                self.store_queue.put({"result": info_list, "type": 1})
        except:
            print(traceback.format_exc())

    # @fn_timer
    def deal_response_detail(self, url, html):
        try:
            info = url['info']
            info.pop("we_name")
            res = self.ext.detail_extractor(html, info)
            if res != -1:
                self.store_queue.put({"result": res, "type": 2})
            else:
                self.log.info("deal_response_detail  = -1 url:{}".format(url["url"]))
        except:
            print(traceback.format_exc())

    def to_store_results(self, results, stores):
        """
            type 1  列表页 title name  去重
                2  详情页 数据
        :param results:
        :param stores:
        :return:
        """
        try:
            result = results["result"]
            type = results["type"]
            if type == 1:
                log_start = time.time()
                for info in result:
                    log_md5 = UtilMD5.md5(info["title"] + info["we_name"])
                    sql = "insert ignore into spider_log(md5, type) values('{}', '1')".format(str(log_md5))
                    s_id = stores[0].insert_row(sql)
                    if s_id > 0:
                        self.spider_count += 1
                        urls = [{"url": info['url'], "type": 1, "ext_type": 2, 'info': info, 'unique_key': self.get_unique_key(), }]
                        self.send_get_spider(urls)
                    else:
                        self.repeat_count += 1
                        # self.log_record.info("spider_log title:{}".format(info["title"]))

                if self.spider_count > 1000:
                    self.log_record.info("spider_count:{}".format(self.spider_count))
                    self.spider_count = 0
                if self.repeat_count > 1000:
                    self.log_record.info("repeat_count:{}".format(self.repeat_count))
                    self.repeat_count = 0

                t_inter = int(time.time() - log_start)
                if t_inter > 5:
                    self.log_record.info("spider_log time:{}".format(t_inter))
            elif type == 2:
                # data_start = time.time()
                data = result
                ke_id = str(data["keyword_id"])[-1:]
                spider_weixin = 'spider_weixin_{}'.format(ke_id)
                spider_weixin_content = 'spider_weixin_content_{}'.format(ke_id)

                if not self.judge_china(data["content"]):
                    # self.log_record.info("spider_weixin_lang add")
                    return
                    # spider_weixin = "spider_weixin_lang"
                    # spider_weixin_content = "spider_weixin_content_lang"

                weixin_content = {"summary": data.pop("summary", ""), "content": data.pop("content", ""), "keyword_id": data.get("keyword_id", 0), "keyword": data.get("keyword", "")}
                s_id = stores[0].store_table_one(data, spider_weixin)
                if s_id > 0:
                    weixin_content["id"] = s_id
                    stores[0].store_table_one(weixin_content, spider_weixin_content)

                # self.log_record.info("data_weixin time:{}".format(time.time() - data_start))
        except:
            print(traceback.format_exc())

    def judge_china(self, c_text):
        zhPattern = re.compile(u'[\u4e00-\u9fa5]+')
        match = zhPattern.search(u"" + str(c_text))
        if match:
            return True
            # print '有中文：%s' % (match.group(0),)
        else:
            return False

    def send_wait(self):
        """
        发送等待, 控制发往下载中心的速率
        """
        if self.sended_queue.qsize() > 4000:
            time.sleep(0.4)
        elif self.sending_queue.qsize() < 10000:
            time.sleep(0.4)

def Main():
    spider = WxSpider()
    # spider.run(1, 1, 1, 1, 600, 600, 600, 600, True)
    spider.run(30, 40, 50, 30, -1, -1, -1, -1, True)
    # spider.run(2, 4, 5, 1, 600, 600, 600, 600, True)


if __name__ == '__main__':
    Main()
