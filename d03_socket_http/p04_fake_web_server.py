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
print(ip, post)

while True:
    buf = client_sk.recv(4*1024)    # 缓冲大小 缓存
    if not buf:
        print('客户端退出')
        break
    print(buf.decode('utf-8'))

