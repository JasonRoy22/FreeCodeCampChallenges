#!/usr/bin/python3

import socket

clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#host = '172.29.64.1'
host = socket.gethostname()

port = 444

clientsocket.connect(('172.29.64.1', port))

message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))

