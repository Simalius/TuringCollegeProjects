import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

class EmailSender:
    def __init__(self):
        self.smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
        self.smtp_port = int(os.getenv("SMTP_PORT", 587))
        self.username = os.getenv("SENDER_EMAIL")
        self.password = os.getenv("SENDER_PASSWORD")

        if not self.username or not self.password:
            raise ValueError("Email username or password is not set. Please check your .env file.")

    def send_email(self, recipient_email, subject, body, attachment_path=None):
        if not self.username or not self.password:
            print("Email username or password is not set. Please check your .env file.")
            return
        
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = recipient_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        if attachment_path:
            try:
                with open(attachment_path, "rb") as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header(
                        "Content-Disposition",
                        f"attachment; filename= {os.path.basename(attachment_path)}",
                    )
                    msg.attach(part)
            except FileNotFoundError:
                print(f"Attachment {attachment_path} not found.")
                return

        try:
            if self.smtp_port == 465:
                with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
                    server.login(self.username, self.password)
                    server.send_message(msg)
            else:
                with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                    server.starttls()
                    server.login(self.username, self.password)
                    server.send_message(msg)
            print(f"Email sent to {recipient_email}.")
        except smtplib.SMTPAuthenticationError:
            print("Failed to send email: Authentication Error. Check your username and password.")
        except smtplib.SMTPException as e:
            print(f"Failed to send email: SMTP Error - {str(e)}")
        except Exception as e:
            print(f"Failed to send email: {str(e)}")
