import sys
import socket
host = '0.0.0.0'
port = sys.argv[1]
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(sock)
if int(port) < 0 and int(port) < 65535:
    sys.stderr.write("ERROR: port number is out off range 0-65535\n")
    exit(1)
else:   
    sock.bind((host, int(port)))
    sock.listen(1)
    print("await connections...")
    
    sock.send("accio")
    if sock.recv(1024) == b'confirm-accio\r\n':
        sock.send("accio")
        if sock.recv(1024) == b'confirm-accio\r\n\r\n':
            conn, addr = sock.accept()
            print("Accepted connection from", addr)
            sock.setblocking(False)
            data = conn.recv(1024)
            if data:
                print("received bytes:", len(data))
                len = conn.send(data)
                print("send bytes: %d" % len)
            sock.close()
        else:
            exit(1)
    else:
        exit(1)
