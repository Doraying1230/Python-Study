# coding:utf-8
import requests
import json
import time
import uuid
import threading
import Queue
import MySQLdb
import config
import re
from download_center.store.store_mysql_pool import StoreMysqlPool
from download_center.store.store_oss import StoreOSS
import sys

reload(sys)
sys.setdefaultencoding('utf8')

url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&fp=result&queryWord=招聘&oe=utf-8&word=招聘'


class BaiduImage:
    def __init__(self):
        self.save_db = StoreMysqlPool(**config.EHCO_DB)
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
        web_folder = "bimages/" + filename
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
        img_head = 'http://website201710.oss-cn-shanghai.aliyuncs.com/bimages/'
        img_name = '{}.jpg'.format(uuid.uuid1())
        aliyun_url = '{}{}'.format(img_head, img_name)
        return aliyun_url, img_name

    def get_10_images(self, url):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
            }
            r = requests.get(url, timeout=15, headers=headers)
            content = r.content
            # print(content)
            pattern = re.compile(r'"thumbURL":"(.*?)",')
            all_images = re.findall(pattern, content)
            return all_images[:10]
        except:
            time.sleep(10)


    def get_keywords_from_db(self,id_num):
        sql = """select `keyword` from `spider_keyword` limit {},100""".format(id_num)
        data = self.db.query(sql)
        if len(data)>1:
            for row in data:
                keyword = row[0]
                yield keyword
        else:
            time.sleep(60*5)

    def get_tasks(self):
        id_num = 0
        while 1:
            if self.q.qsize() < 400:
                for keyword in self.get_keywords_from_db(id_num):
                    self.q.put(keyword)
                id_num += 100
                # time.sleep(60 * 60)
            else:
                time.sleep(10)

    def deal_task(self):
        time.sleep(2)
        while 1:
            try:
                keyword = self.q.get()
                if keyword:
                    aliyun_image_urls = []
                    print(keyword)
                    url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&fp=result&queryWord={}&oe=utf-8&word={}'.format(keyword,keyword)
                    image_urls = self.get_10_images(url)
                    if image_urls:
                        for image in image_urls:
                            response = self.get_image_respone(image)
                            if response:
                                aliyun_url,filename = self.format_img_url()
                                self.up_to_server(response,filename)
                                aliyun_image_urls.append(aliyun_url)
                        insert_sql = """insert into `baidu_image` (`keyword`,`urls`) values ('{}','{}')""".format(keyword,MySQLdb.escape_string(str(aliyun_image_urls).replace("'", '"')))
                        self.save_db.do(insert_sql)
                        # print("insert{}".format(keyword))
                    else:
                        print('not deal',keyword)

            except:
                print('queue is empty!')
                time.sleep(60*5)

    def start(self):
        thread_list = []
        thread_list.append(threading.Thread(target=self.get_tasks))
        for i in range(8):
            t = threading.Thread(target=self.deal_task)
            thread_list.append(t)

        for t in thread_list:
            t.start()

if __name__ == '__main__':
    baidu = BaiduImage()
    baidu.start()


