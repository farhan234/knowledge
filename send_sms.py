import os
import smtplib
from twilio.rest import Client

def func1():
    # Account SID from console
    account_sid_one = "ACf523bbdc454c6639a9e324c66a05d68b"

    # Auth Token from console
    auth_token_one = "1bd576083cc3dc1f4a75361c4b294a5d"

    account_sid = os.environ.get('TWILIO_ACCOUNT_SIDE')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

    client = Client(account_sid_one, auth_token_one)

    message = client.messages.create(
        to="‭+12143150137‬",
        from_="+12569603631",
        body="suck my asss")

    print(message.sid)


