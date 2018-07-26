print("hello world!")
import requests
from lxml import etree
loginUrl = "https://www.qixin.com/api/user/login"
# 启信宝登录接口
homePage = "https://www.qixin.com"
# 启信宝首页
headers = {"Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Content-Length": "66",
    "Content-Type": "application/json;charset=utf-8",
    "Host": "www.qixin.com",
    "Referer": "https://www.qixin.com/auth/login?return_url=%2Fnew-vip",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0",
    "X-Requested-With": "XMLHttpRequest",
    "dc49417fe4f34f86b0fe": "44282ce68be84e73f8eb4d2a4d4b32c02e8e84970160b2d6829c6b8a5380483e50ec708bc38040dd715d283dfac3123cf422ecff2fe4977c8624e457c5046959"
    }
# 请求头（伪装成浏览器）
parameter = {"acc": "13688888888", "pass": "000000", "captcha": {"isTrusted": True}}
# 请求体
session = requests.Session()
# 保持会话
response_1 = session.post(loginUrl, headers=headers, json=parameter, timeout=5)
# 登录
print(response_1.status_code)
# 打印响应码
response_2 = session.get(homePage).content
# 打开启信宝首页
page_2 = etree.HTML(response_2)
link = page_2.xpath("//html/body/div[1]/div[4]/div/div[2]/div/div[1]/div[1]/a//@href")
companyUrl = homePage+link[0]
# 获取第一家公司的URL
response_3 = session.get(companyUrl).content
# 打开第一家公司
page_3 = etree.HTML(response_3)
companyName = page_3.xpath("//html/body/div[6]/div/div[2]/div/div/h4//text()")
# 获取公司名称
code_1 = page_3.xpath("//*[@id='icinfo']/table/tbody/tr[1]/td[2]//text()")
# 获取统一社会信用代码
code_2 = page_3.xpath("//*[@id='icinfo']/table/tbody/tr[2]/td[2]//text()")
# 获取注册号
print(companyName[0]+"\n"+code_1[0]+"\n"+code_2[0])
