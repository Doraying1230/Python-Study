'''
Created on 2017年10月27日

@author: deppon
'''
from scrapy.spiders import CrawlSpider
import scrapy
from scrapy.http import Request,FormRequest

class ZuJuanSpider(CrawlSpider):
    name = "ZuJuanSpider"
    
    account = '13653978879'
    pwd = '123456'

    headers  = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
        'Host':'passport.zujuan.com',
        'Origin':'http://passport.zujuan.com',
        'X - Requested - With': 'XMLHttpRequest',
        'Connection': 'keep - alive'


    }
    def __init__(self, *a, **kw):
        super(ZuJuanSpider, self).__init__(*a, **kw)
        self.meta = eval(kw['meta'])
        
    def start_requests(self):       
        """第一次请求一下登录页面，设置开启cookie使其得到cookie，设置回调函数"""
        return [Request(url=self.meta['login_url'],meta={'cookiejar':1},callback=self.parse,headers=self.headers)]

    def parse(self, response):    

        _csrf = self.extract_from_xpath(response, "//input[@name='_csrf']/@value")
        print('_csrf ===',_csrf)

        formdata={'_csrf': _csrf,  
                  'LoginForm[username]': self.account,  
                  'LoginForm[password]': self.pwd, 
                  'LoginForm[rememberMe]':'0'}

        # 响应Cookie
        Cookie1 = response.headers.getlist('Set-Cookie')   #查看一下响应Cookie，也就是第一次访问注册页面时后台写入浏览器的Cookie
        print("响应Cookie ====",Cookie1)

        print('登录中')
        
        """第二次用表单post请求，携带Cookie、浏览器代理、用户登录信息，进行登录给Cookie授权"""
        return [FormRequest.from_response(response,
                                          url= self.meta['login_post_url'],   #真实post地址
                                          meta={'cookiejar':response.meta['cookiejar']},
                                          formdata=formdata,
                                          callback=self.after_login
                                          )]
    def after_login(self,response):
        yield scrapy.Request(url=self.meta['login_sucess_url'],callback=self.get_json_data,meta=response.meta)
    
    def get_json_data(self,response):
        # 请求Cookie
        Cookie2 = response.request.headers.getlist('Cookie')
        print("登陸成功後 cookie =====",Cookie2)
        
        a = response.body.decode("utf-8")   
        print("登录后响应信息 ====",a)

    
    def extract_from_xpath(self, response, xpath, return_first=True, return_selector=False, embedded_content=False):
        if return_selector:
            return response.xpath(xpath)
        else:
            if return_first:
                if embedded_content:
                    return response.xpath(xpath).xpath('string(.)').extract()
                return response.xpath(xpath).extract_first()
            return response.xpath(xpath).extract()
    
