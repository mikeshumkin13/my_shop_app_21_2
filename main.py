from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/static/"):
            file_path = self.path[1:]
            try:
                with open(file_path, "rb") as file:
                    content = file.read()
                    self.send_response(200)  # СНАЧАЛА код ответа
                    if file_path.endswith(".css"):
                        self.send_header("Content-type", "text/css")
                    elif file_path.endswith(".js"):
                        self.send_header("Content-type", "application/javascript")
                    else:
                        self.send_header("Content-type", "application/octet-stream")
                    self.end_headers()
                    self.wfile.write(content)
            except FileNotFoundError:
                self.send_error(404, "Файл не найден")
            return

        # Рендерим HTML-шаблон
        try:
            with open("templates/index.html", encoding="utf-8") as file:
                content = file.read()
        except FileNotFoundError:
            self.send_error(404, "Файл не найден")
            return

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(content.encode("utf-8"))

def run():
    server_address = ("localhost", 8080)
    httpd = HTTPServer(server_address, MyHandler)
    print("Сервер запущен: http://localhost:8080")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
