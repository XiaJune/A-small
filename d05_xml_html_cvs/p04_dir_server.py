import http
import http.server
import os

class FileHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):           # 接收数据的所内容
        print(self.client_address)
        print(self.server)
        print(self.headers)
        print(self.command)
        print(self.path)
        self.send_response(200) # 发送响应头状态码
        self.send_header('Content-Type', 'text/html;charset=utf-8') # 响应头
        self.end_headers()  # 空行
        self.wfile.write('<!doctype html>'.encode('utf-8'))
        self.wfile.write('<html>'.encode('utf-8'))
        self.wfile.write('<body>'.encode('utf-8'))

        files = os.listdir('.')
        print(files)
        for file in files:
            self.wfile.write(F'<a href="http://127.0.0.1:22222/">{file}</a><hr>'.encode('utf-8'))

        self.wfile.write('</body>'.encode('utf-8'))
        self.wfile.write('</html>'.encode('utf-8'))



    def do_POST(self):      # 发送数据
        pass

    def do_INPUT(self):
        pass

server = http.server.HTTPServer(
    ('', 22222),
    RequestHandlerClass=FileHandler,
    bind_and_activate=True)
print('启动服务器')
server.serve_forever()