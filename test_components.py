# Laser Maze Tripwire - Individual Component Test
# Test Laser, LED, and Buzzer separately
# LDR not included yet

import RPi.GPIO as GPIO
import time

# ---------------------------
# GPIO PIN SETUP
# ---------------------------
LASER_PIN = 17   # GPIO for Laser
LED_PIN = 27     # GPIO for LED (MOSFET input)
BUZZER_PIN = 22  # GPIO for Buzzer

# Use BCM numbering
GPIO.setmode(GPIO.BCM)

# Set pins as outputs
GPIO.setup(LASER_PIN, GPIO.OUT)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# ---------------------------
# Test Laser
# ---------------------------
input("Press Enter to test LASER...")
print("Laser ON for 3 seconds")
GPIO.output(LASER_PIN, GPIO.HIGH)
time.sleep(3)
GPIO.output(LASER_PIN, GPIO.LOW)
print("Laser OFF")

# ---------------------------
# Test LED
# ---------------------------
input("Press Enter to test LED...")
print("LED ON for 3 seconds")
GPIO.output(LED_PIN, GPIO.HIGH)
time.sleep(3)
GPIO.output(LED_PIN, GPIO.LOW)
print("LED OFF")

# ---------------------------
# Test Buzzer
# ---------------------------
input("Press Enter to test BUZZER...")
print("Buzzer ON for 3 seconds")
GPIO.output(BUZZER_PIN, GPIO.HIGH)
time.sleep(3)
GPIO.output(BUZZER_PIN, GPIO.LOW)
print("Buzzer OFF")

# ---------------------------
# Cleanup GPIO
# ---------------------------
GPIO.cleanup()
print("All tests complete. GPIO cleaned up.")
