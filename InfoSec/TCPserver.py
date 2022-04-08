#1/usr/bin/python3

import socket

#Creating the socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = 'IPv4 Address = 172.29.64.1'
host = socket.gethostname()
port = 444

#Binding to socket
serversocket.bind(('172.29.64.1', port)) #Host will be repolaced/substituted with IP, if cahnged and not running on host

#Starting TCP listener
serversocket.listen(3)

while True:
    #Starting the connection
    clientsocket,address = serversocket.accept()

    print("Received Connection From: %s " % str(address))

    message = 'Hello! Thank you for connecting to the server. This is an example of how sockets can be used' + "\r\n"

    clientsocket.send(message.encode('ascii'))

    clientsocket.close()
