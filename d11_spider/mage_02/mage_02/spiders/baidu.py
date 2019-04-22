import scrapy

"""
scrapy爬虫引擎，调用爬虫程序，首先调用start_requests函数，
其中由返回的Request请求对象，来决定我们需要抓取网站的页面；

如果没有重载start_requests函数， 他的默认实现是从start_requests函数中循环获取爬取的页面url

|- 要么提供start_url
|- 要么提供start_requests函数


"""

class BaiduSpider(scrapy.Spider):
    name = 'baidu'

    def parse(self, response):
        print('数据处理')       #  不设置callback就调用默认的函数 有多个就全部调用
        print(response.body)

    def handle_data(self, response):
        print('绑定的处理函数, 调用自己的函数')
        print(type(response))
        print(response.text)

    def start_requests(self):
        print('开始爬虫')
        return [
            scrapy.Request('http://huanqiu.com', callback=self.handle_data), # 绑定选择调用的函数
            scrapy.Request('https://ke.qq.com'),
            scrapy.Request('https://ke.qq.com', dont_filter=True)   # (True)不过滤 就算设置了callback也会调用此函数
        ]

