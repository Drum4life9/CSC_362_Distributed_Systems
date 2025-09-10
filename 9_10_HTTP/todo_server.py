import http.server
import socketserver
from pathlib import Path

PORT = 8000
addr = "0.0.0.0"


class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
	def do_GET(self):
		if self.path != "/todos":
			self.send_response(403)
			self.end_headers()
			self.wfile.write("403 Forbidden, use /todos for get".encode("utf8"))
			return
		contents = Path("todos.txt").read_text()
		if contents == "":
			contents = "(no tasks yet)"
		self.send_response(200)
		self.send_header("Content-type", "text/plain")
		self.end_headers()
		self.wfile.write(contents.encode("utf8"))
	
	def do_POST(self):
		if self.path != "/todos":
			self.send_response(403)
			self.end_headers()
			self.wfile.write("403 Forbidden, use /todos for get".encode("utf8"))
			return
		with open("todos.txt", "a") as f:
			dat = self.log_date_time_string()
			content_len = int(self.headers.get('Content-Length'))
			post_body = self.rfile.read(content_len)
			f.write(dat + " - " + post_body.decode("utf-8") + "\n")
			f.close()
		self.send_response(201, "Created")
		self.send_header("Content-type", "text/plain")
		self.end_headers()
		self.wfile.write("Your todo has been created".encode("utf8"))


if __name__ == '__main__':
	Handler = CustomHTTPRequestHandler
	
	with socketserver.TCPServer((addr, PORT), Handler) as httpd:
		print("serving at port", PORT)
		httpd.serve_forever()
