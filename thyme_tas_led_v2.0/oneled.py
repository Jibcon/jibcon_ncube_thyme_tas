import RPi.GPIO as GPIO
import time
import sys


def ledOff():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.OUT)
    GPIO.output(23, True)
    GPIO.cleanup()

def ledOn():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.OUT)
    GPIO.output(23, False)
    GPIO.cleanup()

if len(sys.argv) > 1:
    if(sys.argv[1] == "0"):
        print "LED OFF"
        ledOff();
    elif(sys.argv[1] == "1"):
        print "LED ON"
        ledOn();
else:
    print "Not enough args"