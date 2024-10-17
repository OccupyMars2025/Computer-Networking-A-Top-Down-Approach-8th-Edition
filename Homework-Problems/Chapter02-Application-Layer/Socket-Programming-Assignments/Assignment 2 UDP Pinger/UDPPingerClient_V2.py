import time
import socket

# Create a UDP socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set a timeout of 1 second
clientSocket.settimeout(1)

# Define the server address and port
serverAddress = ('localhost', 12000)

# Initialize variables for RTT statistics
rtt_list = []
num_lost_packets = 0
total_packets = 10

# Ping 10 times
for sequence_number in range(1, total_packets + 1):
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
        rtt_list.append(rtt)

        # Print the server response and RTT
        print(f"Reply from {server}:\n{response.decode()}\nRTT = {rtt:.6f} seconds\n\n")

    except socket.timeout:
        # If no response is received, print request timeout and increment lost packets
        print("Request timed out")
        num_lost_packets += 1

# Close the socket
clientSocket.close()

# Calculate and print RTT statistics
if rtt_list:
    min_rtt = min(rtt_list)
    max_rtt = max(rtt_list)
    avg_rtt = sum(rtt_list) / len(rtt_list)
else:
    min_rtt = max_rtt = avg_rtt = None

# Calculate packet loss rate
packet_loss_rate = (num_lost_packets / total_packets) * 100

print("\n--- Ping statistics ---")
print(f"Packets: Sent = {total_packets}, Received = {total_packets - num_lost_packets}, Lost = {num_lost_packets} ({packet_loss_rate}% loss)")

if rtt_list:
    print(f"Minimum RTT = {min_rtt:.6f} seconds")
    print(f"Maximum RTT = {max_rtt:.6f} seconds")
    print(f"Average RTT = {avg_rtt:.6f} seconds")
