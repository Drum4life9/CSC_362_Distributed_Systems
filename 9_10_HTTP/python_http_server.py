import http.server
import socketserver

PORT = 8001
addr = "0.0.0.0"

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200, "Hello There")
        self.end_headers()

if __name__ == '__main__':
    Handler = CustomHTTPRequestHandler
    
    with socketserver.TCPServer((addr, PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()
