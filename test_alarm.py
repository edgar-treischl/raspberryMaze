import RPi.GPIO as GPIO
import time

# Pins
LASER_PIN = 17   # Laser S-Pin
BUZZER_PIN = 27  # Buzzer S-Pin

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(LASER_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

try:
    # Laser anmachen
    GPIO.output(LASER_PIN, GPIO.HIGH)
    print("Laser ist an")

    # Simulierte "Unterbrechung" nach 5 Sekunden
    time.sleep(5)
    laser_broken = True

    if laser_broken:
        print("Laser unterbrochen! Alarm!")
        GPIO.output(BUZZER_PIN, GPIO.HIGH)
        time.sleep(3)  # Buzzer piept 3 Sekunden
        GPIO.output(BUZZER_PIN, GPIO.LOW)

    # Laser aus
    GPIO.output(LASER_PIN, GPIO.LOW)
    print("Laser ist aus")

finally:
    GPIO.cleanup()
