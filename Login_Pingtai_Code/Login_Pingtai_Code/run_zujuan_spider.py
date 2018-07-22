'''
Created on 2017年11月1日

@author: deppon
'''

import scrapy.cmdline

META = {
        "web_site":"https://fly.cainiao.com",
        "login_url":"http://passport.zujuan.com/login",
        "login_post_url":"http://passport.zujuan.com/login?jump_url=http%3A%2F%2Fwww.zujuan.com%2Fucenter",
        "login_sucess_url":"http://www.zujuan.com/ucenter",
        }

def main():
    scrapy.cmdline.execute(argv=['scrapy','runspider',
                                 './spiders/zujuan.py',
                                 '-a','meta='+META.__str__()])

if __name__ == '__main__':
    main()