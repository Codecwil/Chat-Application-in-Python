##################### BY WILSON CHOUNDONG #############################

#This Python script is a kind of remote chat (Walkie Talkies) 
# that lets you communicate with a client on the same local host.

#######################################################################

#----------------------CLIENT ----------------------------


# Accept 
# bind __> LOCAL HOST = 127.0.0.1, HOST_PORT = 32000

import socket
import time

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
DATA_SIZE = 1024


s = socket.socket()

print(f"Connection to {HOST_IP} serveur, port {HOST_PORT}")
while True:
    try:
        s.connect((HOST_IP, HOST_PORT))
    except ConnectionRefusedError:
        print(f"ERROR: unable to connect to server. Reconnection...")
        time.sleep(5)
    else:
        print(f"Server Connected")
        break;
    
# DATA RECEIVED 
while True:
    data_received = s.recv(DATA_SIZE)
    if not data_received:
        break
    print("Message : ", data_received.decode())
    send_message = input("you: ")
    s.sendall(send_message.encode())
    
   
    
s.close()