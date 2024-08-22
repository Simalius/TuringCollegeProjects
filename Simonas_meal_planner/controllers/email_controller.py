from utils.email_sender import EmailSender

class EmailController:
    def __init__(self):
        self.email_sender = EmailSender()

    def send_shopping_list(self, recipient_email, subject, body, attachment_path=None):
        try:
            self.email_sender.send_email(recipient_email, subject, body, attachment_path)
        except Exception as e:
            print(f"Failed to send email: {str(e)}")
