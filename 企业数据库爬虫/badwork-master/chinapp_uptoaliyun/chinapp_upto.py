# -*- coding: utf-8 -*-
import MySQLdb
import requests
import time
import Queue
import uuid
import threading
import config

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

    def get_imgs(self,id_num=0):
        sql = 'SELECT id,logo from brand_chinapp WHERE logo is not NULL LIMIT {},100'.format(id_num)
        data = self.db.query(sql)
        if data:
            for row in data:
                if not ('http' in row[1]):
                    logo_id_url = {}
                    _id = int(row[0])
                    logo = row[1]
                    logo_url = 'https://www.chinapp.com/{}'.format(logo)
                    logo_id_url[_id] = logo_url
                    yield logo_id_url
        else:
            time.sleep(60*5)

    def get_image_respone(self, url):
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

    def up_to_server(self, url, respone, filename):
        '''
        将原图下载，并上传到阿里云服务器
        Args:
            url :图片的源地址
            filename:图片文件名
        '''
        # 设置文件目录
        web_folder = "brand/" + filename
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
        img_head = 'http://website201710.oss-cn-shanghai.aliyuncs.com/brand/'
        img_name = '{}.jpg'.format(uuid.uuid1())
        aliyun_url = '{}{}'.format(img_head, img_name)
        return aliyun_url, img_name

    def get_tasks(self):
        id_num = 100
        while 1:
            if self.q.qsize() < 400:
                # id_list = []
                for logo_dict in self.get_imgs(id_num=id_num):
                    self.q.put(logo_dict)
                    # id_list.append(logo_dict.keys()[0])
                # id_num = id_list[-1]
                id_num += 100
            else:
                time.sleep(10)

    def deal_task(self):
        time.sleep(3)
        while 1:
            try:
                logo_dict = self.q.get()
                _id = logo_dict.keys()[0]
                logo_url = logo_dict[_id]
                response = self.get_image_respone(logo_url)
                if response:
                    print('deal_id:',_id)
                    aliyun_url, filename = self.format_img_url()
                    self.up_to_server(logo_url, response, filename)
                    update_sql = "update brand_chinapp set logo='{}' where id = {}".format(
                        MySQLdb.escape_string(str(aliyun_url)), _id)
                    self.db.do(update_sql)
            except:
                print('queue is empty!')
                time.sleep(60 * 5)

    def start(self):
        thread_list = []
        thread_list.append(threading.Thread(target=self.get_tasks))
        for i in range(6):
            t = threading.Thread(target=self.deal_task)
            thread_list.append(t)

        for t in thread_list:
            # t.setDaemon(True)
            t.start()


if __name__ == '__main__':
    aliyun = up2Aliyun()
    aliyun.start()
