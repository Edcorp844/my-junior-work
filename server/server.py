import socket
import threading
import sys

class server:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []
    def __init__(self):
        self.s.bind(('0.0.0.0', 3000))
        self.s.listen(1)
    
    def handler(self, conn, add):
        while True:
            data = conn.recv(1024)
            for conn in self.connections:
                conn.send(bytes(data))
            if not data:
                break

    def run(self):
        while True:
            conn, add = self.s.accept()
            sThread = threading.Thread(target = self.handler, args = (conn, add))
            sThread.daemon = True
            sThread.start()
            self.connections.append(conn)
            print(self.connections)

class client:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def sendMsg(self):
        self.s.send(bytes(input('', utf-8)))

    def __init__(self, address):
        self.s.connect((address, 3000))

        iThread = threading.Thread(target = self.sendMsg)
        iThread.daemon = True
        iThread.start()

        while True:
            data = self.s.recv(1024)
            if not data:
                break

if (len(sys.argv) > 1):
    client = client(sys.argv[1])
else:
    server = server()
    server.run()