import requests.sessions
import requests.models
"""
method=None,    : 方法请求get post
url=None,       ：请求的url
headers=None,   : 请求头部
cookies=None,   ： 特殊的头（name=value, 一堆的属性： 有过期属性，安全属性，domain属性， path属性）
params=None,    ： 请求的querystring 

files=None,     |           |- multipart
data=None,      |-  构造格式 |- form-urlencoding    # 3中数据格式只能3选一
json=None,      |           |- application/json

auth=None,      : 传递服务器登录信息
hooks=None,     : 与HTTP无关，编程默许下的请求的回调（服务器响应后进行的处理）
                    |- 请求，响应分离处理

"""

# 1. 构造用户格式的请求
usr_request = requests.models.Request(
    method='POST',
    url='http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx/getMobileCodeInfo',
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
    },
    data=[('mobileCode', '13658074875'),('userID', '' )])
# 2. 编译成可以发送的请求
pre_request = usr_request.prepare()
# 3. 发送请求
session = requests.sessions.Session()
response = session.send(pre_request)
# 4. 处理请求
print(response.text)