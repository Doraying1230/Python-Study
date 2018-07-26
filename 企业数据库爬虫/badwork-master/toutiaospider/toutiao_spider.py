# -*- coding: utf8 -*-
import sys
import os
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_PATH)
reload(sys)
sys.setdefaultencoding('utf8')
from download_center.new_spider.spider.basespider import BaseSpider
from download_center.new_spider.downloader.downloader import SpiderRequest
from download_center.store.store_mysql_pool import StoreMysqlPool
from download_center.util.util_log import UtilLogger
from download_center.new_spider.downloader import configs as ststem_config
from download_center.new_spider.util.util_md5 import UtilMD5
from store.toutiao_store import ToutiaoStore
from extractor.toutiao_extractor import ToutiaoExtractor
import configs
import random
import traceback
import time
from threading import Thread
import urllib
import json


class ToutiaoSpider(BaseSpider):
    """
    今日头条搜索
    """

    def __init__(self):
        super(ToutiaoSpider, self).__init__()
        self.log = UtilLogger('ToutiaoSpider',
                              os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log/log_toutiao_spider'))
        self.extractor = ToutiaoExtractor()
        self.store_db = StoreMysqlPool(**configs.CORPUS_DB)

        self.search_url = "http://toutiao.com/search_content/?offset=0&format=json&keyword=%s&autoload=true&count=20&_=%s"

    def get_user_password(self):
        return 'zhangle', 'zlspider'

    def send_wait(self):
        """
        发送等待, 控制发往下载中心的速率
        """
        if self.sended_queue.qsize() > 4000:
            time.sleep(0.1)
        elif self.sending_queue.qsize() < 10000:
            time.sleep(0.1)

    def start_requests(self):
        # 235270990
        start = 236814044
        while True:
            try:
                self.log.info('今日头条抓取程序开始启动...')
                db = StoreMysqlPool(**configs.KEYWORD_DB[ststem_config.ENVIR])
                results = db.query("select id, keyword from keyword_sogou_filter where id < %d "
                                   "order by id desc limit 200" % start)
                self.log.info('start id -- %d' % start)
                if results:
                    config = {'req_type': 1, 'redirect': 1}
                    for row in results:
                        for i in range(1, 2):
                            urls = list()
                            key = row[1]
                            key = urllib.quote(key.strip().encode('utf-8'))

                            t = time.time()
                            url = self.search_url % (key, str(round(t)).replace('.', '000'))
                            urls.append({'url': url, 'type': 1, 'page': i, 'keyword': row[1],
                                         'unique_key': str(self.get_unique_key())})
                            header = {'User-Agent': random.choice(self.pc_user_agents)}
                            request = SpiderRequest(headers=header, config=config, urls=urls)
                            self.sending_queue.put(request)
                        start = row[0]
                time.sleep(60)
            except Exception:
                self.log.error('获取初始请求出错:%s' % traceback.format_exc())

    def deal_request_results(self, request, results):
        if results == 0:
            self.log.error('请求发送失败')
        elif results == -2:
            self.log.error('没有相应地域')
        else:
            self.log.info('请求发送成功')
            self.sended_queue.put(request)

    def get_stores(self):
        stores = list()
        stores.append(ToutiaoStore())
        return stores

    def parse_response_results(self, request, results, queues):
        if results == 0:
            self.log.error('获取结果失败')
        else:
            urls = list()
            parse_result_queue = queues['parse_result_queue']
            sended_queue = queues['sended_queue']
            for u in request.urls:
                unique_key = u['unique_md5']
                if unique_key in results:
                    result = results[unique_key]
                    if str(result['status']) == '2':
                        self.log.info('抓取成功:%s' % u['url'])
                        parse_result_queue.put((request, results, None))
                    elif str(result['status']) == '3':
                        self.log.info('抓取失败:%s' % u['url'])
                        parse_result_queue.put((request, results, None))
                    else:
                        urls.append(u)
                else:
                    self.log.error('发送失败:%s' % u['url'])
                    parse_result_queue.put((request, results, None))
            if len(urls) > 0:
                request.urls = urls
                sended_queue.put(request)

    def deal_response_results(self, request, results, r, stores):
        for u in request.urls:
            url = u['unique_md5']
            if url in results:
                result = results[url]
                if str(result['status']) == '2':
                    req_type = request.config['req_type']
                    start = time.time()
                    if req_type == 1:
                        search_results = json.loads(result['result'])
                        if not search_results.get('data'):
                            continue

                        md5s = list()
                        for item in search_results['data']:
                            if 'article_url' in item.keys():
                                url = item['article_url']
                                if "toutiao.com" not in url:
                                    continue
                                md5 = UtilMD5.md5(url)
                                md5s.append(md5)
                        rows = self.store_db.query("select md5 from unique_key where md5 in ('%s')" % ("','".join(md5s)))
                        self.log.info("query - %d - %s" % (req_type, str(time.time() - start)))
                        start = time.time()

                        rows = [v[0] for v in rows]
                        save_rows = [i for i in md5s if i and i not in rows]
                        if save_rows:
                            sql = "INSERT INTO unique_key (md5) VALUES ('%s')" % "'),('".join(save_rows)
                            self.store_db.do(sql)
                            self.log.info("save - %d - %s" % (req_type, str(time.time() - start)))

                        for item in search_results['data']:
                            if 'article_url' in item.keys():
                                config = {'req_type': 2, 'redirect': 1}
                                url = item['article_url']
                                md5 = UtilMD5.md5(url)
                                if md5 not in save_rows:
                                    continue
                                urls = list()
                                urls.append({'url': url, 'type': 1, 'keyword': u['keyword'],
                                             'unique_key': str(self.get_unique_key())})
                                header = {'User-Agent': random.choice(self.pc_user_agents)}
                                request = SpiderRequest(headers=header, config=config, urls=urls)
                                self.sending_queue.put(request)
                    elif req_type == 2:
                        ext_result = self.extractor.extractor(result['result'])
                        if ext_result:
                            ext_result['url'] = u['url']
                            ext_result['keyword'] = u['keyword']
                            self.store_queue.put(ext_result)
                elif str(result['status']) == '3':
                    pass

    def to_store_results(self, results, stores):
        stores[0].store(results)

    def run(self, send_num=1, get_num=1, parse_num=1, deal_num=1, store_num=1,
            send_idle_time=600, get_idle_time=600, parse_idle_time=600,
            deal_idle_time=600, store_idle_time=600, record_log=False):
        self.validate_user()
        thread_start = Thread(target=self.start_requests)
        thread_start.start()
        threads = list()
        for i in range(0, send_num):
            threads.append(Thread(target=self.send_requests, args=(send_idle_time,)))
        for i in range(0, get_num):
            threads.append(Thread(target=self.get_response, args=(get_idle_time,)))

        queues = {
            'response_queue': self.response_queue,
            'parse_result_queue': self.parse_result_queue,
            'sended_queue': self.sended_queue
        }
        for i in range(0, parse_num):
            threads.append(Thread(target=self.parse_response, args=(parse_idle_time, queues)))
        for i in range(0, deal_num):
            threads.append(Thread(target=self.deal_response, args=(deal_idle_time,)))
        for i in range(0, store_num):
            threads.append(Thread(target=self.store_results, args=(store_idle_time,)))
        if record_log:
            threads.append(Thread(target=self.record_log, args=(send_idle_time,)))
        for thread in threads:
            thread.start()


def main():
    spider = ToutiaoSpider()
    spider.run(send_num=10, get_num=10, parse_num=20, deal_num=80, store_num=20,
               send_idle_time=-1, get_idle_time=-1, parse_idle_time=-1, deal_idle_time=-1, store_idle_time=-1)

if __name__ == '__main__':
    main()
