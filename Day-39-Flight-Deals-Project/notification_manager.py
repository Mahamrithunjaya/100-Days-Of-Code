import os
from twilio.rest import Client

TWILIO_SID = os.environ.get("SID_KEY")
TWILIO_AUTH_TOKEN = os.environ.get("AUTH_TOKEN")


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
