# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import redis
import random
import logging
from fake_useragent import UserAgent
import json
from scrapy.exceptions import IgnoreRequest


class TianyanSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class UserAgentAndProxyMiddleware(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def _get_random_cookies(self):
        r = redis.Redis(host='58.221.49.26',password='123456')
        keys = r.keys('cookies:tianyancha:*')
        return random.choice([json.loads(r.get(key)) for key in keys])  # 字典格式

    def process_request(self, request, spider):
        # 设置UserAgent
        useragent = UserAgent().random
        cookies = self._get_random_cookies()
        # print('*'*100)
        # print(ret)
        request.headers.setdefault('User-Agent', useragent)

        # 设置Cookies
        if cookies:
            print(request.url)
            print('cookies: ', type(cookies),cookies)
            request.cookies = cookies
        else:
            self.logger.debug('No Valid Cookies')

    def process_response(self, request, response, spider):
        print('==90909090=='*100)
        print(response.status)
        if response.status in [300, 301, 302, 303]:
            print('==*=='*100)
            try:
                redirect_url = response.headers['location']
                logging.info('有验证码: 当前被重定向到url为 %s' % redirect_url)
                # 重新返回到request队列,再一次请求
                print('返回请求到请求队列中，进行下一次请求: ', request)
                return request
            except Exception:
                raise IgnoreRequest
        elif response.status in [414, ]:
            return request
        else:
            return response

'''
import requests
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, br',
           'Accept-Language': 'zh-CN,zh;q=0.9',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'Host': 'shenzhen.tianyancha.com',
           'Referer': 'https://shenzhen.tianyancha.com/search/',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
           }

r = redis.Redis(host='58.221.49.26',password='123456')
keys = r.keys('cookies:tianyancha:*')
cookies = [json.loads(r.get(key)) for key in keys]  # 字典格式
print('cookies: \n', cookies)
cookies = random.choice(cookies)
url = 'https://www.tianyancha.com/company/2802426215'
response = requests.get(url=url, cookies=cookies, verify=False)
print(response.status_code)
with open('now1.html','w',encoding='utf-8') as f:
    f.write(response.text)
    
'''

'''
{'ssuid': '4453497264', 'aliyungf_tc': 'AQAAAIPNVmtRpAsAH4cOt/WB8rVjlEbE', 'csrfToken': '-v4pw0pGf8CmKY4EOCpSkQQp', 'TYCID': '394fe2b0e62311e78f50f148dc4c1d62', 'undefined': '394fe2b0e62311e78f50f148dc4c1d62', 'Hm_lvt_e92c8d65d92d534b0fc290df538b4758': '1513842468', 'OA': 'H3m/Z+E11PQ/l1OwyjYIrLLEmfN5iY/45hifg3CNcqI=', 'tyc-user-info': '%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzUzNzIwODE0MiIsImlhdCI6MTUxMzg0MjQ2MSwiZXhwIjoxNTI5Mzk0NDYxfQ.5f2SVlNqsKPb_VgwmXWI6vV3u0khNKAyg45iqV8SHwCEq6g2OW4N7C42cTU8kpFjQfM-VNxvXLhdjY7Xd1rvRw%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252213537208142%2522%257D', 'auth_token': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzUzNzIwODE0MiIsImlhdCI6MTUxMzg0MjQ2MSwiZXhwIjoxNTI5Mzk0NDYxfQ.5f2SVlNqsKPb_VgwmXWI6vV3u0khNKAyg45iqV8SHwCEq6g2OW4N7C42cTU8kpFjQfM-VNxvXLhdjY7Xd1rvRw', '_csrf_bk': '4f34ffd1881711c1b3c3ef5041f38a75', 'Hm_lpvt_e92c8d65d92d534b0fc290df538b4758': '1513842496', '_csrf': 'uR/3eVsf21kU25tHmfo2bQ=='}
Host: www.tianyancha.com
'''