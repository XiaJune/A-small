import http
import http.server


# HTTPServer封装了基本的socket细节：socket创建，绑定，监听，接收
server = http.server.HTTPServer(
    ('', 22222),
    RequestHandlerClass=http.server.SimpleHTTPRequestHandler,
    bind_and_activate=True)
print('启动服务器')
server.serve_forever()
# server,handle_request




