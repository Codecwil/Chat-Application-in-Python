# Chat-Application-in-Python
In this blog post, we'll explore a simple Python project that simulates a walkie-talkie chat application using sockets. The project consists of two scripts: IT_chat_Server.py and IT_chat_Client.py. These scripts allow communication between a server and a client on the same local host.

Server Script - IT_chat_Server.py
Pupose
The IT_chat_Server.py script serves as the server side of the chat application.

Initialization
The server script initializes a socket, binds it to the local host 127.0.0.1 and a specified port 32000, and starts listening for incoming connections.



    import  socket 
     
    
    HOST_IP = "127.0.0.1"
    HOST_PORT = 32000
    DATA_SIZE = 1024

    s = socket.socket()
    s.bind((HOST_IP, HOST_PORT))
    s.listen()
                          
    

Connection Establishment
Once a connection is established, the server enters a loop where it continuously sends and receives messages.
connection_socket, client_address = s.accept()
                        print(f"Connection established {client_address}")
                         


Message Communication

The server prompts the user for a message, sends it to the client, receives a response, and prints the received message.


    while True:
    send_message = input("you: ")
    connection_socket.sendall(send_message.encode())
    data_received = connection_socket.recv(DATA_SIZE)
    if not data_received:
        break
    print("Message: ", data_received.decode())
    

    
Cleanup

Finally, the server script closes the sockets.

    s.close()
    connection_socket.close()
    
Client Script - IT_chat_Client.py
Purpose
The IT_chat_Client.py script serves as the client side of the chat application.
Initialization
The client script initializes a socket and attempts to connect to the server. If the connection is refused, it retries after a short delay.

    import socket
    import time

    HOST_IP = "127.0.0.1"
    HOST_PORT = 32000
    DATA_SIZE = 1024

    s = socket.socket()

  
Connection Establishment
Once connected, the client enters a loop where it continuously receives messages from the server and sends user-input messages.
    while True:
        try:
            s.connect((HOST_IP, HOST_PORT))
        except ConnectionRefusedError:
            print(f"ERROR: unable to connect to server. Reconnection...")
            time.sleep(5)
        else:
            print(f"Server Connected")
            break;

    while True:
        data_received = s.recv(DATA_SIZE)
        if not data_received:
            break
        print("Message: ", data_received.decode())
        send_message = input("you: ")
        s.sendall(send_message.encode())

        
    

Cleanup


Finally, the client script closes the socket
    s.close()
    

Wilson Choundong
Conclusion

This project provides a basic understanding of socket communication in Python and serves as a foundation for more complex networking applications. Feel free to modify and extend the code to experiment with additional features and improvements. Happy coding!
