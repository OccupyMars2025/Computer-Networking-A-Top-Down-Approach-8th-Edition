import time
from socket import *

# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Define the server address and port
serverAddress = ('localhost', 12000)

# Set a timeout for the socket
clientSocket.settimeout(1)

# Send heartbeat every second
sequence_number = 1

try:
    while True:
        # Prepare the heartbeat message with a sequence number and current timestamp
        message = f"Heartbeat {sequence_number} {time.time()}"
        clientSocket.sendto(message.encode(), serverAddress)
        print(f"Sent: {message}")

        # Increment the sequence number for the next heartbeat
        sequence_number += 1
        time.sleep(1)  # Send heartbeat every second

except KeyboardInterrupt:
    print("Client stopped.")

finally:
    clientSocket.close()
