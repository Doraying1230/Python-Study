# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from .model import Base, engine, loadSession
from .model import tianyancha


class TianyanchaPipeline(object):
    Base.metadata.create_all(engine)

    def process_item(self, item, spider):
        a = tianyancha.Tianyancha(
            _id=item['_id'],
            title=item['title'],
            url=item['title'],
            update_time=item['update_time']
        )
        session = loadSession()
        session.add(a)
        session.commit()
        return item



