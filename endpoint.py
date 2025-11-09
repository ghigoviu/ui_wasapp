from twilio.rest import Client
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse

account_sid = 'AC1b23657f8e4a5ba89a64f2c325b944d7'
auth_token = 'bc4d7f42fd834c614edfaa33557b8c65'
client = Client(account_sid, auth_token)

"""
message = client.messages.create(
  from_='whatsapp:+14155238886',
  content_sid='HXb5b62575e6e4ff6129ad7c8efe1f983e',
  content_variables='{"1":"12/1","2":"3pm"}',
  to='whatsapp:+5215591393363'
)
"""

response = MessagingResponse()
message = Message()
message.body('Hello World!')
response.append(message)
response.redirect('https://demo.twilio.com/welcome/sms/')

print(response)
