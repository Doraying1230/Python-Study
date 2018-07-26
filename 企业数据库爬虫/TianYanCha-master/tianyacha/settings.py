# -*- coding: utf-8 -*-

# Scrapy settings for tianyacha project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tianyacha'

SPIDER_MODULES = ['tianyacha.spiders']
NEWSPIDER_MODULE = 'tianyacha.spiders'

MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_COLLECTION = 'TEL_INFO'
MONGODB_DANAME = 'TIANYANCHA'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tianyacha (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'Cookie': 'TYCID=ee2592804a7c11e8b05097ed267686a9; undefined=ee2592804a7c11e8b05097ed267686a9; ssuid=724550000; RTYCID=6e4fadab9c3244f3b574ee501a104e4b; aliyungf_tc=AQAAAAxynjXvuwgAIrb+ZUroIWIAmstt; csrfToken=NOFu87LTVf1snZNYK-TSS4zA; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; bannerFlag=true; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1528864108,1529026957,1529046116,1529046123; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTEwOTExMzY3NyIsImlhdCI6MTUyOTA0NjYxNiwiZXhwIjoxNTQ0NTk4NjE2fQ.f8r9lhMMD1oQkoUd4JNnAWHj8mulXeOu207cYe63YjGoyp-fo2ZSFnaU7qwnwNomzHfWnAU-UcRozrUoNey6jg%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252215109113677%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNTEwOTExMzY3NyIsImlhdCI6MTUyOTA0NjYxNiwiZXhwIjoxNTQ0NTk4NjE2fQ.f8r9lhMMD1oQkoUd4JNnAWHj8mulXeOu207cYe63YjGoyp-fo2ZSFnaU7qwnwNomzHfWnAU-UcRozrUoNey6jg; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1529046831'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tianyacha.middlewares.TianyachaSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'tianyacha.middlewares.TianyachaDownloaderMiddleware': 543,
    'tianyacha.middlewares.RandomUserAgent':100,
    # 'tianyacha.middlewares.RandomIpProxy':200,
}
USER_AGENT = [
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
]

PROXIES = [
    {'ip_port':'14.118.255.180:6666','user_password':''},
    {'ip_port':'14.118.252.107:6666','user_password':''},
    {'ip_port':'114.232.94.145:18118','user_password':''},
    {'ip_port':'114.228.75.25:6666','user_password':''},
    {'ip_port':'114.228.75.50:6666','user_password':''},
    {'ip_port':'223.145.231.0:6666','user_password':''},
    {'ip_port':'60.166.121.59:8118','user_password':''},
    {'ip_port':'193.165.144.66:80','user_password':''},
    {'ip_port':'39.134.107.159:8080','user_password':''},
    {'ip_port':'60.166.121.59:8118','user_password':''},

]

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'tianyacha.pipelines.TianyachaPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
LOG_FILE = 'tianyanchaSpider.log'
LOG_LEVEL = 'DEBUG'