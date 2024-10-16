#import socket module
from socket import *
import sys  # For terminating the program
import threading  # For handling multiple requests concurrently

# Function to handle each client request in a separate thread
def handle_client(connectionSocket):
    try:
        message = connectionSocket.recv(1024).decode()
        print("Received message:")
        print(10*"-", " start ", "-"*10)
        print(message)
        print(10*"-", " end ", "-"*10)
        try:
            filename = message.split()[1]
            f = open(filename[1:])  # Open the requested file
            outputdata = f.read()
            print("the content of the requested file :\n", repr(outputdata))

            # # Send HTTP response header
            # connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

            # Send the HTTP response header
            connectionSocket.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n".encode())  # Specify content type
      
            # # Send the content of the requested file to the client
            # for i in range(0, len(outputdata)):
            #     connectionSocket.send(outputdata[i].encode())
                
            # Send the content of the requested file to the client at once (instead of byte-by-byte)
            connectionSocket.sendall(outputdata.encode())
            
            connectionSocket.send("\r\n".encode())
        except IOError:
            # Send 404 Not Found response if the file is not found
            connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
            connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>\r\n".encode())
    except ConnectionResetError:
        print("Client closed the connection prematurely.")
    finally:
        # Close the client connection socket
        connectionSocket.close()
        print("Closing connection")


# Main server function
def start_server():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Bind the socket to a port
    serverSocket.bind(('', 6789))  # Use any available port, like 6789
    serverSocket.listen(5)  # Allow the server to accept multiple connections
    print('Ready to serve...')

    while True:
        # Accept new client connections
        connectionSocket, addr = serverSocket.accept()
        print('Got a connection from', addr)
        
        # Create a new thread for each client connection
        client_thread = threading.Thread(target=handle_client, args=(connectionSocket,))
        client_thread.start()  # Start the new thread to handle the client request

    serverSocket.close()
    sys.exit()  # Terminate the program when done

if __name__ == "__main__":
    start_server()
