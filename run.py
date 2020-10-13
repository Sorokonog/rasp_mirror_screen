import RPi.GPIO as GPIO
import time
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(14, GPIO.IN)

while True:
    i=GPIO.input(14)
    if i==0:                 #When output from motion sensor is LOW
        print ("mirrow",i)
        os.system("sudo vcgencmd display_power 0")
        time.sleep(0.1)
    elif i==1:               #When output from motion sensor is HIGH
        print ("ads",i)
        os.system("sudo vcgencmd display_power 1")  #Turn MirrowScreen ON
        time.sleep(0.1)