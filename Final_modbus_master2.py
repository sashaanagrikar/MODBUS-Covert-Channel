#!/usr/bin/env python3
#Echo Server 
import socket 
import sys
HOST = "192.168.43.101"
PORT = 502 #listen port for Amazon Echo
#socket = (node)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT)) # Binding these to the above host and the port 

s.listen(5)

while True: 
	conn, addr = s.accept()
	x = conn.recv(1024)
#Untill(1024) for data reading, after will be closed or discard connection
        if (x == '12'):
         print ('A')
        elif (x == '13'):
         print ('B')
        elif (x == '14'):
         print ('C')
        elif (x == '15'):
         print ('D')
        elif (x == '16'):
         print ('E')
        elif (x == '17'):
         print ('F')
        elif (x == '18'):
         print ('G')
        elif (x == '19'):
         print ('H')
        elif (x == '22'):
         print ('I')
        elif (x == '23'):
         print ('J')
        elif (x == '24'):
         print ('K')
        elif (x == '25'):
         print ('L')
        elif (x == '26'):
         print ('M')
        elif (x == '27'):
         print ('N')
        elif (x == '28'):
         print ('O')
        elif (x == '32'):
         print ('P')
        elif (x == '33'):
         print ('Q')
        elif (x == '34'):
         print ('R')
        elif (x == '35'):
         print ('S')
        elif (x == '36'):
         print ('T')
        elif (x == '37'):
         print ('U')
        elif (x == '42'):
         print ('V')
        elif (x == '43'):
         print ('W')
        elif (x == '44'):
         print ('X')
        elif (x == '45'):
         print ('Y')
        elif (x == '46'):
         print ('Z')
        elif (x == '52'):
         print ('0')
        elif (x == '53'):
         print ('1')
        elif (x == '54'):
         print ('2')
        elif (x == '55'):
         print ('3')
        elif (x == '62'):
         print ('4')
        elif (x == '63'):
         print ('5')
        elif (x == '64'):
         print ('6')
        elif (x == '72'):
         print ('7')
        elif (x == '73'):
         print ('8')
        elif (x == '82'):
         print ('9')
        elif (x == '29'):
         print (' ')
        elif (x == '38'):
         print ('.')
        elif (x == '47'):
         print ('"')
