import requests

# 请求
usr_request = requests.Request(
    url='http://fy.webxml.com.cn/webservices/EnglishChinese.asmx/TranslatorString',
    method='POST',
    data=[('wordKey', 'handsome')],
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
    }
    )
# 编译请求
pre_request = usr_request.prepare()
# 发起请求
with requests.Session() as session:             # 上下文操作
    response = session.send(pre_request)
    # 处理响应xml（MP3文件base64加密）
    # print(response.text)          # 拿到的属性
    # print(response.raw)             # 成员变量
    # print(response.request)         # 什么请求
    # print(response.status_code)     # 状态码
    # print(response.reason)          # 请求结果
    # print(response.elapsed)         # 请求时间
    # print(response.encoding)        # 请求编码
    # print(response.history)         # 请求历史
    # print(response.headers)         # 头部信息
    # print(response.cookies)         # cookie信息

    # it = response.iter_content(chunk_size=1, decode_unicode=True)   # 按照多少字节读取（chunk_size）
    # print(it) # 上面返回是一个迭代器
    # for item_ in it:
    #     print(item_)

    lines = response.iter_lines(chunk_size=512)   # 解析行的时候 每次缓冲的大小， 默认512   返回都是byes
    print(type(lines))
    for item_ in lines:
        print(item_)