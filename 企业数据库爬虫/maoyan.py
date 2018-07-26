import requests
import re
import json
from requests.exceptions import RequestException
import time

'''多进程演示，引入进程池,luluxiu'''
from multiprocessing import Pool

'''1'''
def get_one_page(url):
    proxies = {"http": "http://118.193.26.18:8080",
               "https": "118.193.26.18:8080"}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36'}
    try:
        response = requests.get(url,headers=headers,proxies=proxies)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

'''2'''
def parse_one_page(html):
    pattern = re.compile('<dd>.*?>(.*?)</i>.*?title="(.*?)".*?data-src="(.*?)@.*?'
                         'star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?'
                         'fraction">(.*?)</i>.*?</dd>',re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield {'index':item[0],
               'title':item[1],
               'picture':item[2],
               'actor':item[3].strip()[3:],
               'time':item[4].strip('上映时间：'),
               'score':item[5]+item[6]}
'''3'''
def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
        '''把字典转化成字符串,加换行符每行一个
        加ensure_ascii=False和encoding='utf-8，防止写入文件直接转化成unicode，输出中文'''
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()

'''4'''
def main(offset):
    url = 'http://maoyan.com/board/4?offset='+str(offset)
    '''把offset变成一个参数'''
    html = get_one_page(url)
    for item in parse_one_page(html):
        write_to_file(item)
    #print(html)

if __name__ == '__main__':
    for i in range(10):
        main(i*10)
        time.sleep(1)

    '''5,多进程启动函数'''
    # pool = Pool()
    # pool.map(main,[i*10 for i in range(10)])
