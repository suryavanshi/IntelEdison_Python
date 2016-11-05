from twilio.rest import TwilioRestClient

account_sid = "xxxx--------" #wrong, get the correct from twilio account
auth_token  = "xxxx-----"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Sent by Python Robot.Taking over the world soon",
    to="+1xxxx",    # Replace with your phone number
    from_="+1xxx-xxx-xxxx") # Replace with your Twilio number
print message.sid 
