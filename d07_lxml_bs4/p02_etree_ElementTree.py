import xml.etree.ElementTree

tree = xml.etree.ElementTree.ElementTree(file='books.xml')      # 只加载文件
# print(tree)

# tree2 = xml.etree.ElementTree.ElementTree()       # 第二种方式
# tree2.parse('books.xml')
# print(tree2)
# list的方式遍历：访问：节点名，属性，文本，子结点
root = tree.getroot()
for ele_ in root:
    print(ele_.tag, ele_.attrib, ele_.text)
    for e_ in  ele_.getchildren():
        print(ele_.tag, ele_.attrib, ele_.text)

# 使用xpath的方式查找tree：Element支持xpath, find
# find()     =>   找到第一个就返回
# findall()  =>   找到所有返回
# findtext() =>   找到节点 返回节点的文本

