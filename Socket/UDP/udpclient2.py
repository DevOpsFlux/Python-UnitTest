# -*- coding: utf-8 -*- 
'''
    UDP Client
'''
import os, sys, string
import json
import socket

def main() :

	UDP_IP_ADDRESS = "203.xx.xxx.xx"
	UDP_PORT_NO = 19309
	Message = "UnitTest, Server"

	clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	clientSock.sendto(Message, (UDP_IP_ADDRESS, UDP_PORT_NO))

#	while True:
#		data, addr = serverSock.recvfrom(1024)
#		print "Message: ", data

	msginfo = {
		'SDateTime' : '2019/03/21',
		'TotalCnt' : '1000',
		'ACnt' : '600',
		'BCnt' : '400'
	}

    #print(json.dumps(msginfo, ensure_ascii=False))
    
    
if __name__ == "__main__" :
    main()