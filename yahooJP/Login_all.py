#coding:utf-8
from selenium import webdriver
import time
import json
import urllib.request as  loadRequest
Chrome_path = 'D:\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe'
try:

    param = {'########@qq.com': '123456'}
    param_a = {'########@qq.com': 'middle_huaxue'}
    for x in param.keys():
        browser = webdriver.PhantomJS(executable_path=Chrome_path)
        browser.get('http://www.cuo88.com/')
        time.sleep(1)
        # browser.save_screenshot('123456.png')
        comment = browser.page_source
        # print(comment)
        browser.find_element_by_id('loginNew').click()
        time.sleep(2)
        browser.find_element_by_id("username").send_keys(x)
        browser.find_element_by_id("password").send_keys(param[x])
        browser.find_element_by_id("vcode").click()
        browser.find_element_by_tag_name("ins").click()
        time.sleep(1)
        browser.save_screenshot('./vcode_img.png')
        vcode = input("请输入验证码：")
        browser.find_element_by_id("vcode").send_keys(vcode)
        browser.find_element_by_id("login_btn").click()
        time.sleep(5)
        now_handle = browser.current_window_handle
        print('数据句柄的值：',now_handle)
        curpage_url = browser.current_url
        print('输出登陆后跳转的url:',curpage_url)
        afterLogin = browser.save_screenshot('./afterLogin.png')
        # a = browser.page_source
        # print(a)
        now_handle = browser.current_window_handle
        # cookie = browser.get_cookies()
        # print('cookies的值',cookie)
        dict_cookies = {}
        for item in browser.get_cookies():
            dict_cookies[item["name"]] =item["value"]
        print('输出的cookie值：',type(dict_cookies),dict_cookies)
        with open('./'+param_a[x]+'_cookie.txt','w') as f:
            f.write(json.dumps(dict_cookies))
        time.sleep(2)


        # cookie = [item["name"] + "=" + item["value"] for item in browser.get_cookies()]
        # print('输出cookie值：',cookie)
        #
        # cookiestr = ';'.join(item for item in cookie)
        # print('输出cookiestr:',cookiestr)

        # print(commentLogin)


except Exception as e:
    print(e)
