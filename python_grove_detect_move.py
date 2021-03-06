import time, sys, signal, atexit
import pyupm_rfr359f as upmRfr359f
import pyupm_biss0001 as upmMotion

# Instantiate an RFR359F digital pin D2
# This was tested on the Grove IR Distance Interrupter
myDistInterrupter = upmRfr359f.RFR359F(2)
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


while(1):
	if (myDistInterrupter.objectDetected()):
		print "Object detected"
	else:
		print "Area is clear"
	if (myMotion.value()):
		print "Detecting moving object"
	else:
		print "No moving objects detected"
	time.sleep(1)