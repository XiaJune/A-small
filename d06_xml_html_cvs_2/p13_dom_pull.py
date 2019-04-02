import xml.dom
import xml.dom.pulldom

result = xml.dom.pulldom.parse('books.xml')
print(result)
print(result.getEvent())
event, doc = result.getEvent()

print(event, doc)
