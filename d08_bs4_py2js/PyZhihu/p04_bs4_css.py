import requests
import bs4

# 下载数据
response = requests.get(url='https://ke.qq.com/course/list/python')
str_content = response.content.decode('utf-8')
# print(str_content)
# 解析 - 遍历
# 1. 加载数据
# doc = bs4.BeautifulSoup(markup=str_content,features='html') # features是解析器 按照填写的解析
doc = bs4.BeautifulSoup(markup=str_content, features='html.parser')

nodes = doc.select('ul > li')               #返回的是迭代器
print(len(nodes), list(nodes)[0].get_text())














