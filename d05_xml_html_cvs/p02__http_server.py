import http.server
import http

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.client_address)



server = http.server.HTTPServer(
    ('', 22222),    # 服务器地址
    RequestHandlerClass=http.server.SimpleHTTPRequestHandler,   # 请求处理器
    bind_and_activate=True)     # 绑定激活 True
print('启动服务器')
server.serve_forever()
