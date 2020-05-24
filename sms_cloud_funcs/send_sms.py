
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

import credentials

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
client = Client(credentials.account_sid, credentials.auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_=credentials.freePhoneNumber,
                     to= credentials.guthriesIphone
                 )

print(message.sid)