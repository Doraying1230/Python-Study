# -*- coding: utf-8 -*-

# Scrapy settings for proxy_auth project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'proxy_auth'

SPIDER_MODULES = ['proxy_auth.spiders']
NEWSPIDER_MODULE = 'proxy_auth.spiders'

LOG_FILE = 'spider.log'
LOG_LEVEL = 'DEBUG'

CLOSESPIDER_TIMEOUT = 0
CLOSESPIDER_PAGECOUNT = 0
CLOSESPIDER_ITEMCOUNT = 0
CLOSESPIDER_ERRORCOUNT = 0

CONCURRENT_ITEMS = 10

HTTPERROR_ALLOW_ALL = True

COOKIES_ENABLED = True
COOKIES_DEBUG = False

DOWNLOAD_TIMEOUT = 5

DUPEFILTER_CLASS = 'proxy_auth.downloadmiddleware.filter.NoFilter'
DUPEFILTER_DEBUG = True

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'proxy_auth (+http://www.yourdomain.com)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS=10

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY=0
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=16
CONCURRENT_REQUESTS_PER_IP=0

# Disable cookies (enabled by default)
#COOKIES_ENABLED=False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'proxy_auth.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   #'scrapy.contrib.downloadermiddleware.downloadtimeout.DownloadTimeoutMiddleware': None,
   #'proxy_auth.downloadmiddleware.set_ip_useragent.IpAndUserAgentMiddleware': 544,
   'proxy_auth.downloadmiddleware.timer.DownloadTimer': 545,
   'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'proxy_auth.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#AUTOTHROTTLE_ENABLED=True
# The initial download delay
#AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED=True
#HTTPCACHE_EXPIRATION_SECS=0
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'

SPIDER_ID = 0

HTTP_URL = ['http://111.161.24.2:9001', 2]
HTTPS_URL = ['https://www.baidu.com/img/baidu_jgylogo3.gif', 705]

IP_LIST = ('210.82.113.13', '210.82.113.14', '210.82.113.15', '210.82.113.16', '210.82.113.17')

D_STATUS = {'INIT':0, 'AVAIL':1, 'INVAL':2, 'TESTED':3}
D_TYPE = {'TP':0, 'HA':1, 'NA':2}
D_SUPPORT = {'HTTP':0x1, 'HTTPS':0x2, 'SOCKET4':0x4, 'SOCKET5':0x8}

USERAGENT_LIST = (\
    'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 Safari/537.31',\
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17',\
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17',\
    \
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)',\
    'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)',\
    'Mozilla/5.0 (Windows; U; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)',\
    \
    'Mozilla/6.0 (Windows NT 6.2; WOW64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1',\
    'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1',\
    'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:15.0) Gecko/20120910144328 Firefox/15.0.2',\
    \
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',\
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',\
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.13; ) Gecko/20101203',\
    \
    'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',\
    'Opera/9.80 (X11; Linux x86_64; U; fr) Presto/2.9.168 Version/11.50',\
    'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; de) Presto/2.9.168 Version/11.52',\
    \
    'Mozilla/5.0 (Windows; U; Win 9x 4.90; SG; rv:1.9.2.4) Gecko/20101104 Netscape/9.1.0285',\
    'Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.1.7pre) Gecko/20070815 Firefox/2.0.0.6 Navigator/9.0b3',\
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',\
)
