import http.client

conn = http.client.HTTPConnection('www.huanqiu.com', 80)

conn.request(
    method='GET',    # 请求方法
    url='/',         #资源
    body='kw=test',  #请求数据
    headers={        # 发送的头 指定不压缩格式
        'Accept-Encoding':'identity',
        'Content-Type': 'text/html;charset=utf-8'
    })
response = conn.getresponse()
print(type(response))
print(response.headers == response.info())
print(2,response.info())
cont = response.read()
print(cont.decode())


