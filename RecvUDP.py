#Receiving

import socket

MY_ADDR = "10.0.2.15"
PORT = 45600

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#WE Bind to the address

sock.bind((MY_ADDR, PORT))

#We can receive data

while True:
    data, addr = sock.recvfrom(2048)
    print("The receive message is ",data,"from",addr)