# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.http import Request
from bs4 import BeautifulSoup
# from urllib.parse import urljoin
# from urllib import unquote


class TianyanchaSpiderSpider(scrapy.Spider):
    name = "tianyancha_spider"
    allowed_domains = []
    script = """
            function main(splash)
                splash.images_enabled = false
                splash:go("%s")
                splash:wait(%s)
                return splash:html()
            end
    """
    start_urls = [
        # u'http://www.tianyancha.com/search?key=北京至信普林科技有限公司'

# u'http://www.tianyancha.com/search?key=中国电子北海产业园发展有限公司',
# u'http://www.tianyancha.com/search?key=冠捷显示科技（北海）有限公司',
# u'http://www.tianyancha.com/search?key=广西三诺电子有限公司',
# u'http://www.tianyancha.com/search?key=广西朗科科技投资有限公司',
# u'http://www.tianyancha.com/search?key=广西惠科科技有限公司',
# u'http://www.tianyancha.com/search?key=北海市京凯达智能产业园发展有限公司',
# u'http://www.tianyancha.com/search?key=北海市硕华科技有限公司',
# u'http://www.tianyancha.com/search?key=北海市新拓科技有限公司',
# u'http://www.tianyancha.com/search?key=北海星沅电子科技有限公司',
# u'http://www.tianyancha.com/search?key=北海市润瑞科技有限公司',
# u'http://www.tianyancha.com/search?key=北海市龙浩光电科技有限公司',
# u'http://www.tianyancha.com/search?key=北海市景光电子有限公司',
# u'http://www.tianyancha.com/search?key=北海六禾电子有限公司',
# u'http://www.tianyancha.com/search?key=广西长城计算机有限公司',
# u'http://www.tianyancha.com/search?key=冠德科技（北海）有限公司',
# u'http://www.tianyancha.com/search?key=广西新未来信息产业股份有限公司',
# u'http://www.tianyancha.com/search?key=北海世纪联合创新科技有限公司',
# u'http://www.tianyancha.com/search?key=广西三创科技有限公司',
# u'http://www.tianyancha.com/search?key=北海恒科电子配件有限公司',
# u'http://www.tianyancha.com/search?key=北海迪威电气设备有限公司',
# u'http://www.tianyancha.com/search?key=北海嘉信高科技有限公司',
# u'http://www.tianyancha.com/search?key=北海金海电气设备有限公司',
# u'http://www.tianyancha.com/search?key=北海市蕴芯电子科技有限公司',
# u'http://www.tianyancha.com/search?key=北海德合精密科技有限公司',
# u'http://www.tianyancha.com/search?key=北海国腾智达电子有限公司',
# u'http://www.tianyancha.com/search?key=北海市立新世纪科技有限公司',
# u'http://www.tianyancha.com/search?key=北海迪威电气设备有限公司',
# u'http://www.tianyancha.com/search?key=北海市舜华科技有限公司',
# u'http://www.tianyancha.com/search?key=北海市新北鑫电子科技有限公司',
# u'http://www.tianyancha.com/search?key=北海市北盈数码科技有限公司',
# u'http://www.tianyancha.com/search?key=北海光速网络有限公司',

# u'http://www.tianyancha.com/search?key=广西云鹏时空科技有限责任公司',
# u'http://www.tianyancha.com/search?key=广西北海翔鸿电子科技有限公司',
# u'http://www.tianyancha.com/search?key=北海蓝宏电器有限公司',
# u'http://www.tianyancha.com/search?key=北海市音迪电子科技有限公司',
# u'http://www.tianyancha.com/search?key=北海长城能源科技股份有限公司',
# u'http://www.tianyancha.com/search?key=北海市百创科技有限公司',
# u'http://www.tianyancha.com/search?key=北海市恒忠模具有限公司',
# u'http://www.tianyancha.com/search?key=北海北部湾联讯电子商务有限公司',
# u'http://www.tianyancha.com/search?key=广西禾合和商贸有限公司',
# u'http://www.tianyancha.com/search?key=北海雅斯特电器有限公司',
# u'http://www.tianyancha.com/search?key=北海市深蓝科技发展有限责任公司',
# u'http://www.tianyancha.com/search?key=北海德康电子有限公司',
# u'http://www.tianyancha.com/search?key=广西国奥电梯有限公司',
# u'http://www.tianyancha.com/search?key=北海利高电子有限公司',
# u'http://www.tianyancha.com/search?key=北海四维十方信息技术有限公司',
# u'http://www.tianyancha.com/search?key=北海小丑鱼信息科技有限公司',
# u'http://www.tianyancha.com/search?key=北海时光信息科技有限公司',
# u'http://www.tianyancha.com/search?key=北海振荣信息科技有限公司',
# u'http://www.tianyancha.com/search?key=北海明杰科技有限公司',
# u'http://www.tianyancha.com/search?key=广西天象广告文化传媒有限公司',
# u'http://www.tianyancha.com/search?key=北海市胜安五金机电有限公司',
# u'http://www.tianyancha.com/search?key=广西会圈网络有限公司',
# u'http://www.tianyancha.com/search?key=广西成泰信息科技有限公司',
# u'http://www.tianyancha.com/search?key=广西思达沃特生态农业科技有限公司',
# u'http://www.tianyancha.com/search?key=广西同诚网络科技有限公司',
# u'http://www.tianyancha.com/search?key=广西能工巧匠网络科技有限公司',
# u'http://www.tianyancha.com/search?key=北海蜘蛛网络科技有限公司',
# u'http://www.tianyancha.com/search?key=北海青企电子商务有限公司',
# u'http://www.tianyancha.com/search?key=北海普朗客量子科技有限公司',
# u'http://www.tianyancha.com/search?key=北海市众影科技有限公司',
# u'http://www.tianyancha.com/search?key=广西晞日能源科技有限公司',

u'http://www.tianyancha.com/search?key=北海宝财电子科技开发有限公司',
u'http://www.tianyancha.com/search?key=北海华红信息科技有限公司',
u'http://www.tianyancha.com/search?key=北海佳利科技有限公司',
u'http://www.tianyancha.com/search?key=北海德铭科技有限公司',
u'http://www.tianyancha.com/search?key=北海达智科技有限公司',
u'http://www.tianyancha.com/search?key=北海鸿力科技有限公司',
u'http://www.tianyancha.com/search?key=广西星恒通科技有限公司',
u'http://www.tianyancha.com/search?key=北海中电联合发展有限公司',
u'http://www.tianyancha.com/search?key=北海市钜鸿电子商务有限公司',
u'http://www.tianyancha.com/search?key=广西北海大华元科技有限公司',
u'http://www.tianyancha.com/search?key=北海银鑫电子科技有限公司',
u'http://www.tianyancha.com/search?key=北海远大电子科技有限公司',
u'http://www.tianyancha.com/search?key=北海龙威网络科技有限公司',
u'http://www.tianyancha.com/search?key=广西逢时能源科技股份有限公司',
u'http://www.tianyancha.com/search?key=北海亿思电子科技开发有限责任公司',
u'http://www.tianyancha.com/search?key=鹏思特（北海）实业有限公司',
u'http://www.tianyancha.com/search?key=广西电力工业勘察设计研究院北海分院',
u'http://www.tianyancha.com/search?key=广西桂能工程咨询集团有限公司',
u'http://www.tianyancha.com/search?key=北海富诚电子科技有限公司',
u'http://www.tianyancha.com/search?key=北海市艾迪斯科技发展有限公司',
u'http://www.tianyancha.com/search?key=广西北海中盟科技开发有限责任公司',

# u'http://www.tianyancha.com/search?key=北海恒基伟业科技发展有限公司',
# u'http://www.tianyancha.com/search?key=北海市创联科技有限公司',
# u'http://www.tianyancha.com/search?key=北海华星电子有限公司',
# u'http://www.tianyancha.com/search?key=北海满溢经济咨询有限公司',
# u'http://www.tianyancha.com/search?key=北海博钢电子科技有限公司',
# u'http://www.tianyancha.com/search?key=北海禾博士电子商务有限公司',
# u'http://www.tianyancha.com/search?key=北海巨之投创业投资有限公司',
# u'http://www.tianyancha.com/search?key=北海长云网络科技有限公司',
# u'http://www.tianyancha.com/search?key=北海市日月辉电子有限公司',
# u'http://www.tianyancha.com/search?key=广西龙锦电子科技有限公司',
# u'http://www.tianyancha.com/search?key=北海鑫富诚电子有限公司',
# u'http://www.tianyancha.com/search?key=北海中电兴发科技有限公司',
# u'http://www.tianyancha.com/search?key=北海创新科存储技术有限公司',
# u'http://www.tianyancha.com/search?key=国钰电子（北海）有限公司',
# u'http://www.tianyancha.com/search?key=广西北海中盟中晶光伏科技有限公司',
# u'http://www.tianyancha.com/search?key=北海市合众科技有限公司',
# u'http://www.tianyancha.com/search?key=北海市创景光电科技有限公司',
# u'http://www.tianyancha.com/search?key=广西鑫盾战神安防电子科技有限公司',
# u'http://www.tianyancha.com/search?key=北海思博网络科技有限公司',
# u'http://www.tianyancha.com/search?key=北海纬合电子科技有限公司',
# u'http://www.tianyancha.com/search?key=广西神酷电子科技有限公司',
# u'http://www.tianyancha.com/search?key=广西安源电子科技有限公司',
# u'http://www.tianyancha.com/search?key=广西九鼎通讯科技有限公司',
# u'http://www.tianyancha.com/search?key=北海市禾成电子有限公司',
# u'http://www.tianyancha.com/search?key=北海纬合电子科技有限公司',

    ]

    def start_requests(self):

        for url in self.start_urls:
            print(url)
            yield Request(url,
                        self.parse_next_page,
                        meta={
                        'splash':{
                            'args':{'lua_source': self.script % (url, 5.0)},
                            'endpoint': 'execute'
                            }
                        })

    # def parse_next_page(self, response):
    #     _soup = BeautifulSoup(response.body, 'html.parser')
    #     divs = _soup('div', attrs={'class': 'search_right_item'})
    #     result = {}
    #     for div in divs[:1]:
    #         enterprise = div.a.get_text().strip() or 'unknown'
    #         result['enterpirse'] = enterprise
    #         titles = div('div', attrs={'class': 'title overflow-width'})
    #         text = div.find('text', attrs={'x': '27', 'y': '28'})
    #         result['score'] = text.get_text().strip() if text else '0'
    #         for item in titles:
    #             k_v = item.get_text().split(u'：')
    #             k = k_v[0].strip()
    #             v = k_v[1].strip() if len(k_v)>=2 else 'unknown'
    #             result[k] = v
    #     yield result





    def parse_next_page(self, response):
        _soup = BeautifulSoup(response.body, 'html.parser')
        divs = _soup('div', attrs={'class': 'search_right_item'})
        for div in divs[:1]:
            _score = div.find('text', attrs={'x': '27', 'y': '28'})
            score = _score.get_text().strip() if _score else 'unknown'
            enterprise = div.a.get_text().strip() or 'unknown'
            _location = div.find('i', attrs={'class': 'fa fa-map-marker c9'})
            location = _location.next_element.string.strip() if _location else 'unknown'
            print('location: ', location)
            url = div.a['href'] if div.find('a', attrs={'href': True}) else None
            script = """
                    function main(splash)
                        splash.images_enabled = false
                        splash:go("%s")
                        splash:wait(%s)
                        splash:runjs("$('a.ng-binding').click()")
                        splash:wait(%s)
                        return splash:html()
                    end
            """
            if url:
                print('url: %s' % url)
                yield Request(
                    url,
                    self.parse_page,
                    meta={
                        'splash':{
                            'args': {'lua_source': script % (url, 6.0, 1.0)},
                            'endpoint': 'execute'
                        },
                        'score': score,
                        'enterprise': enterprise,
                        'location': location
                    }
                )

    def parse_page(self, response):
        result = {}
        result['enterpirse'] = response.meta.get('enterprise', 'unknown')
        result['score'] = response.meta.get('score', 'unknown')
        result['location'] = response.meta.get('location', 'unknown')
        result['url'] = response.url
        _soup = BeautifulSoup(response.body, 'html.parser')
        div = _soup.find('div', attrs={'class': 'company_info_text'})
        if div:
            result['enterprise_name'] = div.find('div').get_text().strip() if div.find('div') else 'unknown'
            spans = div('span', attrs={'class': 'contact_way_title'})
            for span in spans:
                key = span.get_text().strip()
                if u'网址' in key:
                    continue
                else:
                    value = span.next_element.next_element.strip()
                result[key.strip()[:-1]] = value.strip()
            a = div.find('a', attrs={'ng-if': 'company.websiteList', 'href': True})
            result[u'网址'] = a.get_text().strip() if a else 'unknown'

        # 企业背景
        div = _soup.find('div', attrs={'class': 'baseInfo_model2017'})
        if div:
            ths = [th.get_text().strip() for th in div.table.thead('td') if th.get_text()]
            tds = [td.get_text().strip() if td.get_text() else 'unknown' for td in div.table.tbody('td')]
            for i, th in enumerate(ths):
                result[th] = tds[i]
        # divs = _soup('div', attrs={'ng-click': 'goToPage(temp)'})
        # for div in divs:
        #     key_value = div.get_text().strip().split()
        #     if len(key_value) >= 2:
        #         result[key_value[0].strip()] = key_value[1].strip()

        # 基本信息
        divs = _soup('div', attrs={'class': 'baseinfo-module-item'})
        for div in divs:
            key = div.find('div', attrs={'class': 'baseinfo-module-content-title'})
            value = div.find('div', attrs={'class': 'baseinfo-module-content-value'})
            result[key.get_text().strip()] = value.get_text().strip().split()[0] if value else 'unknown'
        div = _soup.find('div', attrs={'class': 'company-content'})
        if div:
            table = div.find('table')
            if table:
                tds = table('td', attrs={'class': 'basic-td'})
                for td in tds:
                    key_value = td.get_text().strip().split(u'：') if td else None
                    if key_value:
                        # print(key_value)
                        result[key_value[0].strip()] = ''.join(key_value[1:])
                    else:
                        print('have no key_value')
            else:
                print('have no table')
        else:
            print('have no div row b-c-white company-content')

        # 主要人员
        divs = _soup('div', attrs={'class': 'staffinfo-module-content'})
        name_postion = []
        for div in divs:
            _dict = {}
            key = div.find('div', attrs={'class': 'staffinfo-module-content-title'})
            _dict[u'name'] = key.get_text().strip() if key else 'unknown'
            value = div.find('div', attrs={'class': 'staffinfo-module-content-value'})
            _dict[u'postion'] = value.get_text().strip().split()[0] if value else 'unknown'
            name_postion.append(_dict)
        result['name_postion'] = name_postion
        result['is_down'] = True

        # 对外投资
        div = _soup.find('div', attrs={'class': 'out-investment-container ng-scope'})
        if div:
            table = div.find('table', attrs={'class': 'table companyInfo-table'})
            if table:
                trs = table('tr')
                ths = [th.get_text().strip() for th in trs[0]('th') if th.get_text()]
                investment = []
                for tr in trs[1:]:
                    tds = [td.get_text().strip() if td.get_text() else None for td in tr('td')]
                    investment.append(dict(zip(ths, tds)))
                result['investment'] = investment


        # 融资历史
        div = _soup.find('div', attrs={'ng-if': 'dataItemCount.companyRongzi>0'})
        if div:
            table = div.find('table', attrs={'class': 'table companyInfo-table'})
            if table:
                trs = table('tr')
                ths = [th.get_text().strip() for th in trs[0]('th') if th.get_text()]
                rongzi = []
                for tr in trs[1:]:
                    tds = [td.get_text().strip() if td.get_text() else None for td in tr('td')]
                    rongzi.append(dict(zip(ths, tds)))
                result['rongzi'] = rongzi
            else:
                result['rongzi'] = []
        else:
            result['rongzi'] = []
        yield result


        # for key, value in result.items():
        #     print(key.encode('utf8'))
        #     if isinstance(value, basestring):
        #         print(value.encode('utf8'))
        #     else:
        #         print(value)

