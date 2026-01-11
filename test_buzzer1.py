import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

print("a = AN | o = AUS | q = Beenden")

while True:
key = input("> ")

if key == "a":
GPIO.output(17, GPIO.HIGH)
    elif key == "o":

GPIO.output(17, GPIO.LOW)
elif key == "q":
break

GPIO.cleanup()