"""  
Updated SMTP Client with Text and Image Sending

"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email import encoders
from email.mime.base import MIMEBase

def send_email_with_image(sender_email, password, recipient_email, subject, body, image_path):
    # Create the multipart email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the email body (text part)
    body_text = MIMEText(body, 'plain')
    msg.attach(body_text)

    # Attach the image part
    try:
        with open(image_path, 'rb') as image_file:
            img_data = image_file.read()
            image = MIMEImage(img_data, name=image_path.split("/")[-1])  # Take the filename from the path
            msg.attach(image)
    except FileNotFoundError as err:
        print(f"Error: The file {image_path} was not found. {err}")
        return

    # SMTP server connection and sending email
    try:
        # Connect to Gmail's SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Secure the connection with TLS
            server.login(sender_email, password)

            # Send the email
            server.sendmail(sender_email, recipient_email, msg.as_string())
            print("Email sent successfully!")

    except smtplib.SMTPException as e:
        print(f"Error sending email: {str(e)}")

# Example usage
sender_email = "sender@gmail.com"
password = "your password"  # Use app-specific password or OAuth if required
recipient_email = "recipient@gmail.com"
subject = "Test Email with Image"
body = "2030/1/1: This is a test email sent from Python, including an image attachment."
image_path = "path/to/your/image.jpg"

send_email_with_image(sender_email, password, recipient_email, subject, body, image_path)
