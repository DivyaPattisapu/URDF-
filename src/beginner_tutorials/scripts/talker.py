#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
import time 
import signal
import sys

#-----------------------------------------------------------------
#SIGINT handler
def sigint_handler(signal, frame):
    pub.publish('Publisher Exiting!')
    print("Exiting!")
    time.sleep(1)
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)
pub = rospy.Publisher('chatter', String, queue_size=10)
rospy.init_node('talker', anonymous=True)
print("There")

while True:
    print("Mssg published")
    pub.publish('Hi')
    time.sleep(1)


