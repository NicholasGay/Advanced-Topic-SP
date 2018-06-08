#FOR MMC

import socket

IP_ADDR = '129.187.223.200'
PORT = 3000
MESSAGE = "TEST"

MY_ADDR = "10.0.2.15"

#We Create the Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #creating a socket in the socket module

#if you want to broadcast data, we need permissions
sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)

#WE send the data
sock.sendto(MESSAGE,(IP_ADDR,PORT))

#WE Bind to the address

sock.bind((MY_ADDR, PORT))

#We can receive data

while True:
    data, addr = sock.recvfrom(3000)
    print("The receive message is ",data,"from",addr)