

#
# Note: may need to follow these instructions
# https://www.twilio.com/docs/sms/quickstart/python
# to get this to work (some extra package instals may be required)
#
# test

# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from handle import process_response
import random

app = Flask(__name__)

#request parameter seems to make google cloud happy
@app.route("/sms", methods=['GET', 'POST'])
def handle_sms(request):
    """Respond to incoming messages with a friendly SMS."""
    try:
        # Start our response
        resp = MessagingResponse()
        print("got a request")

        # Add a message
        body = request.values.get('Body', None)
        phone = "2345678765"

        # mes = "We recieved your message  " + phone +" " +" body"
        mes = process_response(phone, random.randint(0,1), 0)

        resp.message(mes)
    except Exception as e:
        print(e)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)