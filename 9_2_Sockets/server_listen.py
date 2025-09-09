import socket
import json

class MyServerSocket:
    
    def __init__(self, sock=None, MSGLEN=None):
        self.MSGLEN = MSGLEN
        if sock is None:
            self.sock = socket.socket(
                            socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock
            
        self.sock.bind(('0.0.0.0', 50000))
        self.sock.listen(1)
        
        while True:
            conn, addr = self.sock.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    my_json = data.decode('utf8').replace("'", '"')
                    data = json.loads(my_json)
                    print(f'{data['data']} is of type {data['type']}')
                    return

    def awaitReceiveAndPrint(self):
        chunks = []
        bytes_recd = 0
        while bytes_recd < self.MSGLEN:
            chunk = self.sock.recv(min(self.MSGLEN - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)
    



if __name__ == '__main__':
    serverSock = MyServerSocket(MSGLEN=100)
