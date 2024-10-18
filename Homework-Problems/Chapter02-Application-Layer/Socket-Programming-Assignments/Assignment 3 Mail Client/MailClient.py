from socket import *
import ssl
import base64

# Email and password setup
email = "your_email@gmail.com"
password = "your password" # If you use Gmail, you need to generate an app-specific password.

recipient_email = "recipient@gmail.com"

message = "Subject: Test Email\r\n\r\nThis is a test email from the Python SMTP client.Today is 2030/1/1.\r\n"
endmsg = "\r\n.\r\n"

mailserver = ('smtp.gmail.com', 587)

# Create socket and establish a TCP connection
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.settimeout(20)  # Set timeout to 20 seconds

print("Connecting to server...")
clientSocket.connect(mailserver)
print("Connected to server !")

recv = clientSocket.recv(1024).decode()
print("Response after connecting:", recv)

if recv[:3] != '220':
    print('Error: 220 reply not received from server.')

# Send HELO command and check response
heloCommand = 'HELO Alice\r\n'
print(repr(heloCommand))
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('Error: 250 reply not received from server.')

# Start TLS
starttlsCommand = 'STARTTLS\r\n'
print(repr(starttlsCommand))
clientSocket.send(starttlsCommand.encode())
recv_tls = clientSocket.recv(1024).decode()
print(recv_tls)
if recv_tls[:3] != '220':
    print('Error: 220 reply not received from server after STARTTLS.')

# Secure the connection
context = ssl.create_default_context()
clientSocket = context.wrap_socket(clientSocket, server_hostname='smtp.gmail.com')

# AUTH LOGIN (for Gmail authentication)
authCommand = 'AUTH LOGIN\r\n'
print(repr(authCommand))
clientSocket.send(authCommand.encode())
recv_auth = clientSocket.recv(1024).decode()
print(recv_auth)

# Send the base64-encoded username and password
base64_email = base64.b64encode(email.encode()) + b'\r\n'
print(email, " is encoded as ", base64_email)
clientSocket.send(base64_email)
recv_auth = clientSocket.recv(1024).decode()
print(recv_auth)

base64_password = base64.b64encode(password.encode()) + b'\r\n'
print(password, " is encoded as ", base64_password)
clientSocket.send(base64_password)
recv_auth = clientSocket.recv(1024).decode()
print(recv_auth)
if recv_auth[:3] != '235':  # 235 means successful authentication
    print("Authentication failed!")
    clientSocket.close()
    exit()

# Send MAIL FROM command
# Caution: you need "<>", and there is no space between ":" and "<"
mailFrom = f"MAIL FROM:<{email}>\r\n"
print(repr(mailFrom))
clientSocket.send(mailFrom.encode())
recv_mail = clientSocket.recv(1024).decode()
print(recv_mail)
if recv_mail[:3] != '250':
    print('Error: 250 reply not received from server.')

# Send RCPT TO command
rcptTo = f"RCPT TO:<{recipient_email}>\r\n"
print(repr(rcptTo))
clientSocket.send(rcptTo.encode())
recv_rcpt = clientSocket.recv(1024).decode()
print(recv_rcpt)
if recv_rcpt[:3] != '250':
    print('Error: 250 reply not received from server.')

# Send DATA command
dataCommand = 'DATA\r\n'
print(repr(dataCommand))
clientSocket.send(dataCommand.encode())
recv_data = clientSocket.recv(1024).decode()
print(recv_data)
if recv_data[:3] != '354':  # 354 means ready to receive message
    print('Error: 354 reply not received from server.')

# Send the message and the end of message marker
print(repr(message))
clientSocket.send(message.encode())
print(repr(endmsg))
clientSocket.send(endmsg.encode())  # Send end of message indicator
recv_msg = clientSocket.recv(1024).decode()
print(recv_msg)
if recv_msg[:3] != '250':
    print('Error: 250 reply not received from server.')

# Send QUIT command
quitCommand = 'QUIT\r\n'
print(repr(quitCommand))
clientSocket.send(quitCommand.encode())
recv_quit = clientSocket.recv(1024).decode()
print(recv_quit)
if recv_quit[:3] != '221':
    print('Error: 221 reply not received from server.')

# Close the connection
clientSocket.close()
