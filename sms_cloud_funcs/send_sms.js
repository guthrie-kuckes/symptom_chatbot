// Download the helper library from https://www.twilio.com/docs/node/install
// Your Account Sid and Auth Token from twilio.com/console
// DANGER! This is insecure. See http://twil.io/secure


//GUTHRIE'S personal sid, auth token and number
const accountSid = '';
const authToken = '';
const freePhoneNumber = "";
const guthriesIphone = "_______";

const client = require('twilio')(accountSid, authToken);


//Note that in a test, this seemed to cost one cent
client.messages
  .create({
     body: 'This is the ship that made the Kessel Run in fourteen parsecs?',
     from: freePhoneNumber,
     to: guthriesIphone
   })
  .then(message => console.log(message.sid))