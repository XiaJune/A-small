import requests
# import nm
import time
import sys
import bs4
from hashlib import sha1
# import execjs


class ZhihuLogin:
    def login(self, username, password):
        print('开始登录')
        # 1， 判定是否校验码
        input_captcha = ''
        if self.is_captcha():
            # 1.1 下载校验码
            self.down_captcha()
            # 1.2 校验校验码
            # 输入效验码
            input_captcha = input('请输入校验码')
            self.check_captcha(input_captcha)
        # 2. 直接登录
        is_ok = self.check(username, password, input_captcha)
        # 3. 下载首页， 爬取首页主题
        if is_ok:
            self.crawler_home()

    def is_captcha(self):
        print('判定是否需要下载校验码')
        return True
    def down_captcha(self):
        print('下载校验码')
    def check_captcha(self):
        print('校验码验证')
        pass
    def check(self, username, password, captcha):
        # 生成签名
        # 加密
        # 提交
        print('用户登录')
        return True
    def crawler_home(self):
        print('爬取主页')
        pass

obj_login = ZhihuLogin()
obj_login.login('13658074875', 'xj13658074875')

