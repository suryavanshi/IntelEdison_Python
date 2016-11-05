import time, sys, signal, atexit
import pyupm_grovemoisture as upmMoisture

# Instantiate a Grove Moisture sensor on analog pin A0
myMoisture = upmMoisture.GroveMoisture(0)


## Exit handlers ##
# This function stops python from printing a stacktrace when you hit control-C
def SIGINTHandler(signum, frame):
	raise SystemExit

# This function lets you run code on exit, including functions from myMoisture
def exitHandler():
	print "Exiting"
	sys.exit(0)

# Register exit handlers
atexit.register(exitHandler)
signal.signal(signal.SIGINT, SIGINTHandler)


# Values (approximate):
# 0-300,   sensor in air or dry soil
# 300-600, sensor in humid soil
# 600+,    sensor in wet soil or submerged in water

# Read the value every second and print the corresponding moisture level
while(1):
	moisture_val = myMoisture.value()
	if (moisture_val >= 0 and moisture_val < 300):
		result = "Dry"
	elif (moisture_val >= 300 and moisture_val < 600):
		result = "Moist"
	else:
		result = "Wet"
	print "Moisture value: {0}, {1}".format(moisture_val, result)
	time.sleep(1)