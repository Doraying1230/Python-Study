# -*- coding: utf-8 -*-
"""
 @Time: 2017-11-1
 @Author: Ehco1996
"""
import os
import sys


import requests
import time
import uuid
import config

from download_center.store.store_oss import StoreOSS


class Image_to_server(object):
    def __init__(self):
        self.oss = StoreOSS(**config.EHCO_OSS)

    def get_image_respone(self, url, headers={}, data=None):
        '''
        下载指定url二进制的文件
        '''
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        }
        try:
            r = requests.get(url, timeout=30, stream=True, headers=headers)
            r.raise_for_status()
            print '图片下载成功！url: {}'.format(url)
            time.sleep(1)
            return r.content
        except:
            print '图片下载失败！url: {}'.format(url)
            time.sleep(1)
            return -1

    @staticmethod
    def encoding(self, data):
        types = ['utf-8', 'gb2312', 'gbk', 'gb18030', 'iso-8859-1']
        for t in types:
            try:
                return data.decode(t)
            except Exception:
                pass
        return None

    def save_file(content):
        with open('text.jpg', 'wb') as f:
            f.write(content)

    def get_new_url(self):
        '''
        返回新的url地址
        Args:
            url :图片的源地址
        Returns
            url :图片的新地址
        '''
        image_head = "http://website201710.oss-cn-shanghai.aliyuncs.com/p2p/"
        file_name = '{}.jpg'.format(uuid.uuid1())
        new_url = image_head + file_name
        return new_url

    def up_to_server(self, url, filename):
        '''
        将原图下载，并上传到阿里云服务器
        Args:
            url :图片的源地址
            filname:图片文件名
        '''
        # 设置文件目录
        web_folder = "p2p/" + filename
        # 图片的respones
        img_content = self.get_image_respone(url)
        if img_content:
            try:
                status = self.oss.put(web_folder, img_content).status
                if status != 200:
                    print '图片上传失败了'
                else:
                    print filename, '上传成功'
            except:
                pass
        else:
            print("deal_response_image", url)
        time.sleep(1)
