#!/usr/bin/env python3

import sys
import socket

host = sys.argv[1]
port = sys.argv[2]
fileName = sys.argv[3]
bufferSize = 4096 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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


# host = "131.94.128.43"
# port = 54634
# fileName = "file.txt"