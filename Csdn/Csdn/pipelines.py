# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CsdnPipeline(object):
    # 必须有一个这样命名的函数
    def process_item(self, item, spider):
        print(item['title'])
        print(item['time'])
        print(item['number'])
        # 这里必须保留，以便给其他的pipeline使用
        return item
