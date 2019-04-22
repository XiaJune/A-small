# -*- coding: utf-8 -*-
import scrapy


class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = ['ke.qq.com']
    start_urls = ['https://ke.qq.com/']

    def parse(self, response):
        print('处理爬取结果')
