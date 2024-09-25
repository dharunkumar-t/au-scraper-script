import smtplib
from email.mime.text import MIMEText

def send_email(message):
    smtp_server = "localhost"
    smtp_port = 1025
    sender_email = "your_email@example.com"  #sender email
    receiver_email = "recipient_email@example.com"  #recipient's email

    msg = MIMEText(message)
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "New University Announcement"

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.send_message(msg)
