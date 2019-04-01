import http.cookiejar

cook = http.cookiejar.MozillaCookieJar('a.txt')     # 找到格式对应保存的文件
cook.load(ignore_discard=True, ignore_expires=False)    # 把cookie读取出来
for item_ in cook:
    print(item_.name)
