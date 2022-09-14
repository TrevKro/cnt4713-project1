#!/usr/bin/env python3

import sys
import socket

Ip = sys.argv[1]
Port = sys.argv[2]
File = sys.argv[3]
Size = 1024

print(sys.argv)
print(Ip)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print(sock)

sock.bind((Ip, Port))
print(sock)

sock.listen(1)
clientSocket, clientAddress = sock.accept()


print("Accepted Connection form", clientAddress)

data = clientSocket.recv(Size)
if data:
    print("Received bytes:", len(data))
    l = clientSocket.send(data)
    print("Send bytes: %d" % l)

clientSocket.close()
sock.close()


#if __name__ == '__main__':
#    sys.stderr.write("client is not implemented yet\n")
