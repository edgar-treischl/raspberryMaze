import RPi.GPIO as GPIO
import time

BUZZER_PIN = 27  # GPIO-Pin an S-Pin des Buzzer-Moduls

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

try:
    print("Buzzer AN")
    GPIO.output(BUZZER_PIN, GPIO.HIGH)
    time.sleep(2)

    print("Buzzer AUS")
    GPIO.output(BUZZER_PIN, GPIO.LOW)
    time.sleep(2)

finally:
    GPIO.cleanup()
