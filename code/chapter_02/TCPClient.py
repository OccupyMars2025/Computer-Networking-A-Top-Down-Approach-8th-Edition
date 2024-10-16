""" 
page 191
"""

from socket import *

serverName = '127.0.0.1'  # Loopback address
serverPort = 12000

while True:
    # Reconnect after each message: Since the server closes the connection after sending a response, the client needs to create a new connection for each message. This is handled by creating a new clientSocket in each iteration of the loop.
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    
    sentence = input('Input lowercase sentence (or type "exit" to quit): ')
    
    # If the user types 'exit', break the loop and close the connection
    if sentence.lower() == 'exit':
        print("Closing client.")
        clientSocket.close()
        break
    
    # Send the message to the server
    clientSocket.send(sentence.encode())

    # Receive the modified message from the server
    modifiedSentence = clientSocket.recv(1024)
    print('From Server: ', modifiedSentence.decode())
    
    # Close the client connection after receiving the response from the server
    clientSocket.close()
