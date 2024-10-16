""" 
python client.py 127.0.0.1 6789 HelloWorld.html


"""


import sys
from socket import *

# Check if the user provided the correct number of arguments
if len(sys.argv) != 4:
    print("Usage: client.py server_host server_port filename")
    sys.exit()

# Get command-line arguments
server_host = sys.argv[1]
server_port = int(sys.argv[2])
filename = sys.argv[3]

# Create a TCP client socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect to the server
clientSocket.connect((server_host, server_port))

# Send an HTTP GET request to the server
request = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}\r\n\r\n"
clientSocket.send(request.encode())

# # Receive the server's response
# response = clientSocket.recv(1024)

# Receive the server's response
response = b""
while True:
    data = clientSocket.recv(1024)
    if not data:
        break
    response += data

# Print the server's response (header + content)
print("the server's response:")
print(10*"*", " start ", 10*"*")    
print(response.decode())
print(10*"*", " end ", 10*"*")

# Close the connection
clientSocket.close()
