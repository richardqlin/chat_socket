# chat_socket

import socket
import threading

import sys


class Server:
    # set up a socket instance and passed it two parameters.
    # the first parameter is AF_INET and the second one is SOCK_STREAM referes to
    # the address family ipv4. The SOCK_STREAM means connection oriented TCP protocal.
    # using this socket to connect a server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # create an empty connections list of multiple connections
    connections = []
    # connect to a server with host and port
    def __init__(self):
        # assign an empty string server host such as '', assign anything to port, case it is 9000
        host , port = '',9000
        # bind to host and port
        self.s.bind((host,port))
        # it makes the server listen to requests coming from other computer on the network
        self.s.listen(3)
    
    def handler(self,c,a):
        while 1:
            # receive from client
            data = c.recv(1024)
            # iterater connections list and send data to clients
            for conn in self.connections:
                conn.send(data)
            if not data:
                break
    def run(self):
        while 1:
            # build connection with client and receive a new connection through server socket
            c, a = self.s.accept()
            
            cT = threading.Thread(target = self.handler,args= (c, a))
            cT.daemon = True
            cT.start()
            # add the a connection into the connections list
            self.connections.append(c)
            print(self.connections)


class Client:
    # using this socket to connect a client
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def sendMsg(self):
        
        self.s.send(bytes(input(''),'utf-8'))
        
    def __init__(self, address):
        self.s.connect((address,9000))
        iT = threading.Thread(target = self.sendMsg)
        iT.daemon = True
        iT.start()

        while 1:
            data = self.s.recv(1024).decode('utf-8')
            iT = threading.Thread(target = self.sendMsg)
            iT.daemon = True
            iT.start()
            if not data:
                break
            print(data)
                    

                     
        

if len(sys.argv)>1:
    client = Client(sys.argv[1])
else:
    server = Server()
    server.run()
