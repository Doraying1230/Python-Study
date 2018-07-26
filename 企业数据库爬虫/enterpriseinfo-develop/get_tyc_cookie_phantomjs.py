from selenium import webdriver
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# 模拟登录，并保存登录成功后的cookie
def get_tyc_cookie():
    url = 'https://www.tianyancha.com/login'

    username = 'XXXXXX'  # 这里需要换成你自己的天眼查账户用户名
    password = 'XXXXXX'  # 这里需要换成你自己的天眼查账户密码

    # opt = webdriver.ChromeOptions()
    # # 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
    # opt.set_headless()
    # driver = webdriver.Chrome()
    params = DesiredCapabilities.PHANTOMJS  # 这本身是一个dict格式类属性
    params['phantomjs.page.settings.userAgent'] = ("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36"
                                                   " (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
    # windows系统的路径
    # driver = webdriver.PhantomJS(executable_path="D:\phantomjs.exe", desired_capabilities=params)
    # Linux系统的路径
    driver = webdriver.PhantomJS(executable_path="/home/phantomjs", desired_capabilities=params)
    driver.get(url)

    # 模拟登陆
    driver.find_element_by_xpath(
        ".//*[@id='web-content']/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/input"). \
        send_keys(username)
    driver.find_element_by_xpath(
        ".//*[@id='web-content']/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[3]/input"). \
        send_keys(password)
    driver.find_element_by_xpath(
        ".//*[@id='web-content']/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[5]").click()
    time.sleep(1)
    driver.refresh()
    # get the session cookie
    cookie = ['"'+item["name"] + '":"' + item["value"]+'"' for item in driver.get_cookies()]
    # print cookie

    cookiestr = ','.join(item for item in cookie)
    # 保存到文件中
    file = open('enterpriseinfo/cookies/tyc_cookies', 'w')
    file.write(cookiestr)
    file.close()
    print(cookiestr)


if __name__ == "__main__":
    get_tyc_cookie()