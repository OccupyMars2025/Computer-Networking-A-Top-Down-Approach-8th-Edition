import socket

# TCP Client setup
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = '127.0.0.1'  # Server IP
server_port = 8081  # Port number that the server is listening to

try:
    client_socket.connect((server_host, server_port))  # Connect to the server
    client_socket.sendall(b"Hello, Server!")  # Send data to server
    
    response = client_socket.recv(1024)  # Receive response from server
    print(f"Received response from server: {response.decode('utf-8')}")
finally:
    client_socket.close()
