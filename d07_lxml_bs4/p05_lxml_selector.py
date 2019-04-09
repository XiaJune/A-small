import requests
import cssselect
import lxml.etree


# 下载页面
response = requests.get(url='http://ke.qq.com/coure/list/python')
str_content = response.content.decode('utf-8')

# 使用selector解析数据
# parser = lxml.etree.HTMLParser()        #这个是解析器 应该是解析HTML吧
# doc = lxml.etree.parse('文件', parser=parser)   # 第一种

doc = lxml.etree.HTML(str_content)      # 第二种
# print(doc)
# 解析第一步 构建节点树  （选择一 用xpath）
# tree = doc.getroottree()

# 如果需要 可以得到根节点（选择二）
# doc.cssselect('', transator='html') #实际上底层只支持xpath 翻译成html支持的xml
# nodes = doc.cssselect('section')    # 在整个html中寻找section这个节点
# nodes = doc.cssselect('section，html')    # 这个是或 找section或者html
# nodes = doc.cssselect('html section')   #  这个是html所有的后代的section节点
# nodes = doc.cssselect('div > ul')       # 找出div下的直接子节点
# nodes = doc.cssselect('div + ul')         # 找div跟ul兄弟节点（紧邻节点）

# nodes = doc.cssselect('#js_main_nav')             # id选择器
# nodes = doc.cssselect('.main.autoM.clearfix')       # 类选择器（. 点）

nodes = doc.cssselect('div[data-report-module]')    # 属性选择器（前面可以加标签可以不加结果不一样）
# nodes = doc.cssselect('div[data-report-module="middle-course"]')    #加上属性查找更精确
print(len(nodes), nodes)































