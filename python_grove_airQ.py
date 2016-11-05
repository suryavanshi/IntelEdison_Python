from time import sleep
import pyupm_gas as TP401

# Give a qualitative meaning to the value from the sensor
def airQuality(value):
    if(value < 50): return "Fresh Air"
    if(value < 200): return "Normal Indoor Air"
    if(value < 400): return "Low Pollution"
    if(value < 600): return "High Pollution - Action Recommended"
    return "Very High Pollution - Take Action Immediately"

# New Grove Air Quality Sensor on AIO pin 0
airSensor = TP401.TP401(0)

# Wait for sensor to warm up
print "Sensor is warming up for 3 minutes..."
for i in range (1, 4):
    sleep(60)
    print i, "minute(s) passed."
print "Sensor is ready!"

# Loop indefinitely
while True:

    # Read values (consecutive reads might vary slightly)
    value = airSensor.getSample()
    ppm = airSensor.getPPM()

    print "raw: %4d" % value , " ppm: %5.2f   " % ppm , airQuality(value)

    # Sleep for 2.5 s
    sleep(2.5)