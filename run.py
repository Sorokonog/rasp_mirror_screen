import RPi.GPIO as GPIO
import time
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(14, GPIO.IN)

toggle = 0

while True:
    i=GPIO.input(14)
    if i==0: #When output from motion sensor is LOW
        if toggle == 0:                 
            print ("mirrow",i)
            os.system("sudo vcgencmd display_power 0")
            time.sleep(0.1)
            toggle = 1
    elif i==1: #When output from motion sensor is HIGH
        if toggle == 1:       
            print ("ads",i)
            os.system("sudo vcgencmd display_power 1")  #Turn MirrowScreen ON
            time.sleep(0.1)
            toggle = 0