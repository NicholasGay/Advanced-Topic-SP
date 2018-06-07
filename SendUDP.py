# HOW TO SEND UDP PACKETS

import socket

IP_ADDR = '192.168.0.115'
PORT = 45600
MESSAGE = "HELLO"

#We Create the Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #creating a socket in the socket module

#if you want to broadcast data, we need permissions
sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)

#WE send the data
sock.sendto(MESSAGE,(IP_ADDR,PORT))