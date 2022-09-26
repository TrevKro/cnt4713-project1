#!/usr/bin/env python3

import sys
import socket

host = socket.gethostbyname(sys.argv[1])
port = sys.argv[2]
fileName = sys.argv[3]
bufferSize = 4096 
if int(port) < 0 and int(port) < 65535:
    sys.stderr.write("ERROR: port number is out off range 0-65535\n")
    exit(1)
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
            sock.settimeout(10)
            sock.send(b'confirm-accio\r\n')
            sock.settimeout(10)
            sock.send(b'confirm-accio\r\n\r\n')
            print(sock.recv(1024)) == b'accio\r\n'
            file = open(fileName,'rb')
            sendData = file.read(1024)
            print("trying to send file")
            while sendData:
                
                sock.send(sendData)
                SendData = file.read(1024)
            file.close()
            sock.close()
            
    except socket.timeout as msg:
        sys.stderr.write("ERROR: Failed to connect\n")
        exit(1)

    except socket.error as msg:
        sys.stderr.write("ERROR: Failed\n")
        exit(1)