from http.server import BaseHTTPRequestHandler, HTTPServer
import os


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("🔹 Получен GET-запрос:", self.path)

        # Статика (CSS, JS, иконки и т.п.)
        if self.path.startswith("/static/"):
            file_path = self.path[1:]  # убираем первый "/"
            try:
                with open(file_path, "rb") as file:
                    content = file.read()
                    if file_path.endswith(".css"):
                        self.send_response(200)
                        self.send_header("Content-type", "text/css")
                    elif file_path.endswith(".js"):
                        self.send_response(200)
                        self.send_header("Content-type", "application/javascript")
                    elif file_path.endswith(".ico"):
                        self.send_response(200)
                        self.send_header("Content-type", "image/x-icon")
                    else:
                        self.send_response(200)
                        self.send_header("Content-type", "application/octet-stream")
                    self.end_headers()
                    self.wfile.write(content)
            except FileNotFoundError:
                self.send_response(404)
                self.end_headers()
            return

        # Роутинг страниц
        routes = {
            "/": "index.html",
            "/catalog": "catalog.html",
            "/catalog/": "catalog.html",
            "/category": "category.html",
            "/category/": "category.html",
            "/contacts": "contacts.html",
            "/contacts/": "contacts.html",
        }

        file_name = routes.get(self.path)
        if file_name:
            try:
                with open(f"templates/{file_name}", encoding="utf-8") as file:
                    content = file.read()
                    self.send_response(200)
                    self.send_header("Content-type", "text/html; charset=utf-8")
                    self.end_headers()
                    self.wfile.write(content.encode("utf-8"))
            except FileNotFoundError:
                self.send_response(404)
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        print("🔸 Получен POST-запрос:", self.path)

        if self.path == "/contacts":
            content_length = int(self.headers.get("Content-Length", 0))
            post_data = self.rfile.read(content_length).decode("utf-8")
            print(" Сообщение из формы:", post_data)

            # Возврат той же страницы
            try:
                with open("templates/contacts.html", encoding="utf-8") as file:
                    content = file.read()
                    self.send_response(200)
                    self.send_header("Content-type", "text/html; charset=utf-8")
                    self.end_headers()
                    self.wfile.write(content.encode("utf-8"))
            except FileNotFoundError:
                self.send_response(404)
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()


def run():
    server_address = ("localhost", 8080)
    httpd = HTTPServer(server_address, MyHandler)
    print("Сервер запущен: http://localhost:8080")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
