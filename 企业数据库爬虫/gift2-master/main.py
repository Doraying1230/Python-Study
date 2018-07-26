# coding=utf-8
# __author__ = 'franky'
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr
import smtplib
from scrapy import log
from scrapy import signals
from scrapy.crawler import Crawler
from twisted.internet import reactor
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
import pymysql
from scrapy.mail import MailSender
import json, urllib
import requests
from qiushibaike.spiders.qbspider import QbspiderSpider


class JSONObject:
    def __init__(self, d):
        self.__dict__ = d


class manage:
    spiderCounter = 0


    def setupCrawler(self, spiderName):
        crawler = Crawler(get_project_settings())
        crawler.signals.connect(self.spiderClosed, signal=signals.spider_closed)
        # crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
        crawler.configure()

        spider = crawler.spiders.create(spiderName)

        crawler.crawl(spider)
        crawler.start()

    def spiderClosed(self):
        self.spiderCounter -= 1

        if self.spiderCounter == 0:
            reactor.stop()

    def run(self):
        #crawler = CrawlerProcess(get_project_settings())
        settings=get_project_settings();
        settings.set("USER_AGENT",
                     "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36")
        settings.set("ROBOTSTXT_OBEY",False)
        settings.set("DOWNLOAD_DELAY",3)
        DEFAULT_REQUEST_HEADERS = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en',
            'Cookie': '_xsrf=2|1f6b3257|707580dfda4a8a343d52fba9c0a6db27|1481619550; _qqq_uuid_="2|1:0|10:1481619550|10:_qqq_uuid_|56:MDI1Y2Y3NGM3NTQ3YmY5ZjJhMDU5NDkxNTZjYzQ5YzQ1ZGNlMjM2Yw==|404a9e5069cc45ad551978468fee268f9e191fbb7a7bf08fcd8d2691e75c076d"; __cur_art_index=1000; afpCT=1; Hm_lvt_2670efbdd59c7e3ed3749b458cafaa37=1481619551; Hm_lpvt_2670efbdd59c7e3ed3749b458cafaa37=1481698125; _ga=GA1.2.1213135731.1481619552; _gat=1',
            'Host': 'www.qiushibaike.com',
            'If-None-Match': "574d9d2be1412290f59a356e4c34742d43d46240"
        }
        settings.set("DEFAULT_REQUEST_HEADERS",DEFAULT_REQUEST_HEADERS)
        ITEM_PIPELINES = {
            'qiushibaike.pipelines.QiushibaikePipeline': 300,
        }
        settings.set("ITEM_PIPELINES",ITEM_PIPELINES)

        crawler = CrawlerProcess(settings)
        crawler.crawl(QbspiderSpider())
        #crawler.configure()
        # log.start()
        # for spiderName in crawler.spiders.list():
        #     self.spiderCounter += 1
        #     self.setupCrawler(spiderName)

        crawler.start()

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

if __name__ == '__main__':
    handle = manage()
    handle.run()
    config = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'passwd': 'root',
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor
    }
    conn = pymysql.connect(**config)
    conn.autocommit(1)
    cursor = conn.cursor()
    conn.select_db("qiushibaike")


    #天气
    r = requests.get(url='http://wthrcdn.etouch.cn/weather_mini?citykey=101280601')  # 最基本的GET请求
    print(r.status_code)  # 获取返回状态
    print(r.text)
    json_data = json.loads(r.text, object_hook=JSONObject)
    wendu = (json_data.data.wendu)
    ganmao = json_data.data.ganmao
    city = json_data.data.city

    fengxiang = json_data.data.forecast[0].fengxiang
    fengli = json_data.data.forecast[0].fengli
    high = json_data.data.forecast[0].high
    type = json_data.data.forecast[0].type
    low = json_data.data.forecast[0].low
    date = json_data.data.forecast[0].date

    print(city, wendu, ganmao, fengxiang, fengli, high, type, low, date)


    #from_addr = "qibaozhaozhao005@sina.com"
    from_addr="######"
    password = '######'
    #to_addr = '#########'
    #to_addr="######"
    to_addr="451875565@qq.com"
    smtp_server = 'smtp.exmail.qq.com'
    # 邮件内容
    print("邮件内容")
    mail_msg=''
    mail_msg = mail_msg+'''
        <table style="width:100%; font-family:'Microsoft Yahei';">
	<tbody>
		<tr>
			<td>

			<table style="width:100%; max-width:700px; margin:20px auto 0; padding:20px; background:#f6bb43;">
				<tbody>
					<tr style="overflow:hidden;">
						<td><span style="float:left; padding:2px 4px; color:#fff; font-size:18px; border:solid 1px #fff; font-weight:100;">本日天气 </span></td>
					</tr>
					<tr>
					    <tr>
						<td style="font-size:15px;">
							<span>城市：'''+city+'''</span>
						</td>
						</tr>

						<tr>
						<td style="font-size:15px;">
							<span>天气类型：'''+type+'''</span>
						</td>
						</tr>

						<tr>
						<td style="font-size:15px;">
							<span>当前温度：'''+wendu+'''度</span>
						</td>
						</tr>

						<tr>
						<td style="font-size:15px;">
							<span>防感冒指南：'''+ganmao+'''</span>
						</td>
						</tr>

						<tr>
						<td style="font-size:15px;">
							<span>风向：'''+fengxiang+'''</span>
						</td>
						</tr>

						<tr>
						<td style="font-size:15px;">
							<span>风力：'''+fengli+'''</span>
						</td>
						</tr>

						<tr>
						<td style="font-size:15px;">
							<span>最高温：'''+high+'''</span>
						</td>
						</tr>

						<tr>
						<td style="font-size:15px;">
							<span>最低温：'''+low+'''</span>
						</td>
						</tr>

						<tr>
						<td style="font-size:15px;">
							<span>日期：'''+date+'''</span>
						</td>
						</tr>

				</tbody>
			</table>
			<table style="width:100%; max-width:700px; margin:0 auto; padding:20px; background:#fff; border:solid 1px #eee;">
				<tbody>
					<tr style="overflow:hidden;">
						<td><span style="float:left; padding:2px 4px; color:#5e5e5e; font-size:18px; border:solid 1px #5e5e5e; font-weight:100;">开心一下 </span></td>
					</tr>
		    '''

    count = cursor.execute('select * from qiushibaike ORDER BY ulike DESC limit 0,10')
    print(count)
    results = cursor.fetchall()
    mail_msg2=''
    for result in results:
        print(result['content'])
        mail_msg2=mail_msg2+('''<tr>
						<td style="padding:20px 0 10px; font-size:18px; color:#fff; font-weight:700;"><a href="#" style="color:#f6bb43; text-decoration:none;" target="_blank">我是标题</a></td>
					</tr>
					<tr>
					</tr>
					<tr>
						<td><a href="#" target="_blank" style="text-decoration:none;" >'''+result['content']+'''</a></td></tr>"''')


    mail_msg3='''
					<tr>
						<td style="padding:30px; text-align:center;"><a href="#" style="display:inline-block; padding:8px 24px; color:#fff; background:#f6bb43; font-size:16px; border-radius:4px; text-decoration:none;" target="_blank">没有了</a></td>
					</tr>
				</tbody>
			</table>

    '''
    print("mail_msg2的值是",mail_msg2)
    print("邮件对象")
    msg = MIMEMultipart()
    msg['From'] = _format_addr('老学长 <%s>' % from_addr)
    msg['To'] = _format_addr('azhi <%s>' % to_addr)
    msg['Subject'] = Header('每日笑一笑', 'utf-8').encode()
    print(mail_msg+mail_msg2+mail_msg3)
    msg.attach(MIMEText(mail_msg+mail_msg2+mail_msg3, 'html', 'utf-8'))

    #server = smtplib.SMTP(smtp_server, 465)
    server = smtplib.SMTP_SSL("smtp.exmail.qq.com", port=465)
    #server.starttls()
    server.set_debuglevel(1)
    server.login(from_addr, password)
    print("开始向用户%s发送邮件" % to_addr)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    print("邮件发送成功！！！")
    #cursor.execute('truncate table qiushibaike')
    #print("清理完毕！！！")
