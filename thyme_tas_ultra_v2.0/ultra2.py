import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pin_trigger = 4
pin_echo = 17

GPIO.setup(pin_trigger, GPIO.OUT) # trigger signal
GPIO.output(pin_trigger, GPIO.LOW)

GPIO.setup(pin_echo, GPIO.IN) # echo signal

time.sleep(.5)

print("Measuring Distance...")

try :
    while True:
        GPIO.output(pin_trigger, GPIO.HIGH) # shoot the signal for 10 us
        time.sleep(.00001) # 10 us
        GPIO.output(pin_trigger, GPIO.LOW)

        # waiting for the return signal
        while GPIO.input(pin_echo) == GPIO.LOW :
            pass
        start = time.time()

        # receiving signal
    while GPIO.input(pin_echo) == GPIO.HIGH :
        pass
    stop = time.time()

    d = (stop - start) * 170 * 100 # cm, speed of sound 340 m/s in air,  d = 340/2
    print(format(d, ".2f") + " cm")

    time.sleep(.5)

except KeyboardInterrupt:
print("\nInterrupted!")

finally:
GPIO.cleanup()