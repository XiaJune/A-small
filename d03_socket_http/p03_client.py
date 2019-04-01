import socket

ip_addr = ('127.0.0.1', 11112)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,0)  # 使用本地文件实现socket连接

socke = sock.sendto('hello'.encode(), ip_addr)