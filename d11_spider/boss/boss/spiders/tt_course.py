# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TtCourseSpider(CrawlSpider):
    name = 'tt_course'
    allowed_domains = ['ke.qq.com']
    start_urls = ['http://ke.qq.com/']

    rules = (
        Rule(
            LinkExtractor(allow=r'course/\d{6}'),
            callback='parse_item',
            follow=True),
    )
    def parse_item(self, response):
        name = response.xpath()

        # item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
        print(response.url)



















