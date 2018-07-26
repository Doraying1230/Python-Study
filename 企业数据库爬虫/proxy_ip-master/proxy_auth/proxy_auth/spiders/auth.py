# -*- coding: utf-8 -*-
import os
import scrapy
import pymongo
from scrapy import log
from pymongo import MongoClient
from proxy_auth.settings import D_STATUS, D_TYPE, D_SUPPORT, HTTP_URL, HTTPS_URL
from time import time


class AuthSpider(scrapy.Spider):
    name = "auth"

    def __init__(self):
        try:
            self.db = MongoClient('192.168.60.64', 10010).proxy
        except Exception, e:
            self.log('connect mongo 192.168.60.64:10010 failed! (%s)' %(str(e)), level=log.CRITICAL)
            raise scrapy.exceptions.CloseSpider('initialization mongo error (%s)' %(str(e)))

    def start_requests(self):
        ## 0. modify status to invalid where err_count >= 3
        self.db.ip_tbl.update_many({'err_count':{'$gte':3}}, {'$set':{'status':D_STATUS['INVAL']}})
        ## 1. delete record from mongo where status is invalid and update_time at the day before
        self.db.ip_tbl.remove({'status':D_STATUS['INVAL'], 'update_time':{'$lt':time()-86400}})
        ## 3. check useful ip
        records = self.db.ip_tbl.find({'status':{'$ne':D_STATUS['INVAL']}}).sort([('update_time', pymongo.ASCENDING)])
        for record in records:
            self.log('create request ip=%s prot=%s status=%d update_time=%f' \
                    %(record['ip'], record['port'], record['status'], record['update_time']), level=log.DEBUG)
            meta = {}
            meta['proxy_ip'] = record['ip']
            meta['proxy_port'] = record['port']
            if record.get('status', D_STATUS['INIT']) == D_STATUS['INIT']:
                meta['proxy'] = 'https://%s:%s' %(record['ip'], record['port'])
                meta['request_type'] = D_SUPPORT['HTTPS']
                yield scrapy.Request(url=HTTPS_URL[0], meta=meta)

            meta['proxy'] = 'http://%s:%s' %(record['ip'], record['port'])
            meta['request_type'] = D_SUPPORT['HTTP']
            yield scrapy.Request(url=HTTP_URL[0], meta=meta)

    def parse(self, response):
        proxy_ip = response.meta['proxy_ip']
        proxy_port = response.meta['proxy_port']
        is_success = False

        record = self.db.ip_tbl.find_one({'ip':proxy_ip, 'port':proxy_port})
        if not record:
            return
        support = record.get('support', 0)
        err_count = record.get('err_count', 0)
        if response.status == 200 and len(response.body) == HTTPS_URL[1]:
            self.db.ip_tbl.find_one_and_update({'ip':proxy_ip, 'port':proxy_port}, 
                {'$set':{'err_count':0, 'status':D_STATUS['AVAIL'], 'update_time':time(), 'support':support or response.meta['request_type']}})
            self.log('[SUCCEED] %f %s' %(response.meta.get('__end_time', time()) - response.meta['__start_time'], response.meta['proxy']))
        elif response.status == 200 and len(response.body) == HTTP_URL[1]:
            self.db.ip_tbl.find_one_and_update({'ip':proxy_ip, 'port':proxy_port},
                {'$set':{'err_count':0, 'status':D_STATUS['AVAIL'], 'update_time':time(),
                    'type':D_TYPE.get(response.body.strip(), 'TP'), 'support':support or response.meta['request_type']}})
            self.log('[SUCCEED] %f %s' %(response.meta.get('__end_time', time()) - response.meta['__start_time'], response.meta['proxy']))
        else:
            self.db.ip_tbl.find_one_and_update({'ip':proxy_ip, 'port':proxy_port}, {'$set':{'status':D_STATUS['TESTED'], 'err_count':err_count+1}})
            self.log('[FAILED] %f %s code=%d errmsg=%s' %(response.meta.get('__end_time', time()) - response.meta['__start_time'], response.meta['proxy'],
                response.status, response.meta.get('errmsg', '')))
        return
