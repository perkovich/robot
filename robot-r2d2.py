#!/usr/bin/env python


import RPi.GPIO as GPIO
import time
import urllib

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

switch = 21

GPIO.setup(switch, GPIO.IN, GPIO.PUD_UP)

while True:
  if GPIO.input(switch) == False:
   print("Laddar")
   time.sleep(1)
  else:
   print("Ute och klipper")
   time.sleep(1)

GPIO.cleanup()

