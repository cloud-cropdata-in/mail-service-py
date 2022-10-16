import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def smtpMail(sender_email, receiver_email, password, message, subject=None, cc_email=None):
    port = 587
    smtp_server = 'smtp.gmail.com'
    msg = MIMEMultipart('alternative')
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = ', '.join(receiver_email)
    if cc_email:
        msg["Cc"] = ', '.join(cc_email)
    part2 = MIMEText(message, 'html')
    msg.attach(part2)

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)
            server.login(sender_email, password)
            server.send_message(msg)

    except Exception as e:
        print(e)
