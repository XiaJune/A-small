import requests
import lxml.etree
import bs4

# 下载数据
# response = requests.get(url='https://ke.qq.com/course/list/python')
# str_content = response.content.decode('utf-8')
# # print(str_content)
# # 解析 - 遍历
# # 1. 加载数据
# # doc = bs4.BeautifulSoup(markup=str_content,features='html') # features是解析器 按照填写的解析
# doc = bs4.BeautifulSoup(markup=str_content, features='html.parser')
# # print(doc)
# # 2.传统遍历
# nodes = doc.children        #  返回的一个列表迭代器
# for node in nodes:
#     if isinstance(node, bs4.element.Comment):       # 是否有注释
#         print(node.PREFIX, node, node.SUFFIX)





