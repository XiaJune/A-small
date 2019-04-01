import requests

def myhook(resp, *args, **kwargs):
    print(type(resp), args, kwargs)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(type(resp))       # 也可以在这里处理response 返回

user_request = requests.Request(
    method='get',
    url='https://www.baidu.com',
    hooks={'response':myhook})

"""
字典的key只能是response
"""

pre_request = user_request.prepare()

session = requests.Session()
response = session.send(pre_request)

print(response.text)

