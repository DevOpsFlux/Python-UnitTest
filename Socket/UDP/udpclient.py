# -*- coding: utf-8 -*- 
'''
    UDP Client
'''
import socket


localIP     = "127.0.0.1"
localPort   = 20007

bufferSize  = 1024

msgFromClient       = "UnitTest UDP Server"
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = (localIP, localPort)

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

#msgFromServer = UDPClientSocket.recvfrom(bufferSize)
#msg = "Message from Server {}".format(msgFromServer[0])

msg = "Message OK"

print(msg)