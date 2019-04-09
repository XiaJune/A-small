import requests
import lxml.etree
import re


request = requests.Request(
    method='GET',
    url='https://ke.qq.com/course/list/Python',
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
    },
    params={
        'price_min':1,
        'page':3

    })
# 产生一个可以发送的请求
pre_request = request.prepare()

# 发送请求
session = requests.Session()
response = session.send(pre_request)    # 发送请求
# 得到数据
content = response.content.decode()



#  ----------------数据解析
doc = lxml.etree.HTML(content)  # 应该是获得HTML
tree = doc.getroottree()        # 把节点变为节点树

# 所有的价格
# nodes = tree.xpath('//div[@data-report-module="middle-course"]/ul[@class="course-card-list"]/li/div[@class="item-line item-line--bottom"]/span[@class="line-cell item-price"]/text()')
# 所有的机构
node = tree.xpath('//div[@class="item-line item-line--middle"]/span[@class="item-source"]/a[@title]/text()')
# 购买的人数
# nodes = tree.xpath('//div[@class="item-line item-line--middle"]/span[@class="line-cell item-user"]/text()')
# s = re.compile(r'\w+\d')
# for sum in nodes:
#     sum = s.findall(sum)
#     length = len(sum)
#     if length:
#         print(sum)
#     else:
#         print('无人购买')


# 所有课
nodes = tree.xpath('//div[@data-report-module="middle-course"]/ul/li/h4[@class="item-tt"]/a/text()')
for x, y in enumerate(nodes):
    print(node[x],y)

# print(nodes,len(nodes))





