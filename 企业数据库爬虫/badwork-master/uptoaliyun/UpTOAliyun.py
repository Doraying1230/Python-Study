# -*- coding: utf-8 -*-
import MySQLdb
import requests
import time
import Queue
import uuid
import threading
import config
from lxml import etree
from lxml.html import fromstring
from download_center.store.store_oss import StoreOSS
from download_center.store.store_mysql import StoreMysql

from download_center.store.store_mysql_pool import StoreMysqlPool
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class up2Aliyun:
    def __init__(self):
        self.db = StoreMysqlPool(**config.CONN_DB)
        self.oss = StoreOSS(**config.EHCO_OSS)
        self.q = Queue.Queue()

    def get_100_imgs(self):
        sql = """SELECT id,thumb,detail from products where id in (select id from(select id from product_extend where STATUS=0 limit 100)tmp)"""
        data = self.db.query(sql)
        if len(data)>1:
            for row in data:
                img_dict = {}
                _id = int(row[0])
                img_url = row[1]
                img_split_urls = set(img_url.split(';'))
                detail = row[2].replace('\\&quot;', '')
                img_urls = self.get_imgs_src_from_detail(detail)
                img_urls.extend(img_split_urls)
                img_urls = list(filter(lambda x: x, img_urls))
                img_dict[_id] = img_urls
                yield img_dict
        else:
            time.sleep(60 * 5)

    @staticmethod
    def get_imgs_src_from_detail(html_str):
        img_urls = list()
        html = fromstring(html_str)
        imgs = html.xpath('.//img')
        if imgs:
            for img in imgs:
                img_src = img.get('src')
                # 去除空的和太短的不是图片链接的
                if img_src:
                    img_urls.append(img_src)
        return img_urls

    def get_image_respone(self, url, data=None):
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
        web_folder = "products/" + filename
        try:
            status = self.oss.put(web_folder, respone).status
            if status != 200:
                print '图片上传失败了'
            else:
                pass
                # print filename, '上传成功'
        except:
            pass
        else:
            # print("deal_response_image", url)
            pass

    def format_img_url(self):
        img_head = 'http://website201710.oss-cn-shanghai.aliyuncs.com/products/'
        img_name = '{}.jpg'.format(uuid.uuid1())
        aliyun_url = '{}{}'.format(img_head, img_name)
        return aliyun_url, img_name

    def get_tasks(self):
        while 1:
            if self.q.qsize() < 400:
                # print('get_1000_imgs')
                id_list = []
                for img_dict in self.get_100_imgs():
                    id_list.append(img_dict.keys()[0])
                    self.q.put(img_dict)
                update_sql = """update product_extend set status=2 where id in {}""".format(tuple(id_list))
                self.db.do(update_sql)
            else:
                time.sleep(10)

    def deal_task(self):
        time.sleep(3)
        while 1:
            # 有可能当前线程判断有数据，但转眼间被别的线程取走了，导致当前线程取不到出错，线程死掉，所以要trycatch
            try:
                # if not self.q.empty():
                img_id_dict = self.q.get()
                _id = img_id_dict.keys()[0]
                img_urls = img_id_dict[_id]
                if img_urls:
                    print('deal_id: ', _id)
                    img_dict = {}
                    for img_url in img_urls:
                        respone = self.get_image_respone(img_url)
                        if respone:
                            aliyun_url, filename = self.format_img_url()
                            # print('aliyun_link: ', aliyun_url)
                            self.up_to_server(respone, filename)
                            img_dict[img_url] = aliyun_url
                    update_sql = """update product_extend set source_thumb="{}" where id = {}""".format(MySQLdb.escape_string(str(img_dict)), _id)
                    self.db.do(update_sql)

            except:
                print('队列已空！稍等...')
                time.sleep(60 * 5)

    def start(self):
        thread_list = []
        thread_list.append(threading.Thread(target=self.get_tasks))
        for i in range(7):
            t = threading.Thread(target=self.deal_task)
            thread_list.append(t)

        for t in thread_list:
            t.start()


if __name__ == '__main__':
    aliyun = up2Aliyun()
    aliyun.start()
