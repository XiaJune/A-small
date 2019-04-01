import socket

ip_addr = ('www.huanqiu.com', 80)
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)


sk.connect(ip_addr) # 连接到地址服务器

str_request = 'GET / HTTP/1.1\r\n'
str_request += F'Host:{ip_addr[0]}\r\n'
str_request += 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\n'
str_request += 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36\r\n'
str_request += 'Accept-Language: zh-CN,zh;q=0.9\r\n'
# str_request += 'Accept-Encoding: gzip, deflate, br\r\n'  #指定了压缩格式
str_request += 'Connection: keep-alive\r\n'
str_request += '\r\n\r\n'

# 发送数据到服务器
sk.send(str_request.encode())

# 接收服务器的数据
while True:
    buf = sk.recv(4*1024, 0)
    if not buf:
        break
    print(buf.decode('UTF-8'))


