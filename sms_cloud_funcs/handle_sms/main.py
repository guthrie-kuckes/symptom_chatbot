

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

app = Flask(__name__)

#request parameter seems to make google cloud happy
@app.route("/sms", methods=['GET', 'POST'])
def handle_sms(request):
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()
    print("got a request")
    # Add a message
    body = request.values.get('Body', None)
    mes = "We recieved your message of " + body
    resp.message(mes)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)