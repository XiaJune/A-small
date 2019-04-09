import requests
import lxml.etree
import re

session = requests.Session()
response = session.get('http://www.baidu.com')
content = response.content.decode()
# print(content)

# -------------解析

doc = lxml.etree.HTML(content)
tree = doc.getroottree()
nodes = tree.xpath('//title/text()')
for i in nodes:
    print(i)



