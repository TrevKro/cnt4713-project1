#!/usr/bin/env python3
class ClientData:
    def __init__(self, addr):
        self.addr = addr
        self.inb = b'' # input buffer
        self.outb = b'' # output buffer

def acceptConnection(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print('accepted connection from', addr)
    conn.setblocking(False)
    data = ClientData(addr)
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)

def serviceConnection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data:
            data.outb += recv_data
        else:
            print('closing connection to', data.addr)
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print('echoing', repr(data.outb), 'to', data.addr)
            sent = sock.send(data.outb)  # Should be ready to write
            data.outb = data.outb[sent:]
import sys
import socket
import selectors
host = '0.0.0.0'
port = sys.argv[1]
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(sock)
if int(port) < 0 and int(port) < 65535:
    sys.stderr.write("ERROR: port number is out off range 0-65535\n")
    exit(1)
else:   
    sock.bind((host, int(port)))
    sock.listen(10)
    sock.setblocking(False)
    sel = selectors.DefaultSelector()
    sel.register(sock, selectors.EVENT_READ, data=None)
    print('listening on', sock.getsockname())
while True:
    events = sel.select(timeout=None)
    for key, mask in events:
        if key.data is None:
            acceptConnection(key.fileobj)
        else:
            serviceConnection(key, mask)
    sock.send("accio")
    if sock.recv(1024) == b'confirm-accio\r\n':
        sock.send("accio")
        if sock.recv(1024) == b'confirm-accio\r\n\r\n':
            clientSocket, clientAddress = sock.accept()
            print("Accepted connection from", clientAddress)
            sock.setblocking(False)
            data = clientSocket.recv(1024)
            if data:
                print("received bytes:", len(data))
                len = clientSocket.send(data)
                print("send bytes: %d" % len)
            sock.close()
        else:
            exit(1)
    else:
        exit(1)
