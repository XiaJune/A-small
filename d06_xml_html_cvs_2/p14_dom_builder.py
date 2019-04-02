import xml.dom
import xml.dom.xmlbuilder

# 构建  InputSource
input_source = xml.dom.xmlbuilder.DOMInputSource()
input_source.byteStream = open('books.xml', 'r')
# 构建Builder解析InputSource
builder = xml.dom.xmlbuilder.DOMBuilder()
doc = builder.parse(input_source)
print(doc)

# 会出'gbk' codec can't decode byte 0xbe in position 244: illegal multibyte sequence错误