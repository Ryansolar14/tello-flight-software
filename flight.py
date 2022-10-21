#
# ----FLIGHT SOFTWARE FOR DJI TELLO EDU----
# 
# Author: Ryan Busch, ENR100 Garrett College, McHenry, Maryland, USA
# 
# Credits: @shannon-s, ryzerobotics.com
#

import sys
import time
import threading
import socket

host = ''
port = 9000
locaddr = (host,port)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = ('192.168.10.1', 8889)
sock.bind(locaddr)

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

try:
    start_cmd = 'command'
    sock.sendto(start_cmd.encode(encoding="utf-8"), tello_address)
    print('Command sent: ' + start_cmd)
    time.sleep(1)

    check_battery_level = 'battery?'
    battery_level = sock.sendto(check_battery_level.encode(encoding="utf-8"), tello_address)
    print('Command sent: ' + check_battery_level)
    print('The current battery level is: ' + str(battery_level) + '%')

except KeyboradInterrupt:
    print('\n..\n')
    sock.close()
    