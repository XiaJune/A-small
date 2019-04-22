# -*- coding: utf-8 -*-
import scrapy
import scrapy.loader
import re


class LoaderSpider(scrapy.Spider):
    name = 'loader'
    allowed_domains = ['ke.qq.com']
    url = 'https://ke.qq.com/course/list/Python开发?page=1'

    def start_requests(self):
        request = scrapy.Request(
            url=self.url,
            callback=self.item_handle,
        )
        yield  request

    def item_handle(self, response):
        # 定位处理的节点
        course_list = response.xpath('//div[@data-report-module="middle-course"]/ul/li')
        # 循环处理课程内容
        for course in course_list:
            # 创建item对象
            item = CourseItem()
            # 定义加载器
            loader = scrapy.loader.ItemLoader(item=item, selector=course)
            # loader = CourseItemLoader(item=item, selector=course)  # 自己定义的加载器
            loader.context = {'p1':20, 'p2':30}
            #添加xpath， 或者css或者value
            loader.add_xpath('机构名称', 'div/span/a/text()')
            loader.add_css('课程名称', 'h4 > a::text')

            loader.add_xpath('学习人数', 'div[@class="item-line item-line--middle"]/span/text()')
            loader.add_css('课程价格', 'div[class="item-line item-line--bottom"] > span::text')    # add.css里面的属性查找没有@符号
            # loader.add_value('课程价格', '8888')      # add.value可以自己填值

            # 返回数据
            yield loader.load_item()


def in_handle(value):
    # print('数据输入处理细节')
    s = str(value[0])
    reg = re.findall(r'\w.+', s)
    return reg

def out_handle(value):
    # print('数据输出细节处理')
    return value[0]

class CourseItem(scrapy.Item):
    机构名称 = scrapy.Field(input_processor=in_handle,
        output_processor=out_handle,)
    课程名称 = scrapy.Field(input_processor=in_handle,
        output_processor=out_handle,)
    学习人数 = scrapy.Field(input_processor=in_handle,
        output_processor=out_handle,)
    课程价格 = scrapy.Field(
        input_processor=in_handle,
        output_processor=out_handle,
    )

# def xxx(self,value, loader_context):     # 必须传递上下文的环境loader_context
#     print('人数处理前')
#     return value
# def yyy(self,value, loader_context):
#     print('人数处理后')
#     return value
# class CourseItemLoader(scrapy.loader.ItemLoader):       #  自己定义的加载器还继承了父类的
#     # 字段名_in    # 输出处理
#     # 字段名_out   # 实际上是输出处理
#     d_in = xxx
#     o_out = yyy







