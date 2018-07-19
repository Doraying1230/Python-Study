# coding:utf-8

from urllib import parse,request
import json
import http
from urllib import request,parse
from http import cookiejar
#����cookie������
cj = http.cookiejar.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cj), request.HTTPHandler)
request.install_opener(opener)
#���������������
url = "http://passport.zujuan.com/login?jump_url="	 
method="post"
param = {"_csrf" : "d2MyX2FuUWMcV1AwV1gnJBQwAwwkIyYhGxEFOhUGAxIvUQYlUhwzVA==","user-name" : "13653978879","user-pwd" : "123456"}
#json������ʹ��
textmod = json.dumps(param).encode(encoding='utf-8')
textmod = parse.urlencode(textmod).encode(encoding='utf-8')
print(textmod)
#�������
header_dict  = {
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
'Host':'passport.zujuan.com',
'Origin':'http://passport.zujuan.com',
'X - Requested - With': 'XMLHttpRequest',
'Connection': 'keep - alive'
    }

 
req = request.Request(url=url,data=textmod,headers=header_dict)
res = request.urlopen(req)
rescontent = res.read()
#print(rescontent)
print(rescontent.decode(encoding='utf-8'))
print(djhK)