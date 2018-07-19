#coding:utf-8
import requests
from lxml import etree
from bs4 import BeautifulSoup
# from gongMuFund.items import GongmufundItem
import time
import os
import re
class JiGouBu(object):
    def start_request(self):
        heads ={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Upgrade-Insecure-Requests': '1',
            'Connection': 'keep-alive',
            'Host': 'www.csrc.gov.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'

        }
        main_url = "http://www.csrc.gov.cn/pub/zjhpublic/832/3266/3296/3601/index_7401.htm"
        domain = 'http://www.csrc.gov.cn/pub/zjhpublic/'
        count = 1
        while True:
            res = requests.get(url=main_url, headers=heads)
            result = etree.HTML(res.content.decode('utf-8'))
            detailTitle = result.xpath('//div[@class="row"]/li[@class="mc"]/div/a/text()')
            detailUrl = result.xpath('//div[@class="row"]/li[@class="mc"]/div/a/@href')
            detailUrlList = []
            for perIndex in range(len(detailUrl)):
                perUrl = str(detailUrl[perIndex])
                postfix = perUrl.lstrip('../')
                perDetailUrl = domain+postfix
                detailUrlList.append(perDetailUrl)
            print(detailUrlList)
            needDict = dict(zip(detailUrlList, detailTitle))
            biaoji = self.get_detail(needDict,detailUrlList,heads)
            if biaoji== "stop":
                break
            main_url = "http://www.csrc.gov.cn/pub/zjhpublic/832/3266/3296/3601/index_7401_{}.htm".format(str(count))
            print(main_url)
            count += 1
    def get_detail(self ,needDict,detailUrlList,heads):
        for perDetailIndex in range(len(detailUrlList)):
            DUrl = detailUrlList[perDetailIndex]
            resA = requests.get(url=DUrl, headers=heads)
            strong_text = needDict[DUrl]
            biaojiA = self.get_per_data(resA,strong_text)
            if biaojiA == "stop" :
                return "stop"
    def get_per_data(self,resA,strong_text):
        soup = BeautifulSoup(resA.content.decode('utf-8'), 'lxml')
        souptext = soup.get_text()
        item ={}
        if '的批复' in souptext:
            item["title"] = "";
            item["theme"] = ""
            item["style"] = ""
            item["time"] = ""
            item["touguanren"] = ""
            title_content = soup.find(attrs={"class": re.compile("content")})
            all_context = "";
            if (title_content is not None):
                tt = title_content.children
                for child in tt:
                    try:
                        contenx_text = child.getText()
                        s = '?xml:namespace prefix = o ns = "urn:schemas-microsoft-com:office:office" /';
                        i = 0;
                        if (
                            '?xml:namespace prefix = o ns = "urn:schemas-microsoft-com:office:office" /' in contenx_text):
                            if (contenx_text.find(s) == 0):
                                i = len(s)
                        all_context = all_context + contenx_text;
                        if ("基金管理有限公司：" in contenx_text):
                            item["title"] = contenx_text[i:contenx_text.find("基金管理有限公司：")].strip()
                        elif ("证券有限责任公司：" in contenx_text):
                            item["title"] = contenx_text[i:contenx_text.find("证券有限责任公司：")].strip()
                        elif ("资产管理有限公司：" in contenx_text):
                            item["title"] = contenx_text[i:contenx_text.find("资产管理有限公司：")].strip()
                        elif ("证券资产管理公司：" in contenx_text):
                            item["title"] = contenx_text[i:contenx_text.find("证券资产管理公司：")].strip()
                        elif ("基金管理股份有限公司：" in contenx_text):
                            item["title"] = contenx_text[i:contenx_text.find("基金管理股份有限公司：")].strip()
                        elif ("基金管理有限责任公司：" in contenx_text):
                            item["title"] = contenx_text[i:contenx_text.find("基金管理有限责任公司：")].strip()
                        elif ("证券股份有限公司：" in contenx_text):
                            item["title"] = contenx_text[i:contenx_text.find("证券股份有限公司：")].strip()
                        else:
                            continue
                    except:
                        continue
                if "证券投资" not in strong_text:
                    jijin_id = self.find_last(strong_text, "的批复")
                    if ("基金（LOF）注册" in strong_text):
                        item["theme"] = strong_text[jijin_id - 9:jijin_id]
                    elif ("基金（LOF）变更注册" in strong_text):
                        item["theme"] = strong_text[jijin_id - 11:jijin_id]
                    elif ("基金（QDII）注册" in strong_text):
                        item["theme"] = strong_text[jijin_id - 10:jijin_id]
                    elif ("基金（QDII-LOF）注册" in strong_text):
                        item["theme"] = strong_text[jijin_id - 14:jijin_id]
                    elif ("基金注册" in strong_text):
                        item["theme"] = strong_text[jijin_id - 4:jijin_id]
                    elif ("基金变更注册" in strong_text):
                        item["theme"] = strong_text[jijin_id - 18:jijin_id]
                    else:
                        item["theme"] = "没有解析出数据 "
                else:
                    item["theme"] = strong_text[self.find_last(strong_text, "证券投资") + 4:self.find_last(strong_text, "的批复")]
                item["style"] = strong_text[self.find_last(strong_text, "关于准予") + 4:self.find_last(strong_text, "证券投资基金")]

                startIndex = self.find_last(all_context, "基金管理人")
                if (startIndex == -1):
                    item["touguanren"] = " ";
                else:
                    item["touguanren"] = all_context[startIndex + 6:self.find_last(all_context, "为基金的基金托管人")].strip()

                timeValue = all_context[self.find_last(all_context, "{0}年".format(
                    time.strftime('%Y', time.localtime(time.time())))):self.find_last(all_context, "日") + 1]
                item["time"] = timeValue
                if timeValue:
                    dneyTime = time.strftime('%Y', time.localtime(time.time()))
                    if dneyTime in timeValue:
                        self.make_text(item,strong_text)
                    else:
                        return "stop"
                if not timeValue:
                    self.make_text(item, strong_text)


            return "success"
    def find_last(self,string, str):
        last_position = -1
        while True:
            position = string.find(str, last_position + 1)
            if position == -1:
                return last_position
            last_position = position

    def make_text(self,item,strong_text):
        path ="e:\\htfdss\\fund\\replay\\{0}".format(time.strftime('%Y%m%d',time.localtime(time.time())))
        isExists = os.path.exists(path)
        if (isExists):
            pass;
        else:
            os.makedirs(path);

        file = open(path + '\\{0}.json'.format(time.strftime('%Y%m%d', time.localtime(time.time()))),
                    'a')  # 数据存储到data.json
        line = "{0}|" \
               "{1}|" \
               "{2}|" \
               "{3}|" \
               "{4}".format(item["title"], item["theme"], item["style"], item["time"], item["touguanren"]) + "\n"
        try:
            file.write(line)
        except:
            print('没抓取的页面主题：'+strong_text)

jigou = JiGouBu()
jigou.start_request()