
# -*- coding: UTF-8 -*-
#  天眼查网站

import re
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import uuid
import random
import conn_mysql

class mainAll(object):

    def __init__(self):
        self.url = 'https://www.tianyancha.com/login'
        self.username = '15160773967'
        self.password = 'yy171827'
        self.word = '淘宝'
        self.driver = self.login()
        self.scrapy(self.driver)
        print("ok,the work is done!")

    def login(self):
        driver = webdriver.Chrome()
        driver.get(self.url)

        # 模拟登陆
        driver.find_element_by_xpath(
            ".//*[@id='web-content']/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/input"). \
            send_keys(self.username)
        driver.find_element_by_xpath(
            ".//*[@id='web-content']/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[3]/input"). \
            send_keys(self.password)
        driver.find_element_by_xpath(
            ".//*[@id='web-content']/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[5]").click()
        time.sleep(1)
        driver.refresh()
       # driver.get('https://www.tianyancha.com/company/28723141')
        #driver.get('https://www.tianyancha.com/company/2355394483')
        driver.get('https://www.tianyancha.com/company/22822')

        # 模拟登陆完成，输入搜索内容
       # driver.find_element_by_xpath(".//*[@id='home-main-search']").send_keys(self.word)  # 输入搜索内容
      #  driver.find_element_by_xpath(".//*[@class='input-group-addon search_button']").click()  # 点击搜索
      #  driver.implicitly_wait(10)

        # 选择相关度最高的搜索结果 第一条搜索框，然后再
        #tag = driver.find_elements_by_xpath("//div[@class='search_right_item']")
        #tag[0].find_element_by_tag_name('a').click()
        driver.implicitly_wait(2)

        # 转化句柄
        now_handle = driver.current_window_handle
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle != now_handle:
                # 输出待选择的窗口句柄

                driver.switch_to.window(handle)
        return driver

    #  获取所有表格和表单
    def scrapy(self, driver):
        tables = driver.find_elements_by_xpath("//div[contains(@id,'_container_')]")

        # 获取每个表格的名字
        c = '_container_'
        name = [0] * (len(tables) - 2)
        # 生成一个独一无二的十六位参数作为公司标记，一个公司对应一个，需要插入多个数据表
        for i in range(0, 10):
            nowTime = time.time()  # 生成当前时间
            t=int(round(nowTime * 1000))
            randomNum = random.randint(1000, 9999)  # 生成的随机整数n，其中0<=n<=100

            uniqueNum =str(t)  + str(randomNum)
        id = uniqueNum

        table_list = [0] * (len(tables) - 2)
        for x in range(0, len(tables) - 2):
            name[x] = tables[x].get_attribute('id')
            name[x] = name[x].replace(c, '')  # 可以用这个名称去匹配数据库
            # 判断是表格还是表单
            num = tables[x].find_elements_by_tag_name('table')

            # 基本信息表table有两个
            if len(num) > 1:
                result = self.baseInfo(id)

                self.inser_sql(name[x], result)

            #  单纯的表格
            elif len(num) == 1:
                table = tables[x].find_element_by_tag_name('tbody')
                if name[x]=='tmInfo':
                    table_list = self.jiexitable1(table, id)
                else:
                    table_list = self.jiexitable(table, id)
                onclickflag = self.tryonclick(tables[x])

                # 判断此表格是否有翻页功能
                if onclickflag == 1:
                    table_list = self.jiexionclick(tables[x], table_list,driver,id)

                print(table_list)
            # 表单样式
            elif len(num) == 0:
                continue
                table_list= table_list + id
            self.inser_sql(name[x], table_list)


        return name

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
            #print(button..get_attribute("onlick"))

            driver.execute_script("arguments[0].click();", button);

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

        data = list(map(tuple, result)) # 将列表变成元组格式才能被插入数据库中
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


    def baseInfo(self,idd):
        base = self.driver.find_element_by_xpath("//div[@class='company_header_width ie9Style position-rel']/div")
        base = self.driver.find_element_by_xpath("//div[@class='company_header_width ie9Style position-rel']/div")
        try:
            base1 = self.driver.find_element_by_id("company_web_top")
        except Exception:
            base1 = ''

        reg_time = self.driver.find_element_by_xpath(
            "//*[@id='_container_baseInfo']/div/div[2]/table/tbody/tr/td[2]/div[2]/div[2]/div/text")
        reg_ziben = self.driver.find_element_by_xpath("//text[@class='tyc-num']")
        reg_status = self.driver.find_element_by_xpath(
            "//*[@id='_container_baseInfo']/div/div[2]/table/tbody/tr/td[2]/div[3]/div[2]/div")

        # base2= self.driver.find_element_by_class_name("company_header_interior new-border pl10 pt10 pb10 position-rel  mt15")
        # base = self.driver.find_element_by_xpath("//div[@class='position-rel']/div")
        # tel = self.driver.find_element_by_xpath("//div[@class='in-block vertical-top overflow-width mr20']/div")
        # base '淘宝（中国）软件有限公司浏览40770\n高新企业\n电话：18768440137邮箱：暂无\n网址：http://www.atpanel.com
        # 地址：杭州市余杭区五常街道荆丰村'

        # print(base2.text)

        name = base.text.split('我要认证')[0]
        try:
            tel = self.driver.find_element_by_xpath(
                "//*[@id='company_web_top']/div[2]/div[2]/div[2]/div[2]/div[1]/span[2]").text.strip(
                "添加");  # base1.text.split('电话：')[1].split("编辑")[0].strip("添加");
        except Exception:
            tel = ''
        try:
            email = self.driver.find_element_by_xpath(
                "//*[@id='company_web_top']/div[2]/div[2]/div[2]/div[2]/div[2]/span[2]").text.strip("添加");
        except Exception:
            email = ''
        try:
            web = self.driver.find_element_by_xpath(
                "//*[@id='company_web_top']/div[2]/div[2]/div[2]/div[3]/div[1]/a").text.strip("添加");
        except Exception:
            web = ''
        try:
            address = self.driver.find_element_by_xpath(
                "//*[@id='company_web_top']/div[2]/div[2]/div[2]/div[3]/div[2]/span[2]").text.strip("添加");
        except Exception:
            address = ''
        reg_time = reg_time.text
        reg_ziben = reg_ziben.text
        reg_status = reg_status.text
        try:
            abstract = self.driver.find_element_by_xpath("//div[@class='sec-c2 over-hide']//script")
            # 获取隐藏内容
            abstract = self.driver.execute_script("return arguments[0].textContent", abstract).strip()
        except Exception:
            abstract = '';

        # abstract=''
        tabs = self.driver.find_elements_by_tag_name('table')
        rows = tabs[1].find_elements_by_tag_name('tr')
        cols = rows[0].find_elements_by_tag_name('td' and 'th')
        # 工商注册号
        reg_code = rows[0].find_elements_by_tag_name('td')[1].text
        # 组织机构代码
        reg_org = rows[0].find_elements_by_tag_name('td')[3].text
        # 统一信用代码
        creditcode = rows[1].find_elements_by_tag_name('td')[1].text
        # 企业类型
        ent_type = rows[1].find_elements_by_tag_name('td')[3].text
        # 纳税人识别号
        tax_code = rows[2].find_elements_by_tag_name('td')[1].text
        # 行业
        hangye = rows[2].find_elements_by_tag_name('td')[3].text
        if hangye:
            self.inser_sql('hangye', hangye)
        # 营业期限
        deadline = rows[3].find_elements_by_tag_name('td')[1].text
        # 核准日期
        hetime = rows[3].find_elements_by_tag_name('td')[3].text
        # 登记机关
        dengji_name = rows[4].find_elements_by_tag_name('td')[1].text
        # 英文名称
        english_name = rows[4].find_elements_by_tag_name('td')[3].text
        # 注册地址
        reg_address = rows[5].find_elements_by_tag_name('td')[1].text
        # 经营范围
        ent_range = rows[6].find_elements_by_tag_name('td')[1].text
        baseInfo = (
        idd, name, tel, email, web, address, reg_time, reg_ziben, reg_status, abstract, reg_code, reg_org, creditcode,
        ent_type, tax_code, hangye, deadline, hetime, dengji_name, english_name, reg_address, ent_range)
        return baseInfo

    def inser_sql(self,title, table):
        print(title)
        if title == 'baseInfo':
            conn_mysql.base(table)
        elif title == 'staff':
            conn_mysql.staff(table)
        elif title == 'holder':
            conn_mysql.holder(table)
        elif title == 'invest':
            conn_mysql.invest(table)
        elif title == 'jingpin':
            conn_mysql.jingpin(table)
        elif title=='hangye':
            conn_mysql.hangye(table)
        elif title=='changeinfo':
            conn_mysql.change(table)
        elif title=='tmInfo':
            conn_mysql.tminfo(table)
if __name__ == '__main__':
    mainAll()