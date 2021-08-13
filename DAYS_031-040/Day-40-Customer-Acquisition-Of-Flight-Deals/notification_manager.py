import os
import smtplib
from twilio.rest import Client

TWILIO_SID = os.environ.get("SID_KEY")
TWILIO_AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=os.environ.get("FROM_NUMBER"),
            to=os.environ.get("TO_NUMBER"),
        )
        # SID of sent message
        # print(message.sid)
        print("Message sent Successfully.")

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)

            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"From: \"{os.environ.get('SENDER_NAME')}\"<{MY_EMAIL}>\n"
                        f"To: {email}\n"
                        f"Subject: New Low Price Flight!\n\n{message}\nLINK:\n{google_flight_link}".encode('utf-8')
                )
        print("Mail sent successfully.")
