import smtplib as st
from os import getenv
from email.message import EmailMessage


class Email:
    def send(self):
        """Sends an email with the invoice attached"""
        user = "test"
        host = "smtp.gmail.com"
        port = 587

        username = user
        password = getenv("PASSWORD")
        receiver = user

        # Message setup
        email_message = EmailMessage()
        email_message["Subject"] = "Invoice of Order #1"
        with open("invoice.pdf", "rb") as file:
            email_message.add_attachment(file.read(), maintype='application', subtype='pdf', filename='invoice.pdf')

        # Host setup
        gmail = st.SMTP(host, port)
        gmail.ehlo()
        gmail.starttls()
        gmail.login(username, password)

        # Sends the email
        gmail.sendmail(username, receiver, email_message.as_string())
        gmail.quit()
