import http.client

PORT = 8001
addr = "0.0.0.0"

if __name__ == '__main__':
	client_1 = http.client.HTTPConnection(addr, PORT)
	client_1.request("GET", "/")
	resp = client_1.getresponse()
	print(resp.status, resp.reason)