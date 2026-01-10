import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

print("Laser AN")
GPIO.output(17, GPIO.HIGH)
time.sleep(3)

print("Laser AUS")
GPIO.output(17, GPIO.LOW)
time.sleep(3)

GPIO.cleanup()
