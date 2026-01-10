import RPi.GPIO as GPIO
import time

BUZZER_PIN = 17  # GPIO-Pin an S-Pin des Buzzer-Moduls

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)


pwm = GPIO.PWM(BUZZER_PIN, 500)

try:
    pwm.start(90)
    time.sleep(2)
    pwm.stop()

finally:
    GPIO.cleanup()
