# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
GPIO.setmode (GPIO.BCM)
GPIO.setup(4,GPIO.IN)

camera = PiCamera()
i=0
for i in range (100):
        camera.start_preview()
        sleep(1)
        camera.capture('/home/pi/555_project/555_Final_Project/static/test.jpg')
        camera.stop_preview()
        sleep(5)
