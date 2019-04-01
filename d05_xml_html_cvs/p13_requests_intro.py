import requests

session = requests.Session()
response = session.get('https://www.baidu.com')
print(type(response))
# print(response.content.decode('utf-8'))   # 获得内容
# print(response.text)
print(response.__attrs__)   # 获得所有的属性
print(response.history)     #（history 访问历史）

