import time 
from time import strftime
import os

os.system("clear" + "&&" +  "notify-send 'Eye Care is on.'")
print "Eye Care for linux"
print "------------------\n\n", "Welcome", strftime("%H:%M")
while True:
        time.sleep(20 * 60)
        print "Take a break.", strftime("%H:%M")
        os.system("notify-send 'Take a break!'")

# My first awesome app!  ioblock/eyecare-py
