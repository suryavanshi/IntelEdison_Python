import time, sys, signal, atexit
import pyupm_biss0001 as upmMotion
import datetime
from twilio.rest import TwilioRestClient


account_sid = "xxxx" #wrong, get the correct from twilio account
auth_token  = "xxxx"
client = TwilioRestClient(account_sid, auth_token)
 
def send_message():
	msg = "Hey there, Someone at Door at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
	message = client.messages.create(body=msg,
		to="+1xxx-xxx-xxxx",    # Replace with your phone number
		from_="+1xxx-xxx-xxxx") # Replace with your Twilio number
	print message.sid 


# Instantiate an RFR359F digital pin D2
# This was tested on the Grove IR Distance Interrupter
myMotion = upmMotion.BISS0001(3)


## Exit handlers ##
# This function stops python from printing a stacktrace when you hit control-C
def SIGINTHandler(signum, frame):
	raise SystemExit

# This function lets you run code on exit, including functions from myDistInterrupter
def exitHandler():
	print "Exiting"
	sys.exit(0)

# Register exit handlers
atexit.register(exitHandler)
signal.signal(signal.SIGINT, SIGINTHandler)

sent = 0
cnt = 0

while(1):
	if (myMotion.value()):
		print "Motion detected"
		cnt = cnt + 1
		if cnt ==5: 
			print "send text"
			send_message()
			print "Exiting loop"
			break	
		
	else:
		print "Area is clear"
	time.sleep(1)