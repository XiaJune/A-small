import requests
import lxml.etree
import re


user_request = requests.Request(
    method='GET',
    url='https://www.guazi.com/bj/bmw/',
    headers={
        'Cookie': 'uuid=1b7c35f0-a0e4-4710-ca80-030b348bd615; user_city_id=12; ganji_uuid=4082402707404554228494; lg=1; cityDomain=bj; antipas=2978071K30Vq1094D1405c6P67; clueSourceCode=%2A%2300; sessionid=4cb085e1-1eb5-4085-b20f-10add545cc05; Hm_lvt_936a6d5df3f3d309bda39e92da3dd52f=1555548945; cainfo=%7B%22ca_s%22%3A%22seo_bing%22%2C%22ca_n%22%3A%22default%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22%7Bkeyword%7D%22%2C%22ca_content%22%3A%22%22%2C%22ca_campaign%22%3A%22%22%2C%22ca_kw%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%2216353740128%22%2C%22scode%22%3A%2210103213212%22%2C%22ca_transid%22%3A%22%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22ca_i%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_a%22%3A%22-%22%2C%22display_finance_flag%22%3A%22-%22%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%221b7c35f0-a0e4-4710-ca80-030b348bd615%22%2C%22sessionid%22%3A%224cb085e1-1eb5-4085-b20f-10add545cc05%22%7D; close_finance_popup=2019-04-18; preTime=%7B%22last%22%3A1555549125%2C%22this%22%3A1555482791%2C%22pre%22%3A1555482791%7D; Hm_lpvt_936a6d5df3f3d309bda39e92da3dd52f=1555549126',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
    })

# 产生可以发送的请求
pre_request = user_request.prepare()
session = requests.session()            # 创建一个会话
response = session.send(pre_request)    # 吧请求通过会话发送出去

content = response.content.decode('utf-8')
# print(content)

doc = lxml.etree.HTML(content)

tree = doc.getroottree()


nodes = tree.xpath('//div/ul/li/a/div[@class="t-price"]/p/text()')
print(len(nodes))
title = tree.xpath('//div/ul/li/a/h2/text()')
print(len(title))
for i,x in enumerate(nodes):
    node = re.findall(r'\w.+', x)

    print(f'{title[i]}   折后{node[0]}万元')


# 爬不了的时候吧cookie换一下就行
