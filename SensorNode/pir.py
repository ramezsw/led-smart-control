import RPi.GPIO as gpio
import time

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.IN)


def detect_motion():
    try:
        while True:
            if gpio.input(17) == 1:
                print("Motion Detected")
    except KeyboardInterrupt:
        gpio.cleanup()
        print("Quit")

if __name__ == "__main__":
    detect_motion()

    
