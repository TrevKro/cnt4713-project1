#!/usr/bin/env python3

import sys
import socket
port = sys.argv[1]
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(sock)
if int(port) > 0 and int(port) > 65535:
    sys.stderr.write("ERROR: port number is out off range 0-65535\n")
    sys.exit()
else:    
    sock.bind(("0.0.0.0", port))
    sock.listen(1)
    clientSocket, clientAddress = sock.accept()
    print("Accepted connection from", clientAddress)
    data = clientSocket.recv(1024)
    if data:
        print("received bytes:", len(data))
        len = clientSocket.send(data)
        print("send bytes: %d" % len)

    clientSocket.close()
    sock.close()