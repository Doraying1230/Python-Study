from selenium import webdriver
import time


# 模拟登录，并保存登录成功后的cookie
def get_tyc_cookie():
    url = 'https://www.tianyancha.com/login'

    username = 'XXXXXX'  # 这里需要换成你自己的天眼查账号用户名
    password = 'XXXXXX'  # 这里需要换成你自己的天眼查账号密码

    opt = webdriver.ChromeOptions()
    # 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
    opt.set_headless()
    driver = webdriver.Chrome()
    # driver = webdriver.Chrome(chrome_options=opt)
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