
#
# Note: may need to follow these instructions
# https://www.twilio.com/docs/sms/quickstart/python
# to get this to work (some extra package instals may be required)
#


# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()
    print("got a request")
    # Add a message
    body = request.values.get('Body', None)
    mes = "Ahoy! Thanks so much for your message of " + body
    resp.message(mes)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)