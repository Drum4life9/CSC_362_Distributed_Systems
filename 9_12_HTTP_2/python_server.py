import http.server
import socketserver
from pathlib import Path

PORT = 8000
addr = "0.0.0.0"


class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
	def do_GET(self):
		contents = Path("logs.txt").read_text()
		if contents == "":
			contents = "No logs yet"
		self.send_response(200)
		self.send_header("Content-type", "text/plain")
		self.end_headers()
		self.wfile.write(contents.encode("utf8"))
	
	def do_POST(self):
		with open("logs.txt", "a") as f:
			dat = self.log_date_time_string()
			content_len = int(self.headers.get('Content-Length'))
			post_body = self.rfile.read(content_len)
			f.write(dat + " - " + post_body.decode("utf-8") + "\n")
			f.close()
		self.send_response(201, "Created")
		self.send_header("Content-type", "text/plain")
		self.end_headers()
	
	def do_DELETE(self):
		with open("logs.txt", "w") as f:
			f.seek(0)
			f.truncate()
		self.send_response(204, "No Content")
		self.end_headers()
		

if __name__ == '__main__':
	Handler = CustomHTTPRequestHandler
	
	with socketserver.TCPServer((addr, PORT), Handler) as httpd:
		print("serving at port", PORT)
		httpd.serve_forever()
