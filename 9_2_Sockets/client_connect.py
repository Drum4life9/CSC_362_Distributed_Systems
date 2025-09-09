import socket
import json

class MyClientSocket:
	def __init__(self, sock=None, MSGLEN=10):
		self.MSGLEN = MSGLEN
		if sock is None:
			self.sock = socket.socket(
				socket.AF_INET, socket.SOCK_STREAM)
		else:
			self.sock = sock
	
	def connect(self, host, port):
		self.sock.connect((host, port))
	
	def mysend(self, msg):
		if len(msg) > self.MSGLEN:
			self.sock.sendall(msg[:self.MSGLEN].encode())
		else:
			self.sock.sendall(msg.encode())
		
		
if __name__ == '__main__':
	clientSock = MyClientSocket(MSGLEN=100)
	
	clientSock.connect("0.0.0.0", 50000)
	
	is_int = input("Enter 1 to send an integer and 2 to send a message: ")
	
	if is_int == "2":
		inp = input("Enter a message to send to server: ")
		data = {
			"type": "str",
			"data": inp
		}
		send_data = json.dumps(data)
	else:
		inp = int(input("Enter an int to send to server: "))
		data = {
			"type": "int",
			"data": inp
		}
		send_data = json.dumps(data)
	
	clientSock.mysend(send_data)