import time
from socket import *

# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind the socket to the server address
serverSocket.bind(('', 12000))

timeout_period = 3  # Time in seconds to assume the client has stopped if no heartbeat is received

# Dictionary to store the last heartbeat time for each client
client_last_heartbeat = {}

print("UDP Heartbeat server is running...")

while True:
    try:
        # Receive the heartbeat packet from the client
        message, client_address = serverSocket.recvfrom(1024)
        current_time = time.time()

        # Extract the sequence number and the timestamp from the message
        decoded_message = message.decode()
        print(f"Received heartbeat: {decoded_message} from {client_address}")
        client_last_heartbeat[client_address] = current_time  # Update the last heartbeat time

        # Check for missing heartbeats (client timeout)
        # Caution: list() is not redundant, or you will get the error: Error: dictionary changed size during iteration
        for client, last_heartbeat_time in list(client_last_heartbeat.items()):
            if current_time - last_heartbeat_time > timeout_period:
                print(f"Client {client} is assumed to have stopped.")
                del client_last_heartbeat[client]

    except Exception as e:
        print(f"Error: {str(e)}")
