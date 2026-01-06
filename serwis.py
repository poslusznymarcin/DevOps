import http.server
import socketserver
import json

PORT = 8080

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Ustawiamy nagłówek, że wysyłamy JSON
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        # Treść odpowiedzi (JSON)
        response = {"id": 1, "content": "Hello, DevOps World!"}
        self.wfile.write(bytes(json.dumps(response), "utf8"))

# Uruchomienie serwera
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serwis REST dziala na porcie {PORT}")
    httpd.serve_forever()
