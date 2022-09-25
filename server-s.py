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
    sock.bind(("0.0.0.0", int(port)))
    sock.listen(10)
    clientSocket, clientAddress = sock.accept()
    print("Accepted connection from", clientAddress)
    sock.setblocking(False)
    sock.send("accio")
    if sock.recv(1024) == b'confirm-accio\r\n':
        sock.send("accio")
        if sock.recv(1024) == b'confirm-accio\r\n\r\n':

            data = clientSocket.recv(1024)
            if data:
                print("received bytes:", len(data))
                len = clientSocket.send(data)
                print("send bytes: %d" % len)
            sock.close()
        else:
            sys.exit()
    else:
        sys.exit()