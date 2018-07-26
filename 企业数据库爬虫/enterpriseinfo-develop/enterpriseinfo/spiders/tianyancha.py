# -*- coding: utf-8 -*-
import scrapy
import config
import time
import random
import re
import uuid
import hashlib
import conn_mysql
import json
from bs4 import BeautifulSoup
from enterpriseinfo.items import EnterpriseinfoItem


class TianyanchaSpider(scrapy.Spider):
    """
    爬取天眼查网站的数据，
    首先，需要手动登录获取cookies，
    然后，将cookies放到指定的文件中，
    最后，由脚本读取，进行数据的抓取。
    """
    start_urls = ""
    company_id = ""
    headers = {
        # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
       # "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "zh-CN,zh;q=0.9",
       # "Cache-Control": "max-age=0",
       # "Connection": "keep-alive",
       # "Host": "www.tianyancha.com",
       # "Referer": "https://www.tianyancha.com/",
       # "Cookies":"TYCID=72d5b8c031b911e89c98851d3a1a4b62; undefined=72d5b8c031b911e89c98851d3a1a4b62; ssuid=337554444; aliyungf_tc=AQAAAHu/BhUqfQsAdg11alal1EL5y+8C; csrfToken=MgOZxxauyUNKWi9o0DWMaO-r; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1522153324,1522848176,1523102481; RTYCID=0925b539a4cb4a9fb7639aeff4a5eaa5; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1523109225; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNzY5MjE4NzIzNiIsImlhdCI6MTUyMzEwOTIzNCwiZXhwIjoxNTM4NjYxMjM0fQ.nWMTbyOlsgsMJxExBYkrha5putfxT6BfRloQ781I8eWLawaZhYnJeaI3muimNJ_y2zI5nNMc2_CYIsW49qlHZQ%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252217692187236%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNzY5MjE4NzIzNiIsImlhdCI6MTUyMzEwOTIzNCwiZXhwIjoxNTM4NjYxMjM0fQ.nWMTbyOlsgsMJxExBYkrha5putfxT6BfRloQ781I8eWLawaZhYnJeaI3muimNJ_y2zI5nNMc2_CYIsW49qlHZQ",
       # "Upgrade-Insecure-Requests": "1",
       "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

    cookies = ''
    ent_uid = ''

    name = 'tianyancha'
    allowed_domains = ['www.tianyancha.com']
    # start_urls = ['http://www.tianyancha.com/']
    # start_urls = ['https://www.tianyancha.com/company/3160628762']

    def __init__(self, company_url=None, company_id=None, *args, **kwargs):
        super(TianyanchaSpider, self).__init__(*args, **kwargs)
        self.start_urls = [company_url]
        self.company_id = company_id

    def start_requests(self):
        self.get_tyc_cookies()
        # url = "https://www.tianyancha.com/company/22822"  # 北京百度网讯科技有限公司
        # yield scrapy.Request(url, headers=self.headers, cookies=self.cookies)
        yield scrapy.Request(self.start_urls[0], headers=self.headers, cookies=self.cookies)

    def get_tyc_cookies(self):
        """
        从config目录中的tyc_cookies文件中读取原始的cookies数据，然后，解析成新的格式，并返回
        :return: dict
        """
        f = open("cookies/tyc_cookies", "r")
        readout = f.read()
        f.close()
        # 使用正则表达式对文件进行处理，然后返回字典格式
        dictinfo = json.loads("{"+readout+"}")
        self.cookies = dictinfo

    def get_all_url(self):
        """
        @todo 定时任务
        从数据库中获取所有数据的url，然后再进行遍历获取数据，每天只获取1万条数据。
        :return:
        """
        urls = []
        return urls

    def convert(self, data):
        result = ''
        for s in data:
            if s in config.number_map:
                result += config.number_map[s]
            else:
                result += s
        return result

    def parse(self, response):
        """
        获取所有表格和表单
        :param response:
        :return:
        """
        """
        基于百度获取的所有可能的id值，以此为基础，进行遍历
        _container_baseInfo
        _container_staff
        _container_holder
        _container_invest
        _container_changeinfo
        _container_branch
        _container_rongzi
        _container_teamMember
        _container_firmProduct
        _container_touzi
        _container_jingpin
        _container_lawsuit
        _container_court
        _container_announcementcourt
        _container_punish
        _container_equity
        _container_bid
        _container_recruit
        _container_taxcredit
        _container_check
        _container_product
        _container_certificate
        _container_wechat
        _container_tmInfo
        _container_patent
        _container_copyright
        _container_copyrightWorks
        _container_icp
        _container_pastICCount
        _container_pastInverstCount
        _container_pastHolderCount
        _container_pastZhixing
        _container_pastCourtCount
        _container_pastLawsuitCount
        _container_pastPunishmentIC
        _container_pastAnnouncementCount
        _container_pastEquityCount
        _container_news
        """
        ids = response.xpath("//div[contains(@id,'_container_')]/@id").extract()
        item = EnterpriseinfoItem()
        for id in ids:
            # 遍历ids列表，进行对应的处理
            id_short = id.replace("_container_", "")
            item['op_type'] = id_short

            if id_short == "baseInfo":  # 工商信息
                base_info = self.get_base_info(response)
                item['base_info'] = base_info
                item['qiye_id'] = self.company_id
                yield item
                # pass
            # elif id_short == "staff":  # 主要人员
            #     staff = response.xpath("//div[contains(@id,'_container_staff')]")
            #     staff_info = self.get_staff(staff, self.ent_uid)
            #     item['staff_info'] = staff_info
            #     yield item
            #     # pass
            # elif id_short == "holder":  # 股东信息
            #     holder = response.xpath("//div[contains(@id,'_container_holder')]")
            #     holder_info = self.get_holder(holder, self.ent_uid)
            #     item['holder_info'] = holder_info
            #     yield item
                # pass
            # elif id_short == "invest":  # 对外投资, 后续需要做分页爬取
            #     invest = response.xpath("//div[contains(@id,'_container_invest')]")
            #     invest_info = self.get_invest(invest, self.ent_uid)
            #     item['invest_info'] = invest_info
            #     yield item
            # elif id_short == "changeinfo":  # 变更记录
            #     changeinfo = response.xpath("//div[contains(@id,'_container_changeinfo')]")
            #     changeinfo = self.get_changeinfo(changeinfo, result[0])
            #     item['changeinfo'] = changeinfo
            #     yield item
            # elif id_short == "branch":  # 分支机构
            #     branch = response.xpath("//div[contains(@id,'_container_branch')]")
            #     branch_info = self.get_branch(branch, result[0])
            #     item['branch_info'] = branch_info
            #     yield item
            # elif id_short == "rongzi":  # 融资历史
            #     rongzi = response.xpath("//div[contains(@id,'_container_rongzi')]")
            #     rongzi_info = self.get_rongzi(rongzi, result[0])
            #     item['rongzi_info'] = rongzi_info
            #     yield item
            # elif id_short == "teamMember":  # 核心团队
            #     team_member = response.xpath("//div[contains(@id,'_container_teamMember')]")
            #     team_member_info = self.get_team_member(team_member, result[0])
            #     item['team_member_info'] = team_member_info
            #     yield item
            # elif id_short == "firmProduct":  # 企业业务
            #     firm_product = response.xpath("//div[contains(@id,'_container_firmProduct')]")
            #     firm_product_info = self.get_firm_product(firm_product, result[0])
            #     item['firm_product_info'] = firm_product_info
            #     yield item
            # elif id_short == "touzi":  # 投资事件
            #     touzi = response.xpath("//div[contains(@id,'_container_touzi')]")
            #     touzi_info = self.get_touzi(touzi, result[0])
            #     item['touzi_info'] = touzi_info
            #     yield item
            #     pass
            # elif id_short == "jingpin":  # 竞品信息
            #     jingpin = response.xpath("//div[contains(@id,'_container_jingpin')]")
            #     jingpin_info = self.get_jingpin(jingpin, result[0])
            #     item['jingpin_info'] = jingpin_info
            #     yield item
            #     pass
            # elif id_short == "lawsuit":  # 法律诉讼
            #     lawsuit = response.xpath("//div[contains(@id,'_container_lawsuit')]")
            #     lawsuit_info = self.get_lawsuit(lawsuit, self.ent_uid)
            #     item['lawsuit_info'] = lawsuit_info
            #     yield item
            # elif id_short == "court":  # 法院公告
            #     court = response.xpath("//div[contains(@id,'_container_court')]")
            #     court_info = self.get_court(court, result[0])
            #     item['court_info'] = court_info
            #     yield item
            #     pass
            # elif id_short == "announcementcourt":  # 开庭公告
            #     announcementcourt = response.xpath("//div[contains(@id,'_container_announcementcourt')]")
            #     announcementcourt_info = self.get_announcementcourt(announcementcourt, result[0])
            #     item['announcementcourt_info'] = announcementcourt_info
            #     yield item
            #     pass
            # elif id_short == "punish":  # 行政处罚
            #     punish = response.xpath("//div[contains(@id,'_container_punish')]")
            #     punish_info = self.get_punish(punish, self.ent_uid)
            #     item['punish_info'] = punish_info
            #     yield item
            # elif id_short == "equity":  # 股权出质
            #     equity = response.xpath("//div[contains(@id,'_container_equity')]")
            #     equity_info = self.get_equity(equity, self.ent_uid)
            #     item['equity_info'] = equity_info
            #     yield item
            #     pass
            # elif id_short == "bid":  # 招投标
            #     bid = response.xpath("//div[contains(@id,'_container_bid')]")
            #     bid_info = self.get_bid(bid, result[0])
            #     item['bid_info'] = bid_info
            #     yield item
            #     pass
            # elif id_short == "recruit":  # 招聘
            #     recruit = response.xpath("//div[contains(@id,'_container_recruit')]")
            #     recruit_info = self.get_recruit(recruit, result[0])
            #     item['recruit_info'] = recruit_info
            #     yield item
            #     pass
            # elif id_short == "taxcredit":  # 税务评级
            #     taxcredit = response.xpath("//div[contains(@id,'_container_taxcredit')]")
            #     taxcredit_info = self.get_taxcredit(taxcredit, self.ent_uid)
            #     item['taxcredit_info'] = taxcredit_info
            #     yield item
            # elif id_short == "check":  # 抽查检查
            #     check = response.xpath("//div[contains(@id,'_container_check')]")
            #     check_info = self.get_check(check, result[0])
            #     item['check_info'] = check_info
            #     yield item
            #     pass
            # elif id_short == "product":  # 产品信息
            #     product = response.xpath("//div[contains(@id,'_container_product')]")
            #     product_info = self.get_product(product, result[0])
            #     item['product_info'] = product_info
            #     yield item
            #     pass
            # elif id_short == "certificate":  # 资质证书
            #     certificate = response.xpath("//div[contains(@id,'_container_certificate')]")
            #     certificate_info = self.get_certificate(certificate, result[0])
            #     item['certificate_info'] = certificate_info
            #     yield item
            #     pass
            # elif id_short == "wechat":  # 微信公众号信息
            #     wechat = response.xpath("//div[contains(@id,'_container_wechat')]")
            #     wechat_info = self.get_wechat(wechat, result[0])
            #     item['wechat_info'] = wechat_info
            #     yield item
            #     pass
            # elif id_short == "tmInfo":  # 商标信息
            #     tm_info = response.xpath("//div[contains(@id,'_container_tmInfo')]")
            #     tm_info_tuple = self.get_tm_info(tm_info, result[0])
            #     item['tm_info'] = tm_info_tuple
            #     yield item
            #     pass
            # elif id_short == "patent":  # 专利信息
            #     patent = response.xpath("//div[contains(@id,'_container_patent')]")
            #     patent_info = self.get_patent(patent, result[0])
            #     item['patent_info'] = patent_info
            #     yield item
            #     pass
            # elif id_short == "copyright":  # 软件著作权信息
            #     copyright = response.xpath("//div[contains(@id,'_container_copyright')]")
            #     copyright_info = self.get_copyright(copyright, result[0])
            #     item['copyright_info'] = copyright_info
            #     yield item
            #     pass
            # elif id_short == "copyrightWorks":  # 作品著作权
            #     copyright_works = response.xpath("//div[contains(@id,'_container_copyrightWorks')]")
            #     copyright_works_info = self.get_copyright_works(copyright_works, result[0])
            #     item['copyright_works_info'] = copyright_works_info
            #     yield item
            #     pass
            # elif id_short == "icp":  # 网站备案
            #     icp = response.xpath("//div[contains(@id,'_container_icp')]")
            #     icp_info = self.get_icp(icp, result[0])
            #     item['icp_info'] = icp_info
            #     yield item
            #     pass
            # elif id_short == "pastICCount":  # 历史工商信息
            #     past_ic_count = response.xpath("//div[contains(@id,'_container_pastICCount')]")
            #     past_ic_count_info = self.get_past_ic_count(past_ic_count, result[0])
            #     item['past_ic_count_info'] = past_ic_count_info
            #     yield item
            #     pass
            # elif id_short == "pastInverstCount":  # 历史对外投资
            #     past_inverst_count = response.xpath("//div[contains(@id,'_container_pastInverstCount')]")
            #     past_inverst_count_info = self.get_past_inverst_count(past_inverst_count, result[0])
            #     item['past_inverst_count_info'] = past_inverst_count_info
            #     yield item
            #     pass
            # elif id_short == "pastHolderCount":  # 历史股东
            #     past_holder_count = response.xpath("//div[contains(@id,'_container_pastHolderCount')]")
            #     past_holder_count_info = self.get_past_holder_count(past_holder_count, result[0])
            #     item['past_holder_count_info'] = past_holder_count_info
            #     yield item
            #     pass
            # elif id_short == "pastZhixing":  # 历史被执行人
            #     past_zhixing = response.xpath("//div[contains(@id,'_container_pastZhixing')]")
            #     past_zhixing_info = self.get_past_zhixing(past_zhixing, result[0])
            #     item['past_zhixing_info'] = past_zhixing_info
            #     yield item
            #     pass
            # elif id_short == "pastCourtCount":  # 历史法院公告
            #     past_court_count = response.xpath("//div[contains(@id,'_container_pastCourtCount')]")
            #     past_court_count_info = self.get_past_court_count(past_court_count, result[0])
            #     item['past_court_count_info'] = past_court_count_info
            #     yield item
            #     pass
            # elif id_short == "pastLawsuitCount":  # 历史法律诉讼
            #     past_lawsuit_count = response.xpath("//div[contains(@id,'_container_pastLawsuitCount')]")
            #     past_lawsuit_count_info = self.get_past_lawsuit_count(past_lawsuit_count, result[0])
            #     item['past_lawsuit_count_info'] = past_lawsuit_count_info
            #     yield item
            #     pass
            # elif id_short == "pastPunishmentIC":  # 历史行政处罚
            #     past_punishment_ic = response.xpath("//div[contains(@id,'_container_pastPunishmentIC')]")
            #     past_punishment_ic_info = self.get_past_punishment_ic(past_punishment_ic, result[0])
            #     item['past_punishment_ic_info'] = past_punishment_ic_info
            #     yield item
            #     pass
            # elif id_short == "pastAnnouncementCount":  # 历史开庭公告
            #     past_announcement_count = response.xpath("//div[contains(@id,'_container_pastAnnouncementCount')]")
            #     past_announcement_count_info = self.get_past_announcement_count(past_announcement_count, result[0])
            #     item['past_announcement_count_info'] = past_announcement_count_info
            #     yield item
            #     pass
            # elif id_short == "pastEquityCount":  # 历史股权出质
            #     past_equity_count = response.xpath("//div[contains(@id,'_container_pastEquityCount')]")
            #     past_equity_count_info = self.get_past_equity_count(past_equity_count, result[0])
            #     item['past_equity_count_info'] = past_equity_count_info
            #     yield item
            #     pass
            # elif id_short == "news":  # 新闻动态，在页面右侧，这个可以不爬取
            #     news = response.xpath("//div[contains(@id,'_container_news')]")
            #     news_info = self.get_news(news, result[0])
            #     item['news_info'] = news_info
            #     yield item
            #     pass
            #  单纯的表格
            # elif len(num) == 1:
            #     table = tables[x].find_element_by_tag_name('tbody')
            #     if name[x]=='tmInfo':
            #         table_list = self.jiexitable1(table, id)
            #     else:
            #         table_list = self.jiexitable(table, id)
            #     onclickflag = self.tryonclick(tables[x])
            #
            #     # 判断此表格是否有翻页功能
            #     if onclickflag == 1:
            #         table_list = self.jiexionclick(tables[x], table_list,driver,id)

            # 表单样式
            # elif len(num) == 0:
            #     continue
            #     table_list= table_list + id
            # self.inser_sql(name[x], table_list)

    def get_staff(self, staff, ent_uid):
        """
        获取公司主要人员的信息,包括人员姓名和级别(职务)
        :param staff:
        :return:
        """
        rows = staff.xpath("//div[contains(@class,'clearfix')]//tbody/tr")
        result = [[0 for col in range(4)] for row in range(len(rows))]
        for i in range(len(rows)):
            staff_name = rows[i].xpath(".//a/text()").extract()[0]
            staff_jibie_arr = rows[i].xpath(".//span/text()").extract()
            staff_jibie = "".join(staff_jibie_arr)
            # 计算人员信息的md5值,顺序如下:ent_uid, staff_name, staff_jibie
            staff_str = ent_uid + staff_name + staff_jibie
            # 创建md5对象
            hl = hashlib.md5()
            hl.update(staff_str.encode(encoding='utf-8'))
            staff_md5 = hl.hexdigest()
            result[i][0] = staff_md5
            result[i][1] = ent_uid
            result[i][2] = staff_name
            result[i][3] = staff_jibie

        data = list(map(tuple, result))  # 将列表变成元组格式才能被插入数据库中
        return data

    def get_holder(self, holder, ent_uid):
        """
        获取股东的信息
        :param holder:
        :param ent_uid:
        :return:
        """
        rows = holder.xpath(".//tbody/tr")
        result = [[0 for col in range(5)] for row in range(len(rows))]
        for i in range(len(rows)):
            holder_name = rows[i].xpath("./td/a/text()").extract()[0]  # 股东
            holder_percentage = rows[i].xpath("./td//span/text()").extract()[0]  # 出资比例
            holder_contribution = rows[i].xpath("./td//span/text()").extract()[1]  # 认缴出资
            # 计算股东信息的md5值,顺序如下:ent_uid, holder_name, holder_percentage, holder_contribution
            holder_str = ent_uid + holder_name + holder_percentage + holder_contribution
            # 创建md5对象
            hl = hashlib.md5()
            hl.update(holder_str.encode(encoding='utf-8'))
            staff_md5 = hl.hexdigest()
            result[i][0] = staff_md5
            result[i][1] = ent_uid
            result[i][2] = holder_name
            result[i][3] = holder_percentage
            result[i][4] = holder_contribution

        data = list(map(tuple, result))  # 将列表变成元组格式才能被插入数据库中
        return data

    def get_invest(self, invest, ent_uid):
        """
        获取对外投资的信息
        @todo 需要做分页爬取
        :param invest:
        :param ent_uid:
        :return:
        """
        rows = invest.xpath(".//tbody/tr")
        final_list = []
        result = [[0 for col in range(9)] for row in range(len(rows))]
        for i in range(len(rows)):
            company_name = rows[i].xpath("./td/a/span/text()").extract()[0]  # 被投资公司名称
            legal_person = rows[i].xpath("./td/span/a/text()").extract()[0]  # 被投资法定代表人
            total = rows[i].xpath("./td/span")  # 注册资本
            td_lists = []
            for j, itemss in enumerate(total):
                if j == 0:
                    continue
                td_list = itemss.xpath("./text()").extract()
                if len(td_list) == 0:
                    td_lists.append("")
                else:
                    td_lists.append(td_list[0])
            capital = td_lists[0]  # 注册资本
            invest_sum = td_lists[1]  # 投资数额
            invest_percent = td_lists[2]  # 投资占比
            reg_time = td_lists[3]  # 注册时间
            status = td_lists[4]  # 状态
            # 计算信息的md5值,顺序如下:ent_uid, company_name, legal_person, capital, invest_sum, invest_percent,
            # reg_time, status
            invest_str = ent_uid + company_name + legal_person + capital + invest_sum + invest_percent + reg_time + status
            # 创建md5对象
            hl = hashlib.md5()
            hl.update(invest_str.encode(encoding='utf-8'))
            invest_md5 = hl.hexdigest()
            result[i][0] = invest_md5
            result[i][1] = ent_uid
            result[i][2] = company_name
            result[i][3] = legal_person
            result[i][4] = capital
            result[i][5] = invest_sum
            result[i][6] = invest_percent
            result[i][7] = reg_time
            result[i][8] = status
            final_list.append(tuple(result[i]))

        return final_list

    def get_changeinfo(self, change_info, ent_uid):
        """
        获取变更信息
        @todo 需要做分页爬取
        :param change_info:
        :param ent_uid:
        :return:
        """
        rows = change_info.xpath(".//tbody/tr")
        final_list = []
        result = [[0 for col in range(6)] for row in range(len(rows))]
        for i in range(len(rows)):
            # td_lists = rows[i].xpath("./td/div//text()").extract()
            # td_lists = rows[i].xpath("./td").extract()
            td_lists = rows[i].xpath("./td")
            change_time = td_lists[0].xpath("./div//text()").extract()[0]  # 变更时间
            change_item = td_lists[1].xpath("./div//text()").extract()[0]  # 变更项目
            # before_change = td_lists[2].xpath("./div//text()").extract()  # 变更前
            before_change = td_lists[2].xpath("./div").extract()  # 变更前
            # 判断before_change的长度,如果长度大于等于2,则将列表转换成字符串
            if len(before_change) >= 2:
                before_change_final = '<br>'.join(before_change)
            else:
                before_change_final = before_change[0]
            # after_change = td_lists[3].xpath("./div//text()").extract()  # 变更后
            after_change = td_lists[3].xpath("./div").extract()  # 变更后
            if len(after_change) >= 2:
                after_change_final = '<br>'.join(after_change)
            else:
                after_change_final = after_change[0]
            # # 计算信息的md5值,顺序如下:ent_uid, change_time, change_item, before_change_final, after_change_final
            holder_str = ent_uid + change_time + change_item + before_change_final + after_change_final
            # # 创建md5对象
            hl = hashlib.md5()
            hl.update(holder_str.encode(encoding='utf-8'))
            change_md5 = hl.hexdigest()
            result[i][0] = change_md5
            result[i][1] = ent_uid
            result[i][2] = change_time
            result[i][3] = change_item
            result[i][4] = before_change_final
            result[i][5] = after_change_final
            final_list.append(tuple(result[i]))

        return final_list

    def get_branch(self, branch, ent_uid):
        """
        获取分支机构的信息
        :param branch:
        :param ent_uid:
        :return:
        """
        rows = branch.xpath(".//tbody/tr")
        final_list = []
        result = [[0 for col in range(6)] for row in range(len(rows))]
        for i in range(len(rows)):
            td_lists = rows[i].xpath("./td//span/text()").extract()
            company_name = td_lists[0]  # 公司名称
            legal_person = td_lists[1]  # 法定代表人
            status = td_lists[2]  # 状态
            reg_time = td_lists[3]  # 注册时间
            # 计算信息的md5值,顺序如下:ent_uid, company_name, legal_person, status, reg_time
            holder_str = ent_uid + company_name + legal_person + status + reg_time
            # 创建md5对象
            hl = hashlib.md5()
            hl.update(holder_str.encode(encoding='utf-8'))
            branch_md5 = hl.hexdigest()
            result[i][0] = branch_md5
            result[i][1] = ent_uid
            result[i][2] = company_name
            result[i][3] = legal_person
            result[i][4] = status
            result[i][5] = reg_time
            final_list.append(tuple(result[i]))

        return final_list

    def get_rongzi(self, rongzi, ent_uid):
        rows = rongzi.xpath(".//tbody/tr")
        final_list = []
        result = [[0 for col in range(9)] for row in range(len(rows))]
        for i in range(len(rows)):
            td_lists = rows[i].xpath("./td//span/text()").extract()
            rongzi_time = td_lists[0]  # 融资时间
            rongzi_term = td_lists[1]  # 融资轮次
            valuation = td_lists[2]  # 估值
            total = td_lists[3]  # 金额
            percentage = td_lists[4]  # 比例
            investor = td_lists[5]  # 投资方
            news_source = td_lists[6]  # 新闻来源
            # 计算信息的md5值,顺序如下:ent_uid, rongzi_time, rongzi_term, total, investor
            rongzi_str = ent_uid + rongzi_time + rongzi_term + total + investor
            # 创建md5对象
            hl = hashlib.md5()
            hl.update(rongzi_str.encode(encoding='utf-8'))
            rongzi_md5 = hl.hexdigest()
            result[i][0] = rongzi_md5
            result[i][1] = ent_uid
            result[i][2] = rongzi_time
            result[i][3] = rongzi_term
            result[i][4] = valuation
            result[i][5] = total
            result[i][6] = percentage
            result[i][7] = investor
            result[i][8] = news_source
            final_list.append(tuple(result[i]))

        return final_list
        pass

    def get_team_member(self, team_member, ent_uid):
        """
        核心团队
        :param team_member:
        :param ent_uid:
        :return:
        """
        rows = team_member.xpath(".//div[@class='team-item']")
        final_list = []
        result = [[0 for col in range(5)] for row in range(len(rows))]
        for i in range(len(rows)):
            member_name = rows[i].xpath("./div[@class='team-left']/div[@class='team-name']/text()").extract()[0]
            team_title = rows[i].xpath("./div[@class='team-right']/div[@class='team-title']/text()").extract()[0]
            # 获取ul中的详细描述
            ul_arr = rows[i].xpath("./div[@class='team-right']//ul").extract()
            # 将ul中的数据拼接成字符串
            ul_str = ';'.join(ul_arr)
            # 计算信息的md5值,顺序如下:ent_uid, member_name, team_title, ul_str
            team_str = ent_uid + member_name + team_title + ul_str
            # 创建md5对象
            hl = hashlib.md5()
            hl.update(team_str.encode(encoding='utf-8'))
            team_md5 = hl.hexdigest()
            result[i][0] = team_md5
            result[i][1] = ent_uid
            result[i][2] = member_name
            result[i][3] = team_title
            result[i][4] = ul_str
            final_list.append(tuple(result[i]))

        return final_list

    def get_firm_product(self, firm_product, ent_uid):
        rows = firm_product.xpath(".//div[@class='product-item']")
        final_list = []
        result = [[0 for col in range(3)] for row in range(len(rows))]
        for i in range(len(rows)):
            # 左侧的是个图片
            # product_image = rows[i].xpath("./div[@class='product-left']/").extract()[0]
            # 右侧的详细描述
            right_arr = rows[i].xpath("./div[@class='product-right']//text()").extract()
            # 将ul中的数据拼接成字符串
            right_str = ';'.join(right_arr)
            # 计算信息的md5值,顺序如下:ent_uid, right_str
            team_str = ent_uid + right_str
            # 创建md5对象
            hl = hashlib.md5()
            hl.update(team_str.encode(encoding='utf-8'))
            team_md5 = hl.hexdigest()
            result[i][0] = team_md5
            result[i][1] = ent_uid
            result[i][2] = right_str
            final_list.append(tuple(result[i]))

        return final_list

    def get_touzi(self, touzi, ent_uid):
        rows = touzi.xpath(".//tbody/tr")
        final_list = []
        result = [[0 for col in range(10)] for row in range(len(rows))]
        for i in range(len(rows)):
            td_lists = rows[i].xpath("./td//span/text()").extract()
            touzi_time = td_lists[0]  # 时间
            touzi_term = td_lists[1]  # 轮次
            total = td_lists[2]  # 金额
            investor = td_lists[3]  # 投资方
            product = td_lists[4]  # 产品
            area = td_lists[5]  # 地区
            industry = td_lists[6]  # 行业
            operation = td_lists[7]  # 业务
            # 计算信息的md5值,顺序如下:ent_uid, touzi_time,touzi_term,total,investor,product,area,industry,operation
            team_str = ent_uid + touzi_time + touzi_term + total + investor + product + area + industry + operation
            # 创建md5对象
            hl = hashlib.md5()
            hl.update(team_str.encode(encoding='utf-8'))
            touzi_md5 = hl.hexdigest()
            result[i][0] = touzi_md5
            result[i][1] = ent_uid
            result[i][2] = touzi_time
            result[i][3] = touzi_term
            result[i][4] = total
            result[i][5] = investor
            result[i][6] = product
            result[i][7] = area
            result[i][8] = industry
            result[i][9] = operation
            final_list.append(tuple(result[i]))

        return final_list

    def get_jingpin(self, jingpin, ent_uid):
        rows = jingpin.xpath(".//tbody/tr")
        final_list = []
        result = [[0 for col in range(9)] for row in range(len(rows))]
        for i in range(len(rows)):
            td_lists = rows[i].xpath("./td//span/text()").extract()
            product = td_lists[0]  # 产品
            area = td_lists[1]  # 地区
            current_term = td_lists[2]  # 当前轮次
            industry = td_lists[3]  # 行业
            operation = td_lists[4]  # 业务
            setup_time = td_lists[5]  # 成立时间
            valuation = td_lists[6]  # 估值
            # 计算信息的md5值,顺序如下:ent_uid, product,area,current_term,industry,operation,setup_time,valuation
            jingping_str = ent_uid + product + area + current_term + industry + operation + setup_time + valuation
            # 创建md5对象
            hl = hashlib.md5()
            hl.update(jingping_str.encode(encoding='utf-8'))
            jingping_md5 = hl.hexdigest()
            result[i][0] = jingping_md5
            result[i][1] = ent_uid
            result[i][2] = product
            result[i][3] = area
            result[i][4] = current_term
            result[i][5] = industry
            result[i][6] = operation
            result[i][7] = setup_time
            result[i][8] = valuation
            final_list.append(tuple(result[i]))

        return final_list

    def get_lawsuit(self, law_suit, ent_uid):
        """
        这个对应的是信用信息中的司法信息，在天眼查中，这个是法律诉讼
        @todo 需要做分页爬取
        :param law_suit:
        :param ent_uid:
        :return:
        """
        rows = law_suit.xpath(".//tbody/tr")
        final_list = []
        result = [[0 for col in range(8)] for row in range(len(rows))]
        for i in range(len(rows)):
            # 获取所有的td
            td_lists = rows[i].xpath("./td")

            for j, td_obj in enumerate(td_lists):
                td_text = ''.join(td_obj.xpath(".//text()").extract())
                if j == 0:
                    order_num = td_text  # 序号
                elif j == 1:
                    date = td_text  # 日期
                elif j == 2:
                    judicative_paper = td_text  # 裁判文书
                elif j == 3:
                    case_reason = td_text  # 案由
                elif j == 4:
                    case_status = td_text  # 案件身份
                elif j == 5:
                    case_num = td_text  # 案件号
            # 计算信息的md5值,顺序如下:ent_uid, date, judicative_paper, case_reason, case_status, case_num
            holder_str = ent_uid + date + judicative_paper + case_reason + case_status + case_num
            # 创建md5对象
            hl = hashlib.md5()
            hl.update(holder_str.encode(encoding='utf-8'))
            change_md5 = hl.hexdigest()
            result[i][0] = change_md5
            result[i][1] = ent_uid
            result[i][2] = date
            result[i][3] = judicative_paper
            result[i][4] = case_reason
            result[i][5] = case_status
            result[i][6] = case_num
            result[i][7] = self.company_id
            final_list.append(tuple(result[i]))

        return final_list

    def get_court(self, court, ent_uid):
        pass

    def get_announcementcourt(self, announcementcourt, ent_uid):
        pass

    def get_punish(self, punish, ent_uid):
        """
        这个对应的是信用信息中的行政处罚，在天眼查中，这个是经营风险中的行政处罚
        @todo 需要做分页爬取
        :param punish:
        :param ent_uid:
        :return:
        """
        rows = punish.xpath(".//tbody/tr")
        final_list = []
        result = [[0 for col in range(7)] for row in range(len(rows))]
        for i in range(len(rows)):
            td_lists = rows[i].xpath("./td//text()").extract()

            order_num = td_lists[0]  # 序号
            decision_date = td_lists[1]  # 决定日期
            doc_num = td_lists[2]  # 决定书文号
            doc_type = td_lists[3]  # 类型
            decision_unit = td_lists[4]  # 决定机关
            operation = td_lists[5]  # 操作
            # 计算信息的md5值,顺序如下:ent_uid, decision_date, doc_num, doc_type, decision_unit, operation
            holder_str = ent_uid + decision_date + doc_num + doc_type + decision_unit + operation
            # 创建md5对象
            hl = hashlib.md5()
            hl.update(holder_str.encode(encoding='utf-8'))
            change_md5 = hl.hexdigest()
            result[i][0] = change_md5
            result[i][1] = ent_uid
            result[i][2] = decision_date
            result[i][3] = doc_num
            result[i][4] = doc_type
            result[i][5] = decision_unit
            result[i][6] = self.company_id
            final_list.append(tuple(result[i]))

        return final_list

    def get_equity(self, equity, ent_uid):
        """
        这个对应的是信用信息中的股权质押，在天眼查中，这个是经营风险中的股权出质
        @todo 需要做分页爬取
        :param equity:
        :param ent_uid:
        :return:
        """
        rows = equity.xpath(".//tbody/tr")
        final_list = []
        result = [[0 for col in range(8)] for row in range(len(rows))]
        for i in range(len(rows)):
            td_lists = rows[i].xpath("./td//text()").extract()

            order_num = td_lists[0]  # 序号
            public_date = td_lists[1]  # 公告时间
            reg_num = td_lists[2]  # 登记编号
            pledgor = td_lists[3]  # 出质人
            pledgee = td_lists[4]  # 质权人
            status = td_lists[5]  # 状态
            operation = td_lists[6]  # 操作
            # 计算信息的md5值,顺序如下:ent_uid, public_date, reg_num, pledgor, pledgee, status, operation
            holder_str = ent_uid + public_date + reg_num + pledgor + pledgee + status + operation
            # 创建md5对象
            hl = hashlib.md5()
            hl.update(holder_str.encode(encoding='utf-8'))
            change_md5 = hl.hexdigest()
            result[i][0] = change_md5
            result[i][1] = ent_uid
            result[i][2] = public_date
            result[i][3] = reg_num
            result[i][4] = pledgor
            result[i][5] = pledgee
            result[i][6] = status
            result[i][7] = self.company_id
            final_list.append(tuple(result[i]))

        return final_list

    def get_bid(self, bid, ent_uid):
        pass

    def get_recruit(self, recruit, ent_uid):
        pass

    def get_taxcredit(self, taxcredit, ent_uid):
        """
        这个对应的是信用信息中的税务信息，在天眼查中，这个是税务评级
        @todo 需要做分页爬取
        :param taxcredit:
        :param ent_uid:
        :return:
        """
        rows = taxcredit.xpath(".//tbody/tr")
        final_list = []
        result = [[0 for col in range(8)] for row in range(len(rows))]
        for i in range(len(rows)):
            td_lists = rows[i].xpath("./td//text()").extract()

            order_num = td_lists[0]  # 序号
            year = td_lists[1]  # 年份
            tax_level = td_lists[2]  # 纳税评级
            tax_type = td_lists[3]  # 类型
            recognition_code = td_lists[4]  # 纳税人识别号
            evaluation_unit = td_lists[5]  # 评价单位
            # 计算信息的md5值,顺序如下:ent_uid, year, tax_level, tax_type, recognition_code, evaluation_unit
            holder_str = ent_uid + year + tax_level + tax_type + recognition_code + evaluation_unit
            # 创建md5对象
            hl = hashlib.md5()
            hl.update(holder_str.encode(encoding='utf-8'))
            change_md5 = hl.hexdigest()
            result[i][0] = change_md5
            result[i][1] = ent_uid
            result[i][2] = year
            result[i][3] = tax_level
            result[i][4] = tax_type
            result[i][5] = recognition_code
            result[i][6] = evaluation_unit
            result[i][7] = self.company_id
            final_list.append(tuple(result[i]))

        return final_list

    def get_check(self, check, ent_uid):
        pass

    def get_product(self, product, ent_uid):
        pass

    def get_certificate(self, certificate, ent_uid):
        pass

    def get_wechat(self, wechat, ent_uid):
        pass

    def get_tm_info(self, tm_info, ent_uid):
        pass

    def get_patent(self, patent, ent_uid):
        pass

    def get_copyright(self, copyright, ent_uid):
        pass

    def get_copyright_works(self, copyright_works, ent_uid):
        pass

    def get_icp(self, icp, ent_uid):
        pass

    def get_past_ic_count(self, past_ic_count, ent_uid):
        pass

    def get_past_inverst_count(self, past_inverst_count, ent_uid):
        pass

    def get_past_holder_count(self, past_holder_count, ent_uid):
        pass

    def get_past_zhixing(self, past_zhixing, ent_uid):
        pass

    def get_past_court_count(self, past_court_count, ent_uid):
        pass

    def get_past_lawsuit_count(self, past_lawsuit_count, ent_uid):
        pass

    def get_past_punishment_ic(self, past_punishment_ic, ent_uid):
        pass

    def get_past_announcement_count(self, past_announcement_count, ent_uid):
        pass

    def get_past_equity_count(self, past_equity_count, ent_uid):
        pass

    def get_news(self, news, ent_uid):
        pass




    def trytable(self, x):
        # 是否需要去掉get_attribute ,得到的是table的名字 ,若没得表格到flag则为0
        try:
            x.find_element_by_tag_name('table').get_attribute('class')
            flag = 1
        except Exception:
            flag = 0
            print("这不是表格")
        return flag

    def tryonclick(self, x):
        # 测试是否有翻页
        try:
            # 找到有翻页标记
            x.find_element_by_tag_name('ul')
            print("有翻页")
            onclickflag = 1
            onclickflag = 0
        except Exception:
            print("没有翻页")
            onclickflag = 0
        return onclickflag

    def jiexionclick(self, x, result,driver,id):
        PageCount = x.find_element_by_xpath(r".//div[@class='total']").text
        print(PageCount)
        PageCount = re.sub("\D", "", PageCount)  # 使用正则表达式取字符串中的数字 ；\D表示非数字的意思
        PageCount=int(PageCount)
        print(PageCount)
        for i in range(PageCount - 1):
            button = x.find_element_by_xpath(r".//li[@class='pagination-next  ']/a")
            # print(button..get_attribute("onlick"))

            driver.execute_script("arguments[0].click();", button)

          #  button.click()
            time.sleep(1)
            table = x.find_element_by_tag_name('tbody')
            turnpagetable = self.jiexitable(table,id)
            result.append(turnpagetable)
        return result

    def jiexitable(self, x, id):
        try:
            rows = x.find_elements_by_tag_name('tr')
        # 第二个表格是th 有没有什么方法可以同时查找td或者th！！！！！ and 和 or
            cols = rows[0].find_elements_by_tag_name('td' or 'th')
            result = [[0 for col in range(len(cols)+2)] for row in range(len(rows))]
        except Exception:
            rows=''
            cols=''
            result=''
        # 创建一个二维列表

        for i in range(len(rows)):
            result[i][0] = id
            idd = str(uuid.uuid1())
            idd = idd.replace('-', '')
            result[i][1] = idd
            for j in range(len(cols)):
                try:
                    result[i][j+2] = rows[i].find_elements_by_tag_name('td')[j].text
                except Exception:
                    result[i][j + 2] = ''

        data = list(map(tuple, result))  # 将列表变成元组格式才能被插入数据库中
        return data

    def jiexitable1(self, x, id):
        rows = x.find_elements_by_tag_name('tr')
        # 第二个表格是th 有没有什么方法可以同时查找td或者th！！！！！ and 和 or
        cols = rows[0].find_elements_by_tag_name('td' or 'th')
        result = [[0 for col in range(len(cols)+2)] for row in range(len(rows))]
        # 创建一个二维列表


        for i in range(len(rows)):
            result[i][0] = id
            idd = str(uuid.uuid1())
            idd = idd.replace('-', '')
            result[i][1] = idd
            for j in range(len(cols)):
               # result[i][j+2] = rows[i].find_elements_by_tag_name('td')[j].text
                if j==1:

                    a1=rows[i].find_element_by_class_name('image').get_attribute("src")
                    if a1==0:
                        result[i][j + 2] = rows[i].find_elements_by_tag_name('td')[j].text

                    else:
                        result[i][j + 2] = a1
                else:
                    result[i][j + 2] = rows[i].find_elements_by_tag_name('td')[j].text
        data = list(map(tuple, result)) # 将列表变成元组格式才能被插入数据库中
        return data

    def get_base_info(self, response):
        base = response.xpath("//div[@class='company_header_width ie9Style position-rel']")
        try:
            base1 = response.xpath("//div[@id='company_web_top']")
        except Exception:
            base1 = ''
        # 注册时间，需要转码
        reg_time_raw = response.xpath(
            "//*[@id='_container_baseInfo']/div/div[2]/table/tbody/tr/td[2]/div[2]/div[2]/div/text/text()").extract()[0]
        reg_time = self.convert(reg_time_raw)
        # @todo 注册资本需要转码
        reg_ziben = response.xpath(
            "//*[@id='_container_baseInfo']/div/div[2]/table/tbody/tr/td[2]/div[1]/div[2]/div/text/text()").extract()[0]
        reg_status = response.xpath(
            "//*[@id='_container_baseInfo']/div/div[2]/table/tbody/tr/td[2]/div[3]/div[2]/div/text()").extract()[0]

        name = base.xpath("./div[@class='position-rel']/h1/text()").extract()[0]
        # 用企业名称建立唯一键值，使用的方法为md5
        # 创建md5对象
        hl = hashlib.md5()
        hl.update(name.encode(encoding='utf-8'))
        ent_uid = hl.hexdigest()
        self.ent_uid = ent_uid
        try:
            tel = response.xpath(
                "//*[@id='company_web_top']/div[2]/div[2]/div[2]/div[2]/div[1]/span[2]/text()").extract()[0]
        except Exception:
            tel = ''
        try:
            email = response.xpath(
                "//*[@id='company_web_top']/div[2]/div[2]/div[2]/div[2]/div[2]/span[2]/text()").extract()[0]
        except Exception:
            email = ''
        try:
            web = response.xpath(
                "//*[@id='company_web_top']/div[2]/div[2]/div[2]/div[3]/div[1]/a/text()").extract()[0]
        except Exception:
            web = '暂无信息'
        try:
            address = response.xpath(
                "//*[@id='company_web_top']/div[2]/div[2]/div[2]/div[3]/div[2]/span[2]/text()").extract()[0]
        except Exception:
            address = ''
        try:
            ent_faren = response.xpath("//*[@id='_container_baseInfo']/div/div[2]/table/tbody/tr/td[1]/div/div[1]/div[2]/div/a/text()").extract()[0]
        except Exception:
            ent_faren=""
        try:
            # 获取法人信息的补充信息顶部内容
            ent_faren_supplement_top_arr = response.xpath(
                "//*[@id='_container_baseInfo']/div/div[2]/table/tbody/tr/td[1]/div/div[1]/div[2]/p").extract()
            if len(ent_faren_supplement_top_arr) > 0:
                ent_faren_supplement_top = ent_faren_supplement_top_arr[0]
            else:
                ent_faren_supplement_top = ""
        except Exception:
            ent_faren_supplement_top = ""
        try:
            # 获取法人信息的补充信息底部内容
            ent_faren_supplement_bottom_arr = response.xpath(
                "//*[@id='_container_baseInfo']/div/div[2]/table/tbody/tr/td[1]/div/div[contains(@class,'human-bottom')]").extract()
            if len(ent_faren_supplement_bottom_arr) > 0:
                ent_faren_supplement_bottom = ent_faren_supplement_bottom_arr[0]
            else:
                ent_faren_supplement_bottom = ""
        except Exception:
            ent_faren_supplement_bottom = ""
        try:
            summary = response.xpath("//div[@class='sec-c2 over-hide']//script/text()").extract()[0].strip()
        except Exception:
            summary = ''

        tabs = response.xpath("//*[@id='_container_baseInfo']/div/div[3]/table/tbody")
        rows = tabs.xpath('./tr')
        # 工商注册号
        business_reg_code = rows[0].xpath('./td[2]/text()').extract()[0]
        # 组织机构代码
        org_code = rows[0].xpath('./td[4]/text()').extract()[0]
        # 统一信用代码
        creditcode = rows[1].xpath('./td[2]/text()').extract()[0]
        # 企业类型
        ent_type = rows[1].xpath('./td[4]/text()').extract()[0]
        # 纳税人识别号
        tax_code = rows[2].xpath('./td[2]/text()').extract()[0]
        # 行业
        industry = rows[2].xpath('./td[4]/text()').extract()[0]
        if industry:
            pass
            # self.inser_sql('hangye', industry)
        # 营业期限
        deadline = rows[3].xpath('./td[2]/span/text()').extract()[0]
        # 核准日期，需要转码，调用convert
        hetime_raw = rows[3].xpath('./td[4]/text/text()').extract()[0]
        hetime = self.convert(hetime_raw)
        # 登记机关
        dengji_name = rows[4].xpath('./td[2]/text()').extract()[0]
        # 英文名称
        english_name = rows[4].xpath('./td[4]/text()').extract()[0]
        # 注册地址
        reg_address = rows[5].xpath('./td[2]/text()').extract()[0]
        # 经营范围
        ent_range = rows[6].xpath('./td[2]/span/span/span[1]/text/text()').extract()[0]
        base_info = (
        ent_uid, name, tel, email, web, address, reg_time, reg_ziben, reg_status, summary, business_reg_code, org_code,
        creditcode, ent_type, tax_code, industry, deadline, hetime, dengji_name, english_name, reg_address, ent_range,
        ent_faren, ent_faren_supplement_top, ent_faren_supplement_bottom)
        final_list = []
        final_list.append(tuple(base_info))

        return final_list

    def inser_sql(self, title, table):
        if title == 'baseInfo':
            pass
            # print("baseinfo")
            # print(table[0])
            # conn_mysql.base(table)
        # elif title == 'staff':
        #     conn_mysql.staff(table)
        elif title == 'lawsuit':
            conn_mysql.lawsuit(table)
        elif title == 'announcementcourt':
            conn_mysql.announcementcourt(table)
        elif title == 'bid':
            conn_mysql.bid(table)
        elif title == 'rongzi':
            conn_mysql.rongzi(table)
        elif title == 'certificate':
            conn_mysql.certificate(table)
        elif title == 'copyright':
            conn_mysql.copyright(table)
        elif title == 'rongzi':
            conn_mysql.rongzi(table)
        elif title == 'branch':
            conn_mysql.branch(table)
        elif title == 'touzi':
            conn_mysql.touzi(table)
        # elif title == 'holder':
        #     pass
        #     # conn_mysql.holder(table)
        # elif title == 'invest':
        #     conn_mysql.invest(table)
        elif title == 'jingpin':
            conn_mysql.jingpin(table)
        elif title=='hangye':
            conn_mysql.hangye(table)
        elif title=='changeinfo':
            conn_mysql.change(table)
        elif title=='tmInfo':
            conn_mysql.tminfo(table)
        elif title == 'court':
            conn_mysql.court(table)
        elif title == 'punish':
            conn_mysql.punish(table)
        elif title == 'equity':
            conn_mysql.equity(table)
        elif title == 'firmproduct':
            conn_mysql.firmproduct(table)
        elif title == 'teammember':
            conn_mysql.teammember(table)
        elif title == 'copyrightworks':
            conn_mysql.copyrightworks(table)
        elif title == 'icp':
            conn_mysql.icp(table)
        elif title == 'patent':
            conn_mysql.patent(table)
        elif title == 'tmcount':
            conn_mysql.tmcount(table)
        elif title == 'abnormal':
            conn_mysql.abnormal(table)
        elif title == 'equity':
            conn_mysql.equity(table)
        elif title == 'illegal':
            conn_mysql.illegal(table)
        elif title == 'judicialsale':
            conn_mysql.judicialsale(table)
        elif title == 'mortgage':
            conn_mysql.mortgage(table)
        elif title == 'towntax':
            conn_mysql.towntax(table)
        elif title == 'check':
            conn_mysql.check(table)
        elif title == 'product':
            conn_mysql.product(table)
        elif title == 'taxcredit':
            conn_mysql.taxcredit(table)
        elif title == 'taxcredit':
            conn_mysql.taxcredit(table)
        elif title == 'wechat':
            conn_mysql.wechat(table)
        elif title == 'dishonest':
            conn_mysql.dishonest(table)
        elif title == 'zhixing':
            conn_mysql.zhixing(table)
