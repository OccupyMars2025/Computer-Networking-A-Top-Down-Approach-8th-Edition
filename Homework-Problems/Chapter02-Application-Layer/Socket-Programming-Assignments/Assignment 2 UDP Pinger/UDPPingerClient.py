import time
import socket

# Create a UDP socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set a timeout of 1 second
clientSocket.settimeout(1)

# Define the server address and port
serverAddress = ('localhost', 12000)

# Ping 10 times
for sequence_number in range(1, 11):
    # Prepare the ping message
    message = f"Ping {sequence_number} {time.time()}"

    try:
        # Send the message
        start_time = time.time()
        clientSocket.sendto(message.encode(), serverAddress)

        # Receive the response from the server
        response, server = clientSocket.recvfrom(1024)
        end_time = time.time()

        # Calculate the round trip time (RTT)
        rtt = end_time - start_time

        # Print the server response and RTT
        print(f"Reply from {server}:\n{response.decode()}\nRTT = {rtt:.6f} seconds")

    except socket.timeout:
        # If no response is received, print request timeout
        print("Request timed out")

# Close the socket
clientSocket.close()
