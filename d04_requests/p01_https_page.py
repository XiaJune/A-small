# coding = utf-8
import socket
import ssl
import re

def read_line(sock):        # 再socket中读一行
    buffer = b''
    while True:
        buf = sock.recv(1, 0)
        buffer += buf
        last_two_bytes = buffer[-2:]
        if last_two_bytes == b"\r\n":
            break
    return buffer

def read_bytes(s, size):        # 读取指定长度的数据
    buffer = b''
    size_ = size
    while size_ != 0:
        buf = s.recv(size_, 0)
        buffer += buf
        # 计算剩余的字节
        size_ -= len(buf)
    return buffer

server_addr = ('www.baidu.com', 443)

#  创建socket
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
# 包装socket
ssl_sk = ssl.wrap_socket(sk)
# 连接https服务器
ssl_sk.connect(server_addr)
# 发起数据请求
str_request = 'GET / HTTP/1.1\r\n'  # 什么请求什么协议
str_request += F'Host: {server_addr[0]}\r\n'    # 主机地址
str_request += 'Accept: text/html\r\n'      # 数据接收范围
                #  下面这是代理  如果不写就是普通的
str_request += 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36\r\n'
str_request += 'Accept-Language: zh-cn\r\n' #接收语言  中国
str_request += 'Connection: keep-alive\r\n'
str_request += '\r\n\r\n'

ssl_sk.send(str_request.encode('utf-8'), 0)
# 接收服务器响应
# 开始分许数据（行，头， 空行，数据体）
# 读取头信息
buf_header = b''
while True:
    buf = ssl_sk.recv(1, 0)
    buf_header += buf
    # 取buf_header最后4个字节
    last_four_byte = buf_header[-4:]
    if last_four_byte == b'\r\n\r\n':
        print('响应头读取完毕')
        break
# 分析头信息
str_header = buf_header.decode('utf-8')
print(str_header)
# 识别Transfer-Encoding: 头，得到数据chunked
regexp = r'Transfer-Encoding: (.*)\r\n'
result = re.findall(regexp, str_header, re.MULTILINE)
if result and result[0] == 'chunked':
    print('分包')
    buf_content = b''
    len_package = -1
    while len_package != 0:
        # 读取包的大小
        buf_line = read_line(ssl_sk)
        str_line = buf_line[:-2].decode('utf-8')
        print('读取的包长度', buf_line)
        len_package = int(str_line, 16)
        print('包的大小', len_package)
        # 丢两个字节
        read_bytes(ssl_sk, 2)
        # 读取 len_package 长度的数据
        buffer = read_bytes(ssl_sk, len_package)
        buf_content += buffer
    # 读取完毕
    print('读取完毕')
else:
    print('非分包')
