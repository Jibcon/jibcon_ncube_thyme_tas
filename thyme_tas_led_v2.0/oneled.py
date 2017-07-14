import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

print "LED On"

GPIO.setup(23, GPIO.OUT)
GPIO.output(23, False)

GPIO.output(23, True)

time.sleep(1)

GPIO.output(23, False)

# raw_input('press enter to exit program')

GPIO.cleanup()
