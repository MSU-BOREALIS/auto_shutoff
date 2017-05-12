import os
import sys
import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


#these pins are off limits 
#21, 20, 26, 19, 13, 6 ,5, 18
#these BCM pins are all used on sensors
########## Constants #############
AUTOSHUTDOWN = 1
SWITCHGPIO   = 8
##################################

def switchCallback(channel):
    global AUTOSHUTDOWN
    if AUTOSHUTDOWN == 1:
        #doesn't seem to print
        print "Now going to shutdown"
        os.system('/sbin/shutdown -h now')
    sys.exit(0)

def main():
    global SWITCHGPIO
    global AUTOSHUTDOWN
    
    #using the pull-up on this pin
    GPIO.setup(SWITCHGPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    #starting a thread to watch for a falling event on this pin.
    #will run switchCallback() when this completes
    GPIO.add_event_detect(SWITCHGPIO, GPIO.FALLING, callback=switchCallback,bounce_time=200)


    try:
        while True:
            sleep(5)
#            print "I have waited for 5s" 
    except:
        GPIO.cleanup()

if __name__ == '__main__':
    main()



