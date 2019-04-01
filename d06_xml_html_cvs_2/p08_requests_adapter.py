import requests
import requests.adapters

class MyAdapter(requests.adapters.BaseAdapter):
    def send(self, request, stream=False, timeout=None, verify=True, cert=None, proxies=None):
        print(type(request))
        print('对某些特殊的url进行独立的处理')
        if request.method.upper() == 'GET':     #  凡是用get方法的就进入 不然就 None
            resp = requests.api.get(request.url)
        else:
            resp = None
        resp = requests.api.get(request.url)
        return resp

session = requests.Session()
adapter = MyAdapter()

session.mount('https://', adapter=adapter)       # 挂载适配器 凡是用https请求的就好调用适配器 然后去调用类

response = session.get(
    url='https://www.baidu.com',
    headers={'Content-Type':'text/html;charset=UTF-8'}) # 解决乱码问题 编码 告诉对方要什么编码
print(response.content.decode('utf-8'))                 # 第二种解决方法 自己的编码问题