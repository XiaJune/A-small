import xml.etree.ElementTree

"""
编程模型：
    1. 构造Parser
        |- feed(数据)： 数据是解码字符串，还是字节字符串
    2. 指定parser的构造器（TreeBuilder）
        |- 可以默认
    3. 返回的结果ElementTree或者Element
"""
class Mybuilder(xml.etree.ElementTree.TreeBuilder):
    is_root = True
    root_ele = None
    def start(self, tag, attrs):
        ele = super().start(tag, attrs)
        if self.is_root:
            self.root_ele = ele
            self.is_root = False
        # print('start', ele)
        return ele

builder = Mybuilder()
parser = xml.etree.ElementTree.XMLParser(target=builder)
fd = open('books.xml', 'r')
data = fd.read()
parser.feed(data)       # 可以传字符串  文件

root = builder.root_ele
print(root)

