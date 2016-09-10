import time
import RPi.GPIO as GPIO
import os

# Set the GPIO Mode and set the pin to use for the
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# A variable with the LDR reading pin number
PINLDR = 27


def read_LDR():
    LDRCount = 0 # Sets the count to 0
    GPIO.setup(PINLDR, GPIO.OUT)
    GPIO.output(PINLDR, GPIO.LOW)
    time.sleep(0.1) # Drains all charge from the capacitor

    GPIO.setup(PINLDR, GPIO.IN) # Sets the pin to be input
    # While the input pin reads 'off' or Low, count
    while (GPIO.input(PINLDR) == GPIO.LOW):
        LDRCount += 1 # Add one to the counter
    return LDRCount


if __name__ == "__main__":
    while True:
        print(read_LDR())
        time.sleep(1) # Wait for a second
