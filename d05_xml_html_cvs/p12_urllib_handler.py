import urllib.request
import ssl
import json
# 1, 构造一个请求
class BaiduHandler(urllib.request.BaseHandler):
    def default_open(self, req):
        req.add_header('Accept','application/json, text/javascript, */*; q=0.01')
        req.add_header('Connection', 'keep-alive')
        req.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
        req.add_header('Host', 'fanyi.baidu.com')
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36')

request = urllib.request.Request(
    url='https://fanyi.baidu.com/sug',   # url请求方式 地址
    data='kw=test'.encode('utf-8'),     # 请求的数据
    method='POST')    # 请求方法

handler = BaiduHandler()
opener = urllib.request.build_opener(handler)
urllib.request.install_opener(opener)

response = urllib.request.urlopen(request, context=ssl._create_unverified_context())
# 2, 发起请求
print(response.headers)
# print(response.read().decode('unicode_escape'))   # 解码方式
# eval   # 解码方式
data = response.read().decode()
json_d = json.loads(data)
print(json_d)