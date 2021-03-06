#!/usr/bin/python3

import time
import os

import logging

logging.basicConfig(filename="raspi_mirror.log", level=logging.INFO)
log = logging.getLogger("raspi_mirror")
log.info("script started")

try:
    import RPi.GPIO as GPIO
except Exception:
    log.exception("Not a Raspberry Pi to start on")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)

toggle = 0
try:
    while True:
        i=GPIO.input(12)
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
except Exception:
    log.exception("There was a problem.")
    log.info("restarting raspi_mirror")
    os.system('./run.py')
    time.sleep(1)
    quit()