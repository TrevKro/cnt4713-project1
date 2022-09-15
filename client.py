#!/usr/bin/env python3

import sys
import socket

host = sys.argv[1]
port = sys.argv[2]
fileName = sys.argv[3]
bufferSize = 4096 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


if int(port) > 0 and int(port) > 65535:
    print("ERROR: port number is out off range 0-65535")
else:
    print("Connecting to "+ str(host) + ":" + str(port))
    sock.connect((host, int(port)))
    print("Connected.")
    f = open(fileName,'rb')
    print("file opened")
    data = f.read()
    sock.sendfile(f)
    print("file sent. Closing connection")
    f.close()
    sock.close()