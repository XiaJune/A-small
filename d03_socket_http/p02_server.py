import socket

ip_addr = ('127.0.0.1', 11112)
unix_addr = 'file.socket' # 这里是文件表示地址 windows可能不支持

# 创建套接字 socket                   # 报文方式 不用监听 不管对方收没收到
# sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM, 0)  # 使用本地文件实现socket连接

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)  # 使用本地文件实现socket连接
# 绑定地址  也可以不绑定就是（UDP）
sock.bind(ip_addr)    # 绑定的一个本地文件地址
# 监听（listen）

# 接收用户连接
# 为这个用户创建缓冲（客户代理）

# 从客户端缓冲里面读取数据
while True:
    buf = sock.recv(1024*1, 0)    # 设置数据长度
    if not buf:
        break
    print(buf.decode())