"""
page 186
"""

from socket import *

serverName = '127.0.0.1'  # Loopback address
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    message = input('Input lowercase sentence (type "exit" to quit): ')
    
    if message.lower() == 'exit':
        print("Closing connection.")
        break  # Exit the loop and close the connection
    
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(f"Modified message from server: {modifiedMessage.decode()}")

clientSocket.close()
