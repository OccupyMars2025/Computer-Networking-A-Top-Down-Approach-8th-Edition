""" 
open a browser, enter http://127.0.0.1:6789/HelloWorld.html

"""

#import socket module 
from socket import * 
import sys  # In order to terminate the program 

serverSocket = socket(AF_INET, SOCK_STREAM) 

# Prepare a server socket
# Fill in start
serverSocket.bind(('', 6789))  # Bind the server to port 6789 (you can use any available port)
serverSocket.listen(1)  # The server can only handle one connection at a time
# Fill in end

while True: 
    # Establish the connection
    print('Ready to serve...') 
    connectionSocket, addr = serverSocket.accept()  # Fill in start
                                                    # Fill in end 
    print('Connected from: ', addr)                                                          

    try: 
        message = connectionSocket.recv(1024).decode()  # Fill in start
                                                       # Fill in end                
        print("Message from client: ")
        print(10*"*", " start ", 10*"*")
        print(message)
        print(10*"*", " end ", 10*"*")
        print(message.split())
        
        filename = message.split()[1]    # '/HelloWorld.html'            
        f = open(filename[1:])  # Open the file requested by the client                         
        outputdata = f.read()  # Fill in start
                               # Fill in end    
        print("File content is:\n", repr(outputdata), "\n")                                      

        # # Send one HTTP header line into socket 
        # # Fill in start 
        # connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())  
        # # Fill in end           
        
        # Send the HTTP response header
        connectionSocket.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n".encode())  # Specify content type
      

        # # Send the content of the requested file to the client 
        # for i in range(0, len(outputdata)):     
        #     # print(repr(outputdata[i]))      
        #     connectionSocket.send(outputdata[i].encode()) 
            
        connectionSocket.sendall(outputdata.encode())

        connectionSocket.send("\r\n".encode()) 
        connectionSocket.close() 

    except IOError: 
        # Send response message for file not found 
        # Fill in start 
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())  
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>\r\n".encode())  
        # Fill in end 

        # Close client socket 
        # Fill in start 
        connectionSocket.close()
        # Fill in end             

serverSocket.close() 
sys.exit()  # Terminate the program after sending the corresponding data
