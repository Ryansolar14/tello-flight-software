#
# ----FLIGHT SOFTWARE FOR DJI TELLO EDU----
# 
# Author: Ryan Busch, ENR100 Garrett College, McHenry, Maryland, USA
# 
# Credits: @shannon-s, ryzerobotics.com
#

#Import Libraries

import sys
import time
import threading
import socket

#Global Functions

def cmd(command):
    sock.sendto(command.encode(encoding="utf-8"), tello_address)
    print('Command sent: ' + command)

def getData(command, type, symbol):
    return_value = sock.sendto(command.encode(encoding="utf-8"), tello_address)
    print('Command sent: ' + command)
    print(type + ' is currently:' + str(return_value) + symbol)

#Global Variables
host = ''
port = 9000
locaddr = (host,port)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = ('192.168.10.1', 8889) #Tello IP address and port, should not change
sock.bind(locaddr)

# Create and start receiving thread
def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break

recvThread = threading.Thread(target=recv)
recvThread.start()

#Main Program
try:
    cmd('command') #Enter command mode
    getData('battery?', 'Battery Level', '%') #Get battery level

except KeyboardInterrupt:
    print('\n..\n')
    sock.close()


