// Download the helper library from https://www.twilio.com/docs/node/install
// Your Account Sid and Auth Token from twilio.com/console
// DANGER! This is insecure. See http://twil.io/secure


//GUTHRIE'S personal sid, auth token and number
const accountSid = 'AC2e7524c64e69cd4843c70c59e9b32ef6';
const authToken = '30b4022d4974564ff352cb0cb8a5d5cf';
const freePhoneNumber = "+12029339382";
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