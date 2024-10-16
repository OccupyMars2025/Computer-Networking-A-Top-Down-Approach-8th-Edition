import socket

# TCP Server setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = '127.0.0.1'  # localhost
server_port = 8080  # Server listens on this port

server_socket.bind((server_host, server_port))
server_socket.listen(1)  # Listen for incoming connections
print(f"Server is listening on {server_host}:{server_port}")

while True:
    conn, addr = server_socket.accept()  # Accept incoming connection
    print(f"Connected by {addr}")
    
    data = conn.recv(1024)  # Receive data from the client
    if not data:
        break
    
    print(f"Received data: {data.decode('utf-8')}")
    conn.sendall(b"Message received by server!")  # Send response to client
    conn.close()
