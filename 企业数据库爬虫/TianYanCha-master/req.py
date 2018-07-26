import redis
import requests
import json

s = requests.Session()

r = redis.Redis(host='58.221.49.26',password='123456')
keys = r.keys('cookies:tianyancha:*')

cookies = [json.loads(r.get(key)) for key in keys]

url = 'https://www.tianyancha.com/company/2802426215'

headers = {
    'Host':'www.tianyancha.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Accept': 'text/html,applicatiion/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q-0.9',
}

#response = requests.get(url=url, cookies=cookies[0], verify=False)
response = s.get(url=url, headers=headers, cookies=cookies[0], verify=False)

print(response.status_code)
with open('jj.html','w', encoding='utf-8') as f:
    f.write(response.text)
