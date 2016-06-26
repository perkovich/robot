# robot
Raspberry PI to tell if robot is charging or out working

A automatic lawn mower ("robot") is one of the best choices to cut your lawn: automatic, continous, powered by electricity, keeps the grass green and the neighbours jealous. It usually does the job good without support but depending on your garden it might get stuck once in a while. There are advanced robots that are connected to internet and can send notifications but if you have a cheaper model you don't have features like that.

With the help of a Raspberry PI and a magnetic contact and this script I got basic functionality working. So now my robot has its own Twitter account (@stikla9) and it sends notification whenever it goes OUT to work, IN to charge or if its not returning within 75 minutes it sends an EMERGENCY. 

I use Domoticz to handle the notifications and to add the robot to my home automation system and the web service PushingBox (http://www.pushingbox.com) to update Twitter.

I use a magnetic contact like this but anyone will do: https://www.kjell.com/se/sortiment/hus-halsa-fritid/larm-sakerhet-overvakning/larm/detektorer-sensorer-brytare/magnetkontakt-nc-p50500

You need to have this to make it work
-------------------------------------
Raspberry PI with wifi-module
Magnetic contact
Wifi (open or closed)
Domoticz (server or slave depending on your setup)


You need to do this to make it work (not complete)
--------------------------------------------------
1. Put the magnetic contact on the robot and on the charger so that it connects when the robot is in the charger
2. Configure Raspberry PI to use a wifi and connect it to internet
3. Connect the magnetic contact to the GPIO (I used #21 but that can be changed)
4. Setup Domoticz switches for Emergency and for the charger
5. Create three different notifications on PushingBox (IN, OUT and EMERGENCY) if you want Twitter status updates
6. Put the script in a folder and configure it to use the right switches in Domoticz and the right GPIO
7. Start the script by running "nohup ./robot-r2d2.py &"
