# -*- coding: utf-8 -*-
import scrapy
import tencent.items


class TtCourseSpider(scrapy.Spider):
    name = 'tt_course'
    allowed_domains = ['ke.qq.com']
    url = 'https://ke.qq.com/course/list/python爬虫工程师?price_min=1&page=%d'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
    }
    page_no = 1

    def start_requests(self):
        # 构建爬取的网站
        request = scrapy.Request(
            url=self.url % self.page_no,
            callback=self.extract_course,
            method='GET',
            headers=self.headers, errback=self.error_headle)
        return [request]

    def error_headle(self, err):
        print('无数据可爬取')


    def extract_course(self, response):
        output = []
        # 这里得到页面
        print('开始处理数据')
        # xpath 方法
        course = response.xpath('//div[@data-report-module="middle-course"]/ul/li')
        for course in course:
            item_ = tencent.items.TencentItem()
            # 机构
            item_['org'] = course.xpath('div/span/a/@title').get()
            # 价格
            item_['price'] = course.xpath('div/span[@class="line-cell item-price"]/text()').get()
            output.append(item_)
        print('---------------------------')
        if self.page_no <= 10:
            self.page_no += 1
            request = scrapy.Request(
                url=self.url % self.page_no,
                callback=self.extract_course,
                method='GET',
                headers=self.headers, errback=self.error_headle)
            output.append(request)

        return output


















