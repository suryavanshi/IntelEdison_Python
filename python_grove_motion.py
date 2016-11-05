import time, sys, signal, atexit
import pyupm_biss0001 as upmMotion

# Instantiate a Grove Motion sensor on GPIO pin D2
myMotion = upmMotion.BISS0001(3)


## Exit handlers ##
# This function stops python from printing a stacktrace when you hit control-C
def SIGINTHandler(signum, frame):
	raise SystemExit

# This function lets you run code on exit, including functions from myMotion
def exitHandler():
	print "Exiting"
	sys.exit(0)

# Register exit handlers
atexit.register(exitHandler)
signal.signal(signal.SIGINT, SIGINTHandler)


# Read the value every second and detect motion
while(1):
	if (myMotion.value()):
		print "Detecting moving object"
	else:
		print "No moving objects detected"
	time.sleep(1)