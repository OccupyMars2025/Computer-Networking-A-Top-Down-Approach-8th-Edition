""" 
Enter the following in your browser:
http://localhost:8888/www.baidu.com

TODO: the code is not working. remain to be fixed
"""
from socket import * 
import sys 
import re

# Global variable to store the last requested host
last_host = None

if len(sys.argv) <= 1: 
    print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server') 
    sys.exit(2) 

# Create a server socket, bind it to a port and start listening 
tcpSerSock = socket(AF_INET, SOCK_STREAM) 
tcpSerSock.bind(('', 8888))  # Bind to port 8888
tcpSerSock.listen(5)  # Allow up to 5 simultaneous connections

def follow_redirects(headers):
    """Check if the response is a redirection and follow it."""
    if "302" in headers.split('\r\n')[0]:
        # Find the Location header and extract the URL
        match = re.search(r'Location: (.*)', headers)
        if match:
            return match.group(1).strip()
    return None

while 1: 
    try:
        # Start receiving data from the client 
        print('Ready to serve...') 
        tcpCliSock, addr = tcpSerSock.accept() 
        print('Received a connection from:', addr) 
        message = tcpCliSock.recv(1024).decode()  # Receiving data from the client
        print(message) 

        # Extract the filename from the given message (HTTP request)
        try:
            first_line = message.split('\n')[0]  # First line of the request (e.g., GET /www.google.com HTTP/1.1)
            print(first_line)
            url = first_line.split()[1]  # Extract the URL part (the second part of the first line)
            print(url)
            filename = url.partition("/")[2]  # Get everything after the first "/"
            print(filename) 
            fileExist = "false" 
            filetouse = "/" + filename 
            print(filetouse)

            # Declare global before assignment
            global last_host 

            # If the request is for favicon.ico, use the last host
            if "favicon.ico" in filename:
                if last_host is None:
                    print("No previous host to fetch favicon from.")
                    tcpCliSock.close()
                    continue
                hostn = last_host
            else:
                hostn = filename.replace("www.","",1)  # Set the host for normal requests
                last_host = hostn  # Cache this host for future favicon.ico requests
                print(hostn)

            # Check if the file exists in the cache
            try: 
                f = open(filetouse[1:], "r")                       
                outputdata = f.readlines()                         
                fileExist = "true" 

                # ProxyServer finds a cache hit and generates a response message 
                tcpCliSock.send("HTTP/1.0 200 OK\r\n".encode())             
                tcpCliSock.send("Content-Type:text/html\r\n".encode()) 

                # Send cached file to the client
                for i in range(0, len(outputdata)):  
                    tcpCliSock.send(outputdata[i].encode())
                print('Read from cache')    

            # File not found in the cache
            except IOError: 
                if fileExist == "false":  
                    # Create a socket on the proxy server 
                    c = socket(AF_INET, SOCK_STREAM)
                    
                    # Set a timeout for the connection attempt (in seconds)
                    c.settimeout(10)  
                    print(hostn)

                    try: 
                        # Connect to the socket to port 80 
                        c.connect((hostn, 80)) 

                        # Send the GET request with additional headers
                        request = ("GET / HTTP/1.1\r\n" +
                                   "Host: " + hostn + "\r\n" +
                                   "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36\r\n" +
                                   "Accept-Encoding: gzip, deflate\r\n" +
                                   "Connection: close\r\n\r\n")
                        
                        print("Request to origin server:\n", request)  # Debugging: Print the request
                        c.sendall(request.encode())  # Send the GET request to the server
                        
                        # Read the response headers
                        response = b""
                        buffer = c.recv(4096)  # Receive the response (4096 bytes at a time)
                        response += buffer
                        headers = response.decode().split('\r\n\r\n')[0]
                        print("Received headers:\n", headers)
                        
                        # Check for redirects (302 status)
                        redirect_url = follow_redirects(headers)
                        if redirect_url:
                            print("Redirecting to:", redirect_url)
                            if redirect_url.startswith("https://"):
                                print("Cannot handle HTTPS redirects, closing connection.")
                                tcpCliSock.close()
                                continue
                            else:
                                # Extract host and path from redirect URL
                                hostn = redirect_url.replace("http://", "").split("/")[0]
                                path = "/" + "/".join(redirect_url.split("/")[1:])
                                request = ("GET " + path + " HTTP/1.1\r\n" +
                                           "Host: " + hostn + "\r\n" +
                                           "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36\r\n" +
                                           "Accept-Encoding: gzip, deflate\r\n" +
                                           "Connection: close\r\n\r\n")
                                print("Sending redirect request to:", hostn)
                                c = socket(AF_INET, SOCK_STREAM)
                                c.connect((hostn, 80))
                                c.sendall(request.encode())
                                response = c.recv(4096)
                        else:
                            print("No redirection, processing response...")

                        # Cache the final response if no further redirects
                        tmpFile = open("./" + filename, "wb")
                        while len(buffer) > 0:
                            tmpFile.write(buffer)  # Write the buffer to cache
                            tcpCliSock.send(buffer)  # Send the buffer to the client
                            buffer = c.recv(4096)  # Receive the next chunk of data

                    except Exception as e: 
                        print("Illegal request:", e)

                else: 
                    # HTTP response message for file not found 
                    tcpCliSock.send("HTTP/1.0 404 Not Found\r\n".encode())
                    tcpCliSock.send("Content-Type:text/html\r\n".encode())
                    tcpCliSock.send("\r\n".encode())

        except IndexError as e:
            print("Error processing request:", e)

    except Exception as e:
        print("Error:", e)

    # Close the client and the server sockets     
    tcpCliSock.close()  
