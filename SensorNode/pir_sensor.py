import RPi.GPIO as GPIO
import time
import datetime


GPIO.setmode(GPIO.BCM)
PIR_PIN = 17
GPIO.setup(PIR_PIN, GPIO.IN)


def MOTION(PIR_PIN):
        #start_time = time.time()
        #print("fuck u")
        return True
        
#time.sleep(1)
#print("READY")


def mot():
        while 1:
                presence = GPIO.input(PIR_PIN)

                if(presence):
                        return True
                        presence = 0
                        time.sleep(2)
def detect_motion():
        try:
                GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
        
                #start_time = time.time()
                #print(start_time)


                #print(GPIO.event_detected(PIR_PIN))
                #print(PIR_PIN)
                #stop_time = time.time()
                #elapsed_time = int(stop_time - start_time)
                #print(elapsed_time)
                while 1:
                        time.sleep(100)

        except KeyboardInterrupt:
                print(" Quit")
                GPIO.cleanup()

if __name__ == "__main__":
        while True:
                print(detect_motion())
                
