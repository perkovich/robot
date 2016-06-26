#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import urllib2
import datetime
import logging

logging.basicConfig(filename='R2D2.log',format='%(asctime)s %(message)s',level=logging.DEBUG)

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
     response = urllib2.urlopen('http://10.0.176.x:8080/json.htm?type=command&param=switchlight&idx=2&switchcmd=Off')
     html = response.read()
     logging.info('In')
     response = urllib2.urlopen('http://api.pushingbox.com/pushingbox?devid=xxxxx')
     html = response.read()
   last_seen = datetime.now()
   #timedelta will be the expected time out cutting grass
   expected_back = datetime.now() + timedelta(minutes=75)

  else:
   print("Ute och klipper")
   if charging == 0:
     charging = 1
     #Flip switch in Domoticz to say "Leaving charger"
     response = urllib2.urlopen('http://10.0.176.x:8080/json.htm?type=command&param=switchlight&idx=2&switchcmd=On')
     html = response.read()
     #temporarily set time
     expected_back = datetime.now() + timedelta(minutes=75)
     logging.info('Out')
     response = urllib2.urlopen('http://api.pushingbox.com/pushingbox?devid=xxxxx')
     html = response.read()
   charging = 1
   now = datetime.now()
   if now >= expected_back:
     if sent_alert == 0:
       #Flip doorbellswitch in Domoticz to say "I should be back by now, probably MIA"
       response = urllib2.urlopen('http://10.0.176.x:8080/json.htm?type=command&param=switchlight&idx=3&switchcmd=On')
       html = response.read()
       logging.info('Emergency')
       response = urllib2.urlopen('http://api.pushingbox.com/pushingbox?devid=xxxxx')
       html = response.read()
       sent_alert = 1
       print("Emergency!!")
   else:
    sent_alert = 0
  time.sleep(1)

GPIO.cleanup()


