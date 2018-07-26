#coding = utf8
import requests
import json
from lxml import etree
class SpiderAnhui:
    def __init__(self):
        self.temp_url=  "https://www.qichacha.com/g_AH_{}"
        self.headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "max-age=0",
            "cookie": "UM_distinctid=164ab4fe4e91d6-098f2dbf756575-4323461-1fa400-164ab4fe4ea10a; zg_did=%7B%22did%22%3A%20%22164ab4fe53845-0c97075048dd95-4323461-1fa400-164ab4fe539b1%22%7D; _uab_collina=153188249918392111865428; PHPSESSID=h4pm2n7hoh65pae1fp1uu0ntp3; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1531967924,1531981885,1531981979,1532047838; hasShow=1; acw_tc=AQAAAH/c63wTkwUA4gUM0jgfD9NyJ+Vp; CNZZDATA1254842228=1863370741-1531877779-https%253A%252F%252Fwww.baidu.com%252F%7C1532052982; _umdata=2BA477700510A7DF8620B0A5CC1A474244713A29B9DB158519A5A3FA23A2974F2A2BD7FA7511BF0ECD43AD3E795C914C51563DBBE6B2FE663AD30F8BA3A0E3BC; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201532054936148%2C%22updated%22%3A%201532055014326%2C%22info%22%3A%201531882497359%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.qichacha.com%22%2C%22cuid%22%3A%20%221a8f49f168786f6520be249b14b903f4%22%7D; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1532055015",
            "referer": "https://www.qichacha.com/",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
        }
    def get_url_list(self):
        url_list = []
        for i in range(1,501):
            url = self.temp_url.format(i)
            url_list.append(url)
        return url_list
    def parse_url(self,url):
        print("parsing:",url)
        response = requests.get(url,headers = self.headers)
        html = etree.HTML(response.content)
        print(html)
        return html
    def get_content(self,html):
        item_list = []
        company_list = html.xpath("//div[@class='col-md-12']/section")
        print(company_list)
        for company in company_list:
            company_name_1 = company.xpath(".//span[@class='name']/em/text()")
            company_name_2 = company.xpath(".//span[@class='name']/text()")
            company_name = "".join(company_name_1+company_name_2)
            company_master = company.xpath("./a/span[2]/small[1]//i[@class='i i-user3']/following::text()[1]")
            company_master = [i.replace("\t","") for i in company_master]
            company_master = [i.replace(" ", "") for i in company_master]
            company_master = "".join(company_master)
            company_time = company.xpath("./a/span[2]/small[1]//i[@class='i i-user3']/following::text()[2]")
            company_time = [i.replace("\t","")for i in company_time]
            company_time = [i.replace(" ", "") for i in company_time]
            company_time = [i.replace("\n", "") for i in company_time]
            company_time = "".join(company_time)
            company_capital = company.xpath("./a/span[2]/small[1]//i[@class='i i-user3']/following::text()[3]")
            company_capital = [i.replace("\t","")for i in company_capital]
            company_capital = [i.replace("\n", "") for i in company_capital]
            company_capital = [i.replace(" ", "") for i in company_capital]
            company_capital = "".join(company_capital)
            company_catagory = company.xpath("./a/span[2]/small[1]//i[@class='i i-user3']/following::text()[4]")
            company_catagory = [i.replace("\t", "") for i in company_catagory]
            company_catagory = [i.replace("\n", "") for i in company_catagory]
            company_catagory = [i.replace(" ", "") for i in company_catagory]
            company_catagory = "".join(company_catagory)
            company_position = company.xpath("./a/span[2]/small[2]/text()")
            company_position = ("".join(company_position)).replace(" ","")
            item = dict(
                company_name = company_name,
                company_master =company_master,
                company_time =company_time,
                company_capital =company_capital,
                company_catagory =company_catagory,
                company_position =company_position
            )
            print(item)
            item_list.append(item)
        return item_list
    def save_content(self,item_list):
        with open("anhui.txt","a") as f:
            for item in item_list:
                f.write(json.dumps(item,ensure_ascii=False,indent=2))
            print("save sucess")
    def run(self):
        #1.获取URL规律
        url_list= self.get_url_list()
        #2.发送请求，获取响应
        for url in url_list:
            html = self.parse_url(url)
            item_list = self.get_content(html)
            self.save_content(item_list)
        #3.提取内容
        #4.保存内容
if __name__ == '__main__':
    anhui = SpiderAnhui()
    anhui.run()
