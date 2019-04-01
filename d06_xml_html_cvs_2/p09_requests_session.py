import requests

session = requests.Session()

req1 = requests.Request(
    method='get',
    url='https://fanyi.baidu.com',

    )

pre_req1 = req1.prepare()

req2 = requests.Request(url='https://fanyi.baidu.com/sug', method='POST', data=[('kw', 'test')])
pre_req2 = req2.prepare()

# 输出观察 headers  cookies
print(1,session.headers)
print(1,session.cookies)        # 响应前cookie
session.send(pre_req1)
print(2,session.headers)
print(2,session.cookies)        #响应第一次的cookie  会保留cookie下一次访问
# 输出观察 headers  cookies
session.send(pre_req2)
print(3,session.headers)
print(3,session.cookies)        #响应第二次的cookie   会带上cookie下一次访问
