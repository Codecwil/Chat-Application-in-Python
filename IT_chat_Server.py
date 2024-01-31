##################### BY WILSON CHOUNDONG #############################

#This Python script is a kind of remote chat (Walkie Talkies) 
# that lets you communicate with a client on the same local host.

#######################################################################


#----------------------SERVER ----------------------------

# listen
# bind __> LOCAL HOST = 127.0.0.1, HOST_PORT = 32000

import socket

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
DATA_SIZE = 1024


s = socket.socket()
s.bind((HOST_IP, HOST_PORT))
s.listen()

print(f"Waiting for connection on {HOST_IP}, port {HOST_PORT}...")
connection_socket, client_address = s.accept()
print(f"Connection established {client_address}")



# DATA RECEIVED 
while True:
    
    send_message = input("you: ")
    connection_socket.sendall(send_message.encode())
    data_received = connection_socket.recv(DATA_SIZE)
    if not data_received:
        break
    print("Message : ", data_received.decode())



s.close()
connection_socket.close()