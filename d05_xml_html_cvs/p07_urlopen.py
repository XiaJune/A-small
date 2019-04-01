import urllib
import urllib.request
import ssl

# request = urllib.request.Request(
#     url='http://www.huamqiu.com',
#     method='get',
#     data='',
#     headers={})
# 判断request是字符串直 使用某些参数 直接调用Request类构造对象
# result = urllib.request.urlopen(request,)         #  下面注释等价 两种方式都可以

# result = urllib.request.urlopen(url='http://www.huanqiu.com',
#     method='get',
#     data='',
#     headers={})

ctx = ssl._create_unverified_context()          # ssl使用于https
result = urllib.request.urlopen('https://www.baidu.com', context=ctx)   # urlopen构造一个请求

print(result)   # 得到 http.client.HTTPResponse
print(result.status, result.reason)
print(result.headers)
print(result.read().decode('utf-8'))


