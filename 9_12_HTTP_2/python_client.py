import http.client

PORT = 8000
addr = "0.0.0.0"

if __name__ == '__main__':

	while True:
		client_1 = http.client.HTTPConnection(addr, PORT)
		
		inp = input("Type 1 for GET, 2 for POST, 3 for DELETE, 4 for close: ")
		if inp == "4":
			break
		elif inp == "3":
			client_1.request("DELETE", "/")
		elif inp == "2":
			msg = input("Type log to send: ")
			client_1.request("POST", "/", msg)
		elif inp == "1":
			client_1.request("GET", "/")
			resp = client_1.getresponse()
			print(resp.read().decode("utf-8"))
		else:
			break
		client_1.close()