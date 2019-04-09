import requests
import bs4

# 下载数据
response = requests.get(url='https://ke.qq.com/course/list/python')
str_content = response.content.decode('utf-8')
# print(str_content)
# 解析 - 遍历
# 1. 加载数据
# doc = bs4.BeautifulSoup(markup=str_content,features='html')   # 加载不同的类型 吧
doc = bs4.BeautifulSoup(markup=str_content, features='html.parser') # features是解析器 按照填写的解析
# for sec in doc.html.body.children:            # xpath用/ 这里用的 . 点
#     print(len(sec))                             # 文档节点的个数

nodes = doc.find_all(
    name='div',                                                 # 节点名
    attrs={'data-report-module':'middle-course'},                   # 属性
    recursive=True,                                                # 是否递归
    text=None,                                                        # 文本
    limit=None)                                                     # 最大个数
print(nodes)











