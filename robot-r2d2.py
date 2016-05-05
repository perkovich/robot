#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import urllib2
import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

from datetime import datetime, timedelta

switch = 21
charging = 0
GPIO.setup(switch, GPIO.IN, GPIO.PUD_UP)
now = datetime.now()
sent_alert = 0

while True:
  if GPIO.input(switch) == False:
   print("Laddar")
   if charging == 1:
     charging = 0
     #Flip switch in Domoticz to say "I'm in the charger now"
     response = urllib2.urlopen('http://10.0.176.46:8080/json.htm?type=command&param=switchlight&idx=2&switchcmd=Off')
     html = response.read()
   last_seen = datetime.now()
   #timedelta will be the expected time out cutting grass
   expected_back = datetime.now() + timedelta(minutes=45)

  else:
   print("Ute och klipper")
   if charging == 0:
     charging = 1
     #Flip switch in Domoticz to say "Leaving charger"
     response = urllib2.urlopen('http://10.0.176.46:8080/json.htm?type=command&param=switchlight&idx=2&switchcmd=On')
     html = response.read()
   charging = 1
   now = datetime.now()
   if now >= expected_back:
     if sent_alert == 0:
       #Flip doorbellswitch in Domoticz to say "I should be back by now, probably MIA"
       response = urllib2.urlopen('http://10.0.176.46:8080/json.htm?type=command&param=switchlight&idx=3&switchcmd=On')
       html = response.read()
       sent_alert = 1
       print("Emergency!!")
   else:
    sent_alert = 0
  time.sleep(1)

GPIO.cleanup()
