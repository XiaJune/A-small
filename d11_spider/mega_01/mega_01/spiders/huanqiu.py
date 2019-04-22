# -*- coding: utf-8 -*-
import scrapy


class HuanqiuSpider(scrapy.Spider):
    name = 'huanqiu'
    allowed_domains = ['http://www.huanqiu.com']
    start_urls = ['http://www.huanqiu.com/']

    def parse(self, response):
        print('hello I am a creeper')
        print(type(response))
