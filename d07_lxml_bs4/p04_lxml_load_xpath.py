import requests
import lxml.etree

# -------------------数据下载
# 1. 产生用户请求
usr_request = requests.Request(
    method='GET',
    url='https://ke.qq.com/course/list/Python',
    headers={          # 建议加上User-Agent  其他的需要时加上
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
    },
    params={
        'price_min':'1',
        'page':2})
# 2. 产生可以发送的请求
pre_request = usr_request.prepare()
# 3. 发送请求
session = requests.Session()
response = session.send(pre_request)

# 4. 得到需要的数据
content = response.content.decode('utf-8')
# print(content)


# -------------------- 数据解析
# 1. 加载数据，产生节点：节点数 <-> 节点
# parser = lxml.etree.HTMLParser()
# # text = html或者xml数据，， parser = 指定的解析器， base_url = ''指定html种存在的相对资源
# doc = lxml.etree.fromstring(content, parser=parser)  # 可以加上parser=parser 也可以不需要

doc = lxml.etree.HTML(content)          # 跟上面两行代码执行结果一样 把上面封装在HTML里面的

# 2. 对节点与节点，进行解析
# 第一种遍历方法
# length = len(doc)
# for idx in range(length):
#     print(doc[idx])
# 第二种遍历方法
# for e in doc:
#     print(e)
# it = iter(doc)      # 返回迭代器  可以用next使用
# print(type(it))

# 第三种遍历方式（节点管理操作）
# nodes = doc.getchildren()
# for node_ in nodes:
#     print(node_)

# 把节点变换为树
# tree = doc.getroottree()
# print(tree)

# 节点的想关数据：属性attrib，节点名tag, 节点文本：text tail
# for e in doc:
#     print(e.attrib, e.tag, e.text)

# 属性提供给几个特殊函数get（） 某个属性值，items(), keys(), values()
# for e in doc:
#     print(e.items(), e.keys(), e.values(), e.get('no', '缺省值'))

# 1. find 方法
# nodes = doc.findall('span')
# print(nodes)

# 节点的根：只有树才有根，才能使用 /
# . 标签是当前节点的意思
#  双 // 表示所有的后代节点
# nodes = doc.findall('body/.//div')    # 都使用相对位置 没有根的概念
# print(len(nodes))
# tree = doc.getroottree()        #  这里返回树
# nodes = tree.findall('//div')
# print(len(nodes))

# nodes = doc.findall('body/..')      # 两个点表示上一级节点
# print(len(nodes), nodes[0])
# tree = doc.getroottree()        #
# nodes = tree.findall('/body/..')
# print(len(nodes), nodes[0])

# find不是严格的xpath， @ 这个语法find不处理
# 取属性  的方法
# nodes = doc.xpath('body/header/@id')
# print(len(nodes), nodes[0])
# tree = doc.getroottree()        #
# nodes = tree.xpath('/html/body/header/@id')
# print(len(nodes), nodes[0])

# 取文本节点
# nodes = doc.xpath('body/div')
# print(len(nodes), nodes[0])
# tree = doc.getroottree()        #
# nodes = tree.xpath('/html/body/header')
# print(len(nodes), nodes[0])

# 使用positon()获取位置，并且做测试
# 属性测试
# tree = doc.getroottree()
# nodes = tree.xpath('/html/body/header/div/div/[@class="header-index-text"]')
# print(len(nodes), nodes)
# 访问技巧
tree = doc.getroottree()
# nodes = tree.xpath('//div[@data-report-module="middle-course"]/ul[@class="course-card-list"]/li/div[@class="item-line item-line--bottom"]/span[@class="line-cell item-price"]/text()')
nodes = tree.xpath('//div[@class="item-line item-line--middle"]/span[@class="item-source"]/a[@title="马哥教育"]/text()')



print(len(nodes), nodes)

















