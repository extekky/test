from http.server import BaseHTTPRequestHandler, HTTPServer


HOST = "0.0.0.0"  # слушаем на всех интерфейсах, чтобы контейнер был доступен извне
PORT = 8080       # порт, на котором будет работать сервер


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200) # Отправляем статус 200 OK
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"Hello from Effective Mobile!")

    def log_message(self, format, *args):
        # Простой лог в stdout, чтобы было видно в docker logs
        print("%s - %s" % (self.address_string(), format % args))


if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), Handler)
    print(f"Server started on {HOST}:{PORT}")
    server.serve_forever()