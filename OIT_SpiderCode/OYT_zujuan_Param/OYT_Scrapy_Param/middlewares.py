# # import random
# # import base64
# # from hfdata.spiders.BaseCrawlSpider import BaseCrawlSpider
# # from scrapy.crawler import Crawler
# # from hfdata.settings import PROXY
# import logging
# from fake_useragent import UserAgent
#
#
# class RandomUserAgent(object):
#     # Randomly rotate user agents based on a list of predefined ones
#
#     def __init__(self, crawler):
#         super(RandomUserAgent, self).__init__()
#         fallback = crawler.settings.get('FAKEUSERAGENT_FALLBACK', None)
#         self.ua = UserAgent(fallback=fallback)
#         self.ua_type = crawler.settings.get('RANDOM_UA_TYPE', 'random')
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls(crawler)
#
#     def process_request(self, request, spider):
#         def get_ua():
#             '''Gets random UA based on the type setting (random, firefox…)'''
#             return getattr(self.ua, self.ua_type)
#
#         randomua = get_ua()
#         logging.debug('change user-agent to {}'.format(randomua))
#         request.headers.setdefault('User-Agent', randomua)
#
#
# class ProxyMiddleware(object):
#     def process_request(self, request, spider):
#         #         proxy = BaseCrawlSpider.custom_settings['PROXY']
#         #         proxy = Crawler.settings['PROXY']
#         proxy = spider.settings['PROXY']
#         print(proxy)
#         #         if proxy['user_pass'] is not None:
#         #             request.meta['proxy'] = "http://%s" % proxy['ip_port']
#         #             encoded_user_pass = base64.encodestring(proxy['user_pass'])
#         #             request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
#         #             print ("**************ProxyMiddleware have pass************" + proxy['ip_port'])
#         #         else:
#         print("**************ProxyMiddleware************" + proxy)
#         request.meta['proxy'] = "http://%s" % proxy