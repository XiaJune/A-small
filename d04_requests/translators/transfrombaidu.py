import socket
import ssl
import re
import json
from PyQt5.QtCore import QObject
"""
负责爬取内容
"""
class BaiDuTranslator(QObject):
    def __init__(self):
        super().__init__()
        # 定义属性 请求头
        self.request = 'POST /sug HTTP/1.1\r\n'
        self.request += 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8\r\n'
        self.request += 'Host: fanyi.baidu.com\r\n'       # 爬取的网站地址
                            # 下面是用户代理
        self.request += 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36\r\n'
        self.request += 'Content-Length: {length}\r\n'  # 数据长度
        self.request += 'Connection: Close\r\n'     # 爬取完关闭
        self.request += '\r\n'
        self.request += 'kw={keyword}'  # 需要爬取的内容传参数

    def translatedd(self, kw):
        print('开始翻译', kw)
        # 创建socket
        sock_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        # 包装socket
        ssl_sock_ = ssl.wrap_socket(sock_)    # 包装sock
        # 链接
        ssl_sock_.connect(('fanyi.baidu.com', 443)) # 链接对象跟端口
        # 发送请求
        l = kw.encode('utf-8')
        str_request_ = self.request.format(length=len(l)+3, keyword=kw) # 加上了3个长度keyword

        ssl_sock_.send(str_request_.encode('utf-8'), 0)
        # 读取头
        buf_header_ = self.__read_headers(ssl_sock_)
        str_header_ = buf_header_.decode('utf-8')

        # 判断是分块还是非分块
        # 读取块
        regexp = r'Content-Length: (\d*)\r\n'
        re_ = re.findall(regexp, str_header_, re.M)
        buf_body = b''
        if re_:
            print('非分包')
            len_body_ = int(re_[0], 10) # 取出第一个值转换为10进制
            buf_body += self.__read_block(ssl_sock_, len_body_)
            print('读取完毕')
        else:
            len_block_ = -1
            while len_block_ != 0:
                line_ = self.__read_line(ssl_sock_)
                len_block_ = int(line_[:-2].decode('utf-8'), 16)

                buf_body += self.__read_block(ssl_sock_, len_block_)
                self.__read_block(ssl_sock_, 2)     # 丢掉两个字节  就是丢掉最后空行
                print('分包读取完毕')



        ssl_sock_.close()
        sock_.close()

        # 解析数据
        json_content_ = json.loads(buf_body)

        if json_content_['errno'] == 0:
            # 过滤后打印得到的值
            s = ''
            a = 0
            for i in json_content_['data'][0]['v']:
                s += i
                if i == ';':
                    a += 1
                    if a == 4:
                        print(s)
                        a = 0
                        s = ''
            print(json_content_['data'][0]['v'][-11:])
            return json_content_['data'][0]['v']
        else:
            return '翻译错误'

    def __read_headers(self, sock): # 每读一次传入一个socket
        buf_header =b''
        while True:
            buf = sock.recv(1, 0)
            buf_header += buf
            # 取buf_header最后4个字节
            last_four_byte = buf_header[-4:]
            if last_four_byte == b'\r\n\r\n':
                print('响应头读取完毕')
                break
        return buf_header


    def __read_line(self, sock):    # 每读一次传入一个socket
        buffer = b''
        while True:
            buf = sock.recv(1, 0)
            buffer += buf
            last_two_bytes = buffer[-2:]
            if last_two_bytes == b"\r\n":
                break
        return buffer

    def __read_block(self, sock, size): # 读取的大小 size
        buffer = b''
        size_ = size
        while size_ != 0:
            buf = sock.recv(size_, 0)
            buffer += buf
            # 计算剩余的字节
            size_ -= len(buf)
        return buffer