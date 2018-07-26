# -*- coding: utf-8 -*-
import os,re,requests, execjs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64)  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    }
    raw_cookies = "UM_distinctid=16248a4955f674-034e8bfe4f13ab-3e3d5f01-15f900-16248a4956042d; zg_did=%7B%22did%22%3A%20%2216248a49590409-033c1e80ddf87d-3e3d5f01-15f900-16248a495927d7%22%7D; _uab_collina=152163718087949934401174; PHPSESSID=u8q0cfvpvhvk2dulgg00pljde5; CNZZDATA1254842228=49471465-1521636737-https%253A%252F%252Fwww.baidu.com%252F%7C1522021411; hasShow=1; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1521851320,1521852458,1521852748,1522026238; acw_tc=AQAAAENx0lxOBAoA8+DVOuqGAntxVXOq; _umdata=0823A424438F76AB31F89788339023ED00002F082E37A40E2024A92F74B673EFBC9E24D9378B8381CD43AD3E795C914C647C9B1566008010E195CF701238492F; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201522026237396%2C%22updated%22%3A%201522026770553%2C%22info%22%3A%201521637168545%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%22bb8de2faa7202286c89f9c3ed7b38e8a%22%7D; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1522026771"
    cookies = {}
    for line in raw_cookies.split(';'):
        key, value = line.split('=', 1)
        cookies[key] = value
    url = "http://www.qichacha.com/"

    r_session = requests.session()

    response = r_session.post(url,headers = headers, cookies=cookies)

    searchkey = "百度"
    myurl = "http://www.qichacha.com/search_riskinfo?key="+searchkey+"&province=JS"
    response = r_session.get(myurl, headers=headers, cookies=cookies)
    soup0 = BeautifulSoup(response.text, "html.parser")
    pagenum = soup0.select('.pagination')[0].select('li')[-2].text
    pagenum = filter(str.isdigit, str(pagenum))

    f = open('E:\\gethtml.txt', 'a')


    for i in range(1, int(pagenum) ):
        url = "http://www.qichacha.com/search_riskinfo?key="+searchkey+"&province=JS"+"&p="+str(i)
        response = r_session.get(url, headers=headers, cookies = cookies)
        soup = BeautifulSoup(response.text, "html.parser")
        for soup_info in soup.select('.m_srchList tbody tr'):
            # print soup_info.find('a').text #获取标题
            for td_info in soup_info.select('td')[:-2]:
                alist = td_info.text.strip().split('\n')
                for a in alist:
                    f.write(a.strip().encode('utf8'))
                    f.write('\n')
                # f.write(td_info.text.strip().encode('utf8'))
                # f.write('\n')

            zzr = soup_info.select('td')[-1].find_all('a')
            for item in zzr:
                a = item.get("onclick")
                b = a.lstrip('wsView("').rstrip("'").rstrip(")").rstrip(ur'"企业搜索-风险列表-查看详情"').rstrip("(").rstrip('");zhugeTrack')
                newurl = 'http://www.qichacha.com/wenshuDetail_'+b+'.html'
                newurl = 'http://www.qichacha.com/wenshuDetail_e9be0c2a79a81039d48116550c5cfbab.html'
                response = r_session.get(newurl, headers=headers, cookies=cookies)
                newsoup = BeautifulSoup(response.text, "html.parser")
                if len(newsoup.select('#wsview'))>0:
                    # a = newsoup.select('#wsview')[0].text.replace('\n','')
                    f.write(newsoup.select('#wsview')[0].text.replace('\n','').encode('utf8'))
                    f.write('\n')
            f.write('===================================================')
            f.write('\n')

    f.close()




