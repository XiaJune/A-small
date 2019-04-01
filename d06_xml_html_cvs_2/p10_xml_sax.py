import xml.sax
import xml.sax.handler
import xml.sax.expatreader

# 2. 继承ContentHandler处理数据
class MyHandler(xml.sax.handler.ContentHandler):
    def startDocument(self):
        print('读取到文档节点')

    def endDocument(self):
        print('文档结束')

    def startElement(self, name, attrs):
        print('节点名', name, attrs)

    def endElement(self, name):
        print('节点结束', name)

# 1. 创建一个reader读取器
xml_reader = xml.sax.expatreader.ExpatParser()
# 3. 把handler与reader绑定到一起
handler = MyHandler()
xml_reader.setContentHandler(handler=handler)

# 4. 输入数据开始工作
# xml_reader.feed(data='<books>PY书</books>')  # 可以是自己写的字符串

# fd = open('books.xml', 'r')# 这里是打开文件 读取文件
# print(type(fd))
# buffer = fd.read()
# fd.close()
# xml_reader.feed(data=buffer)

xml_reader.parse('books.xml')


