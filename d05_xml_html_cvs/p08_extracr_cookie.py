import http.cookies
import http.cookiejar
import urllib.request
import ssl
"""
把请求的cookie保存成文件
1， 发起请求
2， 得到响应
3， 利用CookieJar类提供的函数，从Request,Response中抽取Cookie
4， 保存Cookie
"""
# 1, 发起请求urllib， request.openurl
request = urllib.request.Request(url='https://www.baidu.com')
# 2, 得到响应：上面会返回响应
response = urllib.request.urlopen(request, context=ssl._create_unverified_context())
# 3, 利用CookieJar类提供的函数，从Request,Response中抽取Cookie: 利用构造器构造
cookies = http.cookiejar.CookieJar()  # 还不支持保存
# cookies = http.cookiejar.LWPCookieJar() # 抽取cookie 加载cookie 保存cookie  配合save使用
# cookies = http.cookiejar.MozillaCookieJar()   # 保存在文件 配合save使用
# cookies = http.cookiejar.FileCookieJar()      # 抽象类 还未实现

cookies.extract_cookies(response=response, request=request)
# 4, 保存Cookie：利用FileCookieJar类或者子类

print(type(cookies))
for item_ in cookies:
    print(item_.name, item_.value, item_.path, item_.domain)

# cookies.save('b.txt')   # 保存在文件 save



