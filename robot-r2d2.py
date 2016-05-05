#!/usr/bin/env python


import RPi.GPIO as GPIO
import time
import urllib2
import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

from datetime import datetime, timedelta

switch = 21
laddar = 0
GPIO.setup(switch, GPIO.IN, GPIO.PUD_UP)
now = datetime.now()
sent_alert = 0

while True:
  if GPIO.input(switch) == False:
   print("Laddar")
   if laddar == 1:
     laddar = 0
     response = urllib2.urlopen('http://10.0.176.46:8080/json.htm?type=command&param=switchlight&idx=2&switchcmd=Off')
     html = response.read()
   last_seen = datetime.now()
   expected_back = datetime.now() + timedelta(seconds=10)

  else:
   print("Ute och klipper")
   if laddar == 0:
     laddar = 1
     response = urllib2.urlopen('http://10.0.176.46:8080/json.htm?type=command&param=switchlight&idx=2&switchcmd=On')
     html = response.read()
   laddar = 1
   now = datetime.now()
   if now >= expected_back:
     if sent_alert == 0:
       response = urllib2.urlopen('http://10.0.176.46:8080/json.htm?type=command&param=switchlight&idx=3&switchcmd=On')
       html = response.read()
       sent_alert = 1
       print("Emergency!!")
   else:
    sent_alert = 0
  time.sleep(1)

GPIO.cleanup()
