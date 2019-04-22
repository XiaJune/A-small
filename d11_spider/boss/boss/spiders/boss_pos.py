import scrapy
import boss.items

class BossPosSpider(scrapy.Spider):
    name = 'boss_pos'
    page_no = 1

    # 3.1 爬取的条件
    url_page = 'https://www.zhipin.com/c101010100/?query=%s&page=%d$ka=page-next'
    # 3.2 爬取的条件header(已经设置到settings文件中) # 如果是定制的头就在这里写

    # 3, 重载爬虫的初始请求函数
    def start_requests(self):

        # 3.3 根据页数生成url
        url = self.url_page % (self.joname, self.page_no)
        # 3.4 创建一个请求对象
        request = scrapy.Request(
            url=url,
            method='get',
            callback=self.parse_pos,
            #errback=self.parse_err,
            dont_filter=True)   # 是否不过滤这条（True）不过滤
        return [request]        # 这里要返回列表
        # yield request         # 返回生成器



    def parse_pos(self, response):
        print('抽取职位数据（数据抽取， 是否继续爬取）')
        # 4.2 找到爬取区域
        list_job = response.xpath('//div[@class="job-list"]/ul/li')
        if len(list_job) == 0:
            return
        for job in list_job:
            # 4.3 解析职位的数据
            item = boss.items.PositionItem()
            item['岗位名称'] = job.xpath('div/div/h3/a/div/text()').get()
            item['薪水'] = job.xpath('div/div/h3/a/span/text()').get()
            item['招聘机构'] = job.xpath('div/div/div/h3/text()').get()
            item['地区'] = job.xpath('div/div/p/text()').get()
            item['行业'] = job.xpath('div/div/div/p/text()').get()
            yield item
        # 4.4 是否继续爬取
        self.page_no += 1
        url = self.url_page % (self.joname, self.page_no)
        # 3.4 创建一个请求对象
        request = scrapy.Request(
            url=url,
            method='get',
            callback=self.parse_pos,
            #errback=self.parse_err,
            dont_filter=True)  # 是否不过滤这条（True）不过滤
        yield request

def parse_err(self, error):
        print('处理爬取异常')































