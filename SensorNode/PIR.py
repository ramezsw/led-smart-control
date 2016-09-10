import RPi.GPIO as GPIO
import time

# Set the GPIO naming convention
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set a variable to hold the GPIO Pin identity
PinPIR = 17

#print("PIR Module Test (CTRL-C to exit)")

# Set pin as input
GPIO.setup(PinPIR, GPIO.IN)

def detect_motion():
    Current_State  = 0
    Previous_State = 0
    
    try:
        #print("Waiting for PIR to settle ...")
        # Loop until PIR output is 0

        while GPIO.input(PinPIR) == 1:
            Current_State = 0

        #print("    Ready")
        # Loop until users quits with CTRL-C
        while True:
            # Read PIR state
            Current_State = GPIO.input(PinPIR)

            # If the PIR is triggered
            if Current_State == 1 and Previous_State == 0:
                #start_time = time.time()
                return True
                #print("    Motion detected!")
                Previous_State = 1
            # If the PIR has returned to ready state
            elif Current_State == 0 and Previous_State == 1:
                #stop_time = time.time()
                #print("    Ready")
                #elapsed_time = int(stop_time- start_time)
                return False
                Previous_State = 0

                #print(start_time)
                #print(stop_time)
                #print(elapsed_time)

            #elapsed_time = int(stop_time- start_time)
            #return elapsed_time
        

            #stop_time= time.time()
            #elapsed = int(stop_time - start_time)
            #print(elapsed)
            #print(elapsed_time)

            # Wait for 10 milliseconds
            time.sleep(0.01)

    except KeyboardInterrupt:
        print(" Quit")

        # Reset GPIO settings
        GPIO.cleanup()

if __name__ == "__main__":
    while True:
        if detect_motion():
            print("detected")
