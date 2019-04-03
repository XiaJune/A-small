from xml.etree.ElementTree import ElementTree

tree = ElementTree(file='books.xml')
# e = tree.findall('book')      # 下面这都是第一种查找
# print(e)
# e = tree.find('book')         # 当前节点的子结点种搜索
# print(e.tag, e.attrib, e.text)
#
# e = tree.findtext('book/title')   # 根节点， 节点路径分隔符
# print(e)

# e = tree.findall('book/price')      #   下面是第二种查找
# for e_ in e:
#     print(e_.tag, e_.text)


# e = tree.findall('book//title')      #  所有子结点与孙子系欸但
# for e_ in e:
#     print(e_.tag, e_.text)


# e = tree.findall('book/./title')        # 当前节点
# for e_ in e:
#     print(e_.tag, e_.text)


# e = tree.findall('book/title/..')      #   父节点
# for e_ in e:
#     print(e_.tag, e_.text)

# XPATH + XQuery + XLink -> XSTL(dom + css) 文档和样式分离的原始技术
e = tree.findall('book[@no="0001"]')      # 使用节点的属性查找 谓词操作[@]
for e_ in e:
    print(e_.tag, e_.text)