# *****************************************************************
# ** python script to run in the background to watch GPIO     *****
# ** pin for a falling edge and shutdown pi when falling edge *****
# *****************************************************************

import os
import sys
import RPi.GPIO as GPIO
from time import sleep


# ********* constants **********************
# these constants can also be updated from a config file if desired to pass values to the program
AUTOSHUTDOWN = 1      # used for implementing a config file
SWITCHGPIO = 8        # GPIO pin to watch
# ******************************************

GPIO.setmode(GPIO.BCM)      # use broadcom pin numbering
GPIO.setwarnings(False)
GPIO.setup(SWITCHGPIO, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def switchCallback(channel):
    global AUTOSHUTDOWN

    if AUTOSHUTDOWN == 1:
        os.system('/sbin/shutdown -h now')
    sys.exit(0)

def main():
    global SWITCHGPIO
    GPIO.add_event_detect(SWITCHGPIO, GPIO.FALLING, callback=switchCallback)
    
    try:
        while True:
            sleep(5)
    except:
        GPIO.cleanup()


if __name__=='__main__':
    main()

