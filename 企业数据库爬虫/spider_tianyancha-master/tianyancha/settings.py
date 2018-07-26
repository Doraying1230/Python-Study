# -*- coding: utf-8 -*-

# Scrapy settings for tianyancha project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tianyancha'

SPIDER_MODULES = ['tianyancha.spiders']
NEWSPIDER_MODULE = 'tianyancha.spiders'

HTTPERROR_ALLOW_ALL = True
DOWNLOAD_TIMEOUT = 3
DNS_TIMEOUT = 3

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tianyancha.middlewares.TianyanchaSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'tianyancha.downloadmiddleware.anti_ban.AntiBanMiddleware': 543,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'tianyancha.pipelines.TianyanchaPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
LOG_FILE = 'logs/spider.log'
LOG_LEVEL = 'INFO'
#LOG_MAX_SIZE = 10
LOG_BACKUP_COUNT = 10

SPIDER_INFO = {
    'ID': 'TJ_01',
    'SUB_ID': 0,
    'SUB_NUM': 7,
    'TJ_PROXY': False,
    'PUB_PROXY': False,
    'MULTI_IP': {'MONGO': False,
                 'LOCALE_ALL': True,
                 'LOCALE_ONE': False,
                 'NEED_AUTH': False}
}


MONGO_INFO = {
    'host': '192.168.60.65',
    'port': 10010
}


AUTOTHROTTLE_ENABLED = False
EXTENSIONS = {
            'tianyancha.extensions.AutoThrottleWithList.AutoThrottleWithList':300,
            }
# LIMIT_SITES = (
    # {'ID': 'WEB', 'REGEX': r'.*\/page\/creditdetail.htm$', 'DEALY_TIME': 10},
    # {'ID': 'BAIDU_LINK', 'REGEX': r'.*www\.baidu\.com\/link.*', 'DEALY_TIME': 1},
# )
