import socket
import ssl

# 构造一个ssl的上下文环境 Context
# ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
# #加载服务器证书和私钥
# ctx.load_cert_chain(        # 证书链  钥匙链
#     certfile='certs/server.crt',   # 服务器证书
#     keyfile='certs/server_rsa_private.pem', # 服务器私钥
#     password='server')      # 服务器密码
# # 创建socket
# sk = socket.socket(
#     socket.AF_INET,
#     socket.SOCK_STREAM,
#     socket.IPPROTO_TCP)
# # 包装socket
# w_sk = ctx.wrap_socket(sock=sk, server_side=True)
#
# # 开始通信
# w_sk.bind(('', 22222))   # 8443 ssl标准的默认端口 443 前面数字随便加
# w_sk.listen(2)
# print('等待客户连接')
# client, (ip, port) = w_sk.accept()
# print('连接：', ip, port)
# # 利用包装socket进行数据交换
# while True:
#     buf = client.recv(4*1024, 0)
#     if not buf:
#         break
#     print(buf.decode('utf-8'))
