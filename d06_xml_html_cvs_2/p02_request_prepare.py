import requests.sessions
import requests.models

# 构造请求
pre = requests.models.PreparedRequest()
pre.prepare_method('get')
# pre.prepare_url(
#     url='https://ke.qq.com/course/list/prthon',
#     params={                            #  请求的数据 参数
#         'price_min':1,
#         'page':4
#     },
#     )
# pre.prepare_headers(
#     headers={
#         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
#     }
#     )

pre.prepare(          #  封装用户定位请求数据
    method='get',                       #  请求方法
    url='https://ke.qq.com/course/list/prthon',                             #  请求url
    params={                            #  请求的数据 参数
        'price_min':1,
        'page':4
    },
    headers={                           #  请求头 下面是用户代理
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
    }
    )
# 发送请求
session = requests.sessions.Session()
response = session.send(pre)
print(response.text)