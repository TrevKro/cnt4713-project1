#!/usr/bin/env python3

import sys
import socket

IP = sys.argv[1:]
PORT = sys.argv[2:]
FILE = sys.argv [3:]
SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print(sock)

sock.bind((IP, PORT))
print(sock)

sock.listen(1)
clientSocket, clientAddress = sock.accept()


print("Accepted Connection form", clientAddress)

data = clientSocket.recv(SIZE)
if data:
    print("Received bytes:", len(data))
    l = clientSocket.send(data)
    print("Send bytes: %d" % l)

clientSocket.close()
sock.close()


#if __name__ == '__main__':
#    sys.stderr.write("client is not implemented yet\n")
