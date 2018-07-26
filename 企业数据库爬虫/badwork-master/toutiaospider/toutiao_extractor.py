# -*- coding: utf-8 -*-
"""
Created on 2018/1/12 11:41

@author: zhangle
"""
from download_center.new_spider.spider.spider import SpiderExtractor
import json
import HTMLParser


class ToutiaoExtractor(SpiderExtractor):
    """
    解析
    """

    def __init__(self):
        super(ToutiaoExtractor, self).__init__()
        self.html_parser = HTMLParser.HTMLParser()

    def extractor(self, text):
        """
        将一个页面文本解析为结构化信息的字典
        Args:
            text: 需要解析的文本
        Returns:
            数组: 每条为一个完整记录，记录由字典格式保存
        """
        results = dict()
        try:
            info = text.split("BASE_DATA")[1].split(";</script>")[0].strip()
            if info:
                category = info.split("chineseTag: '")[1].split("'")[0].strip()
                title = info.split("title: '")[1].split("'")[0].strip()
                content = info.split("content: '")[1].split("'")[0].strip()
                publish_time = info.split("time: '")[1].split("'")[0].strip()
                abstract = info.split("abstract: '")[1].split("'")[0].strip()
                tags = json.loads(info.split("tags: ")[1].split("],")[0].strip()+"]")

                results['category'] = category
                results['title'] = title
                results['publish_time'] = publish_time
                results['content'] = self.html_parser.unescape(content)
                results['category'] = category
                results['abstract'] = abstract
                results['tags'] = ",".join([v['name'] for v in tags])
        except Exception, e:
            pass
        return results

if __name__ == '__main__':
    extractor = ToutiaoExtractor()
    with open("sample.txt", "rb") as f:
        #
        returntext = extractor.extractor(f.read())
        for re in returntext:
            print re, returntext[re]
