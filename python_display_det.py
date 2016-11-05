import pyupm_i2clcd as lcd
import time, sys, signal, atexit
import pyupm_rfr359f as upmRfr359f
import pyupm_biss0001 as upmMotion

# Initialize Jhd1313m1 at 0x3E (LCD_ADDRESS) and 0x62 (RGB_ADDRESS) 
myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
# Instantiate an RFR359F digital pin D2
# This was tested on the Grove IR Distance Interrupter
myDistInterrupter = upmRfr359f.RFR359F(2)
myMotion = upmMotion.BISS0001(3)

myLcd.setCursor(0,0)
# RGB Blue
#myLcd.setColor(53, 39, 249)

# RGB Red
myLcd.setColor(255, 0, 0)


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
		myLcd.write('Object det')
	else:
		print "Area is clear"
	if (myMotion.value()):
		print "Detecting moving object"
		myLcd.setCursor(1,2)
		myLcd.write('Movement')
	else:
		print "No moving objects detected"
	time.sleep(1)
	myLcd.clear()
	#myLcd.setCursor(0,0)
	