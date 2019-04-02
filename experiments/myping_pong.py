import socketserver, socket, sys

host = "0.0.0.0"
port = 10000
address = (host, port)

class MyTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

class TCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        message = self.request.recv(10).strip()
        print(message)
        self.request.sendall(message.upper())

def serve():
    server = MyTCPServer(address, TCPHandler)
    server.serve_forever()

def ping():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)

    sock.sendall(input("?").encode())
    data = sock.recv(10)
    print("Received from server: {0}".format(data.decode()))
    
    
if __name__ == "__main__":
    command = sys.argv[1]
    if command == "serve":
        serve()
    elif command == "ping":
        ping()
    else:
        print("invalid command")
