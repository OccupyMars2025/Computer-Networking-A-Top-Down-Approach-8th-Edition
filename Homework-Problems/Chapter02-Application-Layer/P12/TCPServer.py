""" 
P12, page 201
"""

import socket

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Get local machine name
    host = 'localhost'  # Use '0.0.0.0' to listen on all interfaces
    port = 12345  # Port to listen on (set this in the browser proxy settings)
    
    # Bind to the port
    server_socket.bind((host, port))
    
    # Start listening for incoming connections (backlog of 5 connections)
    server_socket.listen(5)
    
    print(f"Server listening on {host}:{port}...")
    
    while True:
        # Establish connection with client
        connection_socket, addr = server_socket.accept()
        print(f"Connection from {addr} established.")
        
        # Receive and print data from the client
        while True:
            data = connection_socket.recv(1024).decode('utf-8')  # Buffer size 1024 bytes
            if not data:
                break
            print(f"Received: {data.strip()}")
        
        # Close the client connection
        connection_socket.close()

if __name__ == "__main__":
    start_server()
