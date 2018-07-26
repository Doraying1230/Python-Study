# coding:utf-8
import requests
import time
import uuid
import threading
import Queue
import MySQLdb
import config
import re

from lxml import etree
from lxml.html import fromstring
from download_center.store.store_mysql_pool import StoreMysqlPool
# from StoreMysqlPool import StoreMysqlPool
from download_center.store.store_oss import StoreOSS
import sys
import base64

reload(sys)
sys.setdefaultencoding('utf8')


class BaiduImage:
    def __init__(self):
        self.db = StoreMysqlPool(**config.CONN_DB)
        self.oss = StoreOSS(**config.EHCO_OSS)
        self.q = Queue.Queue()


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
            print '图片下载成功！url: {}'.format(url)
            time.sleep(1)
            return r.content
        except:
            # print '图片下载失败！url: {}'.format(url)
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
        web_folder = "comments/" + filename
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
        img_head = 'http://website201710.oss-cn-shanghai.aliyuncs.com/comments/'
        img_name = '{}.jpg'.format(uuid.uuid1())
        aliyun_url = '{}{}'.format(img_head, img_name)
        return aliyun_url, img_name

    def strip_img(self, html):

        try:
            tree = fromstring(html.decode('utf-8'))
            imgs = tree.xpath('.//img')
            for img in imgs:
                img_src = img.get('src')
                # st = time.time()
                response = self.get_image_respone(img_src)
                # print("get_image_respone end time:{}".format(time.time() - st))
                if response:
                    aliyun_url,filename = self.format_img_url()
                    img.set('src',aliyun_url)
                    self.up_to_server(response, filename)
                else:
                    img.getparent().remove(img)
            content = etree.tostring(tree, encoding='utf-8', method='html').strip()
            return content[5:-6]
        except:
            pass

    def get_all_id_content(self,id_num=0):
        sql = """select id,content from comments limit {},500""".format(id_num)
        data = self.db.query(sql)
        if data:
            for row in data:
                _id = row[0]
                content = row[1]
                yield (_id,content)
        else:
            time.sleep(60*5)

    def get_tasks(self):
        while 1:
            # if self.q.qsize() < 400:
            print("get_tasks")
            for each in self.get_all_id_content():
                self.q.put(each)
            else:
                time.sleep(60*5)

    @staticmethod
    def find_img(s):
        pattern = re.compile(r'src="(.*?)"')
        return re.search(pattern,s)

    def deal_task(self):
        time.sleep(2)
        while 1:
            try:
                id_content = self.q.get()
                _id = id_content[0]
                html = id_content[1]
                if self.find_img(id_content[1]):
                    content = self.strip_img(html)
                    update_sql = """update `comments` set content="{}" where id = {}""".format(MySQLdb.escape_string(base64.b64encode(str(content))), _id)
                    self.db.do(update_sql)
                    print("insert: {}".format(_id))
                else:
                    # i = time.time()
                    update_sql = """update `comments` set content="{}" where id = {}""".format(MySQLdb.escape_string(base64.b64encode(str(html))), _id)
                    self.db.do(update_sql)
                    # print("update_sql:{}".format(time.time() -i))
            except:
                print('queue is empty!')
                time.sleep(60*5)

    def start(self):
        thread_list = []
        thread_list.append(threading.Thread(target=self.get_tasks))
        for i in range(10):
            t = threading.Thread(target=self.deal_task)
            thread_list.append(t)

        for t in thread_list:
            t.start()

if __name__ == '__main__':
    baidu = BaiduImage()
    baidu.start()


