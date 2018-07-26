# -*- coding: utf-8 -*-
import requests
import uuid
import time
import config
from lxml.html import fromstring
from download_center.store.store_oss import StoreOSS
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class GetAllInfo:
    def __init__(self,html):
        self.oss = StoreOSS(**config.EHCO_OSS)
        self.tree = fromstring(html.decode('utf-8','ignore'))

    def get_image_respone(self,url):
        '''
        下载指定url二进制的文件
        '''
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        }
        try:
            r = requests.get(url, timeout=20, stream=True, headers=headers)
            r.raise_for_status()
            # print '图片下载成功！url: {}'.format(url)
            time.sleep(1)
            return r.content
        except:
            print '图片下载失败！url: {}'.format(url)
            time.sleep(1)
            return None

    def up_to_server(self,respone, filename):
        '''
        将原图下载，并上传到阿里云服务器
        Args:
            url :图片的源地址
            filename:图片文件名
        '''
        # 设置文件目录
        web_folder = "comments/" + filename
        try:
            status = self.oss.put(web_folder, respone).status
            if status != 200:
                print '图片上传失败了'
            else:
                pass
                # print filename, '上传成功'
        except:
            pass
        else:
            # print("deal_response_image", url)
            pass

    def format_img_url(self):
        img_head = 'http://website201710.oss-cn-shanghai.aliyuncs.com/comments/'
        img_name = '{}.jpg'.format(uuid.uuid1())
        aliyun_url = '{}{}'.format(img_head, img_name)
        return aliyun_url, img_name

    # 获取公司图片并上传到阿里云
    def get_company_image(self):
        img_dict = {}
        img = self.tree.xpath('//*[@class="logo"]/div//img')[0]
        if img is not None:
            img_url = img.get('src')
            response = self.get_image_respone(img_url)
            if response:
                aliyun_url,filename = self.format_img_url()
                # self.up_to_server(response,filename)
                img_dict['old_img'] = img_url
                img_dict['new_img'] = aliyun_url
        return img_dict

    # 获取公司的基本信息
    def get_company_base(self):
        base_dict, base_list = {}, []
        company_name = self.tree.xpath(
            '//*[@id="company-top"]/div/div[2]/div[1]/text()')[0].strip()
        base_list.append(company_name)
        company_base = self.tree.xpath(
            '//*[@id="company-top"]/div/div[2]//span//text()')
        company_base = list(
            filter(lambda x: x, map(lambda x: x.strip(), company_base)))

        for i, each in enumerate(company_base):
            if any(x in each for x in ['电话', '邮箱', '官网', '地址']):
                base_list.append(company_base[i+1])
        for name, v in zip(['name', 'tel', 'email', 'website', 'address'], base_list):
            base_dict[name] = v
        return base_dict

    # 获取公司的详细经营信息
    def get_company_detail(self):
        detail_dict = {}
        all_name = ['register_capital', 'pay_capital','operate_state', 'establish_date', 
                    'register_number', 'organization_code', 'taxpayer_number', 'social_code', 
                    'company_type', 'industry', 'approval_date','register_authority', 'affiliated_area', 
                    'english_name', 'used_name', 'operate_mode','personnel_scale', 'business_term', 'scope_operation']
        
        all_company_detail = self.tree.xpath('//*[@id="Cominfo"]/table[2]//tr//text()')
        all_company_detail = list(
            filter(lambda x: x, map(lambda x: x.strip(), all_company_detail)))
        del(all_company_detail[-5:-1])

        for name,v in zip(all_name,all_company_detail[1::2]):
            detail_dict[name] = v
        return detail_dict

    # 获取股东信息
    def get_shareholder_detail(self):
        all_shareholder ,all_shareholder_dict= [],{}
        all_shareholder_detail = self.tree.xpath(
            '//*[@id="Sockinfo"]/table//tr//text()')
        all_shareholder_detail = list(filter(lambda x: x, map(
            lambda x: x.strip(), all_shareholder_detail)))[5:]
        all_shareholder_detail = [all_shareholder_detail[i:i+6]
                                for i in xrange(0, len(all_shareholder_detail), 6)]
        for each in all_shareholder_detail:
            del(each[1])
            all_shareholder.append(each)
        all_shareholder_dict['shareholder'] = all_shareholder
        return all_shareholder_dict

    # 获取主要人员信息
    def get_main_member(self):
        all_members,all_members_dict = [],{}
        all_main_member = self.tree.xpath('//*[@id="Mainmember"]/table//tr//text()')
        all_main_member = list(filter(lambda x: x, map(
            lambda x: x.strip(), all_main_member)))[3:][1::2]
        for name,v in zip(all_main_member[::2],all_main_member[1::2]):
            all_members.append((name,v))
        all_members_dict['member'] = all_members    
        return all_members_dict

    @property
    def get_detail(self):
        all_detail = {}
        img_dict = self.get_company_image()
        base_dict = self.get_company_base()
        detail_dict = self.get_company_detail()
        shareholder_dict = self.get_shareholder_detail()
        member_dict = self.get_main_member()
        all_detail.update(img_dict)
        all_detail.update(base_dict)
        all_detail.update(detail_dict)
        all_detail.update(shareholder_dict)
        all_detail.update(member_dict)
        return all_detail

if __name__ == '__main__':
    with open('xiaomi.html','r') as f:
        html = f.read()
    get_detail = GetAllInfo(html)
    get_allinfo = get_detail.get_detail
    print(get_allinfo)



