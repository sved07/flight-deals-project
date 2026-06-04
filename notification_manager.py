import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = os.environ['TWILIO_ACCOUNT_SID']
        self.auth_token = os.environ['TWILIO_AUTH_TOKEN']
        self.client = Client(self.account_sid, self.auth_token)



    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{os.environ["TWILIO_WHATSAPP_FROM"]}',
            body=message_body,
            to=f'whatsapp:{os.environ["TWILIO_WHATSAPP_TO"]}'
        )
        print(message.sid)