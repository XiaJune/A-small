"""
    功能： 实现百度翻译sug与v2transapi的HTTP XHR请求的封装实现
    作者： Miller
    日期： 2019-04-10
"""
import requests
import re

class BaiduCrawler:
    def __init__(self):
        self.__grk = None
        self.__token = None
        self.__sign =None
        # 初始化http请求的session，header
        self__session = requests.session()

        # 加载fanyi.baidu.com 获取token 获取gtk
        self.__get_gtk_token()

    def sug(self, kw):
        return '为实现'

    def v2transapi(self, kw):
        # 利用输入的被翻译的词，生成sign
        self.__get_sign(kw)
        # 加载js脚本
        # 加载js脚本，适应gtk替换window[L]
        # 调用js脚本e函数，产生sign(签名)

        # 生成请求data （关键： token， sign）
        data={
            'from':'en',
            'to':'zh',
            'query':'kw',
            'transtype':'realtime',
            'simple_means_flag':'3',
            'sign': self.__sign,
            'token':self.__token
        }
        # 发起请求，获得数据
        return '没有实现'

    def __get_gtk_token(self):
        response_home = self.__session.get(url='https://fanyi.baidu.com')
        str_home =response_home.content.decode('utf-8')

        self.__token = re.findall(r"token: '(.*)',", str_home)[0]
        self.__gtk = re.findall(r";window.gtk = '(.*)';", str_home)[0]
        print(self.__token)
        print(self.__gtk)

    def __get_sign(self, kw):
        # 加载js脚本

        # 加载js脚本，s
        self.__sign = None



