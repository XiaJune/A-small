import requests
import lxml.etree
import re

req = {
    '':''
}
session = requests.Session()
response = session.post('https://movie.douban.com/', req)
content = response.content.decode()
doc = lxml.etree.HTML(content)  # 应该是获得HTML
tree = doc.getroottree()

nodes = tree.xpath('//div/[@class="slide-page"]/p/text()')
print(nodes)

