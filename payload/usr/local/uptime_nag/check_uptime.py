#!/usr/bin/python

# Get epoch time of last boot and subtract that from the current epoch time then convert to days. 
# If the amount of days up is great than or equal to 30 send the user a notification alerting them
# that they need to reboot. 

import subprocess
import sys
import time
import os

def bashCommand(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

    stdout = []
    while True:
        line = p.stdout.readline()
        stdout.append(line)
        print(line),
        if line == '' and p.poll() != None:
            break
    return ''.join(stdout)

def days_up(upt_epo):
    epoch_now = int(time.time())
    diff = epoch_now - upt_epo
    days_up = diff / 84600
    return days_up

uptime_epoch = bashCommand("sysctl -n kern.boottime | awk '{print $4}' | sed 's/,//g'")
uptime_epoch = int(uptime_epoch)

if days_up(uptime_epoch) >= 30:
    bashCommand('/usr/local/bin/yo_scheduler -t "Unbounce I.T." -s `date +%H:%M:%S` -n "It looks like your computer has been up for over a month - please reboot!" -b "More Info" -B "./usr/local/uptime_nag/pop_dialog"')
    print "notification sent - stop snooping in my scripts"
else:
    print "within limits - if you're reading this you're pretty nosey."
exit(0)
