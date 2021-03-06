import socket
ip_addr = ('', 22222)

# 俗称 插座
sk = socket.socket(
    socket.AF_INET,     # IP格式(地址族)
    socket.SOCK_STREAM, # 数据格式 （字节流，数据报文，RAW原生数据内核数据格式：报文）
    socket.IPPROTO_TCP)  #数据内容（协议）

# 插在网卡上
sk.bind(ip_addr)

# 监听
sk.listen(2) # backlog同时连接最大并发数量这里写的2

# 接收
client_sk,(ip, post) = sk.accept()  # 等待接收


str_response = 'Http/1.1 200 ok\r\n'
str_response += 'Refresh:3; url=https://www.baidu.com'  # 停3秒
# str_response = 'Http/1.1 401 Unauthorized\r\n'
# str_response += 'WWW-Authenticate: Basic realm="louis!"\r\n'
# str_response += 'Connection: Keep-Alive\r\n'
# str_response += 'Keep-Alive: 115\r\n'
# str_response += '\r\n\r\n'


client_sk.send(str_response.encode('utf-8'), 0)
# while True:
#     buf = client_sk.recv(1024*4, 0)
#     if not buf:
#         break
#     print(buf.decode())
client_sk.close()
sk.close()



