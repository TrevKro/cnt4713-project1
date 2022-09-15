#!/usr/bin/env python3

import sys
import socket

host = socket.gethostbyname(sys.argv[1])
port = sys.argv[2]
fileName = sys.argv[3]
bufferSize = 4096 
if int(port) > 0 and int(port) > 65535:
    sys.stderr.write("ERROR: port number is out off range 0-65535\n")
    sys.exit()
else:
    try:
        print("Connecting to "+ str(host) + ":" + str(port))
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            #print(sock)
            sock.settimeout(10)
            sock.connect((host, int(port)))
            #print(sock)
            #dataFromServer = sock.recv(1024)
            print("First Recieved: " + str(sock.recv(1024)))
            sock.send(b'confirm-accio\r\n')
            sock.send(b'confirm-accio\r\n\r\n')
            print("Second Recieved: " + str(sock.recv(1024)))
            f = open(fileName,'rb')
            print("file opened")
            data = f.read()
            sock.sendfile(f)
            print("file sent. Closing connection.")
            f.close()
            sock.close()
    except socket.timeout as msg:
        sys.stderr.write("ERROR: Failed to connect\n")
        sys.exit()
