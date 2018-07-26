# coding:utf-8
import pymysql
import threading, queue
import time
import csv
import urllib.parse
from lxml import etree
import subprocess
from bs4 import BeautifulSoup
from RedisQueue import RedisQueue
from datetime import date
import codecs
import multiprocessing


config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'root',
    'charset':'utf8mb4',
    'cursorclass':pymysql.cursors.DictCursor
    }
conn = pymysql.connect(**config)
conn.autocommit(1)
cursor = conn.cursor()
conn.select_db("mail")
# def download_data(url, num_retries=2):
#     # print('download url ',url)
#     print("消费url ", url)
#     out_bytes = subprocess.check_output(['phantomjs', './code.js', str(url,encoding="utf-8")])
#     out_text = out_bytes.decode('utf-8')
#     dom_tree = etree.HTML(out_text)
#     links = dom_tree.xpath('//div[@class="company_info_text"]/span/text()')
#     name = dom_tree.xpath('//div[@class="baseinfo-module-content-value-fr baseinfo-module-content-value"]/a[@class="ng-binding ng-scope"]/text()')
#     print("公司法人是%s" % name)
#     company_name = dom_tree.xpath('//div[@class="company_info_text"]/p/text()')
#     # print(name)
#     # print(len(links))
#     if (len(links) > 0 and len(company_name) > 0):
#         '''
#         print('links[0] 的值是'+links[0])
#         print('links[1] 的值是'+links[1])
#         print('links[2] 的值是'+links[2])
#         print('links[3] 的值是'+links[3])
#         print('links[4] 的值是'+links[4])
#         print('links[9] 的值是'+links[9])
#
#         for i in links:
#            print(i)
#         '''
#         if name is None:
#             name='未公开'
#         print('公司的值是' + company_name[0])
#         # print('公司的url是'+ company_url)
#         print('电话的值是' + links[1])
#         print('邮箱的值是' + links[3])
#         # print('地址的值是' + links[9])
#         filename=str(date.today())+'.csv'
#         print("------------------------------我是分割线---------------------------------")
#         #csv_file = open(filename, 'a', newline='', encoding='GB18030')
#         # try:
#         #     writer = csv.writer(csv_file)
#         #     writer.writerow((company_name[0], name[0], links[1], links[3]))
#         try:
#             print("mysql 执行开始！！！")
#             cursor.execute("insert into  company(company_name,owner,phone,email)  VALUES (%s,%s,%s,%s)", (company_name[0],name[0],links[1],links[3]))
#             conn.commit()
#             print("sql 执行完毕！！！")
#
#
#         except Exception as e:
#             print(e)
#             if num_retries > 0:
#                 print("正在进行数据下载重试操作！！！", num_retries - 1)
#                 download_data(url, num_retries - 1)
#             else:
#                 print("重试失败，把%s 重新放入队列" % url)
#                 url_queue.put(url)
#         # finally:
#         #     cursor.close()
#
#
#     else:
#         if num_retries > 0:
#             print("正在进行数据下载重试操作！！！", num_retries - 1)
#             download_data(url, num_retries - 1)
#
#
# def download_url(company_name, num_retries=2):
#     out_bytes = subprocess.check_output(['phantomjs', './url.js',
#                                          "http://www.tianyancha.com/search?key=" + urllib.parse.quote(
#                                              company_name) + "&checkFrom=searchBox"])
#     out_text = out_bytes.decode('utf-8')
#     html = BeautifulSoup(out_text, "lxml")
#     soup = html.find("a", {"class": {"query_name", "search-new-color"}})
#     try:
#         company_url = soup.attrs['href']
#         url_queue.put(company_url)
#         print("生产url ", company_url)
#     except Exception as e:
#         print(e)
#         if num_retries > 0:
#             print("正在进行url下载重试操作！！！", num_retries - 1)
#             download_url(company_name, num_retries - 1)
#         else:
#             print("重试失败，把%s 重新放入队列" % company_name)
#             name_queue.put(company_name)
#     time.sleep(2)
#
#
# def url_consumer(url_queue):
#     while True:
#         company_url = url_queue.get()
#         download_data(company_url, 5)
#         time.sleep(2)
#     url_queue.task_done()
#
#
# def url_producer(name_queue, url_queue):
#     while True:
#         company_name = name_queue.get()
#         download_url(company_name, 5)


#name_queue = queue.Queue()
# i=0
# name_queue=RedisQueue("name"+str(i+1))
# csv_reader = csv.reader(open('./company.csv', encoding="utf8"))
# for row in csv_reader:
#
#     name_queue.put(row[0])
# url_queue = RedisQueue("url"+str(i+1))
# for n in range(4):
#     producer_thread = threading.Thread(target=url_producer, args=(name_queue, url_queue,))
#     producer_thread.start()
# for n in range(5):
#     consumer_thread = threading.Thread(target=url_consumer, args=(url_queue,))
#     consumer_thread.start()
# #url_queue.join()


def thread_crawl():
    def download_data(url, num_retries=2):
        # print('download url ',url)
        print("消费url ", url)
        out_bytes = subprocess.check_output(['phantomjs', './code.js', str(url, encoding="utf-8")])
        out_text = out_bytes.decode('utf-8')
        dom_tree = etree.HTML(out_text)

        legal_name = dom_tree.xpath(
            '//div[@class="baseinfo-module-content-value-fr baseinfo-module-content-value"]/a[@class="ng-binding ng-scope"]/text()')
        print("公司法人是%s" % legal_name)
        company_name = dom_tree.xpath('//div[@class="company_info_text"]/div[@class="in-block ml10 f18 mb5 ng-binding"]/text()')


        data=dom_tree.xpath('//div[@class="company_info_text"]/span/text()')
        if (len(data) > 0):
            '''
            print('links[0] 的值是'+links[0])
            print('links[1] 的值是'+links[1])
            print('links[2] 的值是'+links[2])
            print('links[3] 的值是'+links[3])
            print('links[4] 的值是'+links[4])
            print('links[9] 的值是'+links[9])

            for i in links:
               print(i)
            '''
            phone=data[1]
            email=data[3]
            if legal_name ==[]:
                legal_name = '未公开'
            print('公司的值是' + company_name[0])
            # print('公司的url是'+ company_url)
            print('电话的值是' + phone)
            print('邮箱的值是' + email)
            # print('地址的值是' + links[9])
            filename = str(date.today()) + '.csv'
            print("------------------------------我是分割线---------------------------------")
            # csv_file = open(filename, 'a', newline='', encoding='GB18030')
            # try:
            #     writer = csv.writer(csv_file)
            #     writer.writerow((company_name[0], name[0], links[1], links[3]))
            try:
                print("mysql 执行开始！！！")
                cursor.execute("insert into  company(company_name,owner,phone,email)  VALUES (%s,%s,%s,%s)",
                               (company_name, legal_name, phone, email))
                conn.commit()
                print("sql 执行完毕！！！")


            except Exception as e:
                print(e)
                if num_retries > 0:
                    print("正在进行数据下载重试操作！！！", num_retries - 1)
                    download_data(url, num_retries - 1)
                else:
                    print("重试失败，把%s 重新放入队列" % url)
                    url_queue.put(url)

                    # finally:
                    #     cursor.close()


        else:
            if num_retries > 0:
                print("正在进行数据下载重试操作！！！", num_retries - 1)
                download_data(url, num_retries - 1)

    def download_url(company_name, num_retries=2):
        out_bytes = subprocess.check_output(['phantomjs', './url.js',
                                             "http://www.tianyancha.com/search?key=" + urllib.parse.quote(
                                                 company_name) + "&checkFrom=searchBox"])
        out_text = out_bytes.decode('utf-8')
        html = BeautifulSoup(out_text, "lxml")
        soup = html.find("a", {"class": {"query_name", "search-new-color"}})
        try:
            company_url = soup.attrs['href']
            url_queue.put(company_url)
            print("生产url ", company_url)
        except Exception as e:
            print(e)
            if num_retries > 0:
                print("正在进行url下载重试操作！！！", num_retries - 1)
                download_url(company_name, num_retries - 1)
            else:
                print("重试失败，把%s 重新放入队列" % company_name)
                name_queue.put(company_name)
        time.sleep(2)

    def url_consumer(url_queue):
        while True:
            company_url = url_queue.get()
            download_data(company_url, 5)
            time.sleep(2)
        url_queue.task_done()

    def url_producer(name_queue, url_queue):
        while True:
            company_name = name_queue.get()
            download_url(company_name, 5)

    threads = []
    print("-------------------------")
    while name_queue.qsize()>0 or url_queue.qsize()>0:
        """
        这儿crawl_queue用上了，就是我们__bool__函数的作用，为真则代表我们MongoDB队列里面还有数据
        threads 或者 crawl_queue为真都代表我们还没下载完成，程序就会继续执行
        """
        for thread in threads:
            if not thread.is_alive():  ##is_alive是判断是否为空,不是空则在队列中删掉
                threads.remove(thread)
        #while len(threads) < 10 or name_queue.qsize()>0 or url_queue.qsize()>0:  ##线程池中的线程少于max_threads 或者 crawl_qeue时
        t1 = threading.Thread(target=url_producer, args=(name_queue, url_queue,))  ##创建线程
        t2=threading.Thread(target=url_consumer,args=(url_queue,))
        threads.append(t1)
        threads.append(t2)
        for t in threads:
            t.setDaemon(True)
            t.start()
        t.join()
        time.sleep(1)
        print("流程执行完毕！！！")




def process_crawl():
    process = []
    num_cpus = multiprocessing.cpu_count()
    print('将会启动进程数为：', num_cpus)
    for i in range(num_cpus):
        p = multiprocessing.Process(target=thread_crawl)  ##创建进程
        p.start()  ##启动进程
        process.append(p)  ##添加进进程队列
    for p in process:
        p.join()  ##等待进程队列里面的进程结束

if __name__ == "__main__":
    i = 0
    name_queue = RedisQueue("name" + str(i + 1))
    # csv_reader = csv.reader(open('./company.csv', encoding="utf8"))
    # for row in csv_reader:
    #      name_queue.put(row[0])
    url_queue = RedisQueue("url" + str(i + 1))

    print("队列已经生成！！！")
    process_crawl()
    print("数据全部抓取完成！！！")