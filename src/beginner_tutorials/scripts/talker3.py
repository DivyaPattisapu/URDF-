import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String
import time 
import signal
import sys

def sigint_handler(signal, frame):
    pub.publish('Publisher Exiting!')
    print("Exiting!")
    time.sleep(1)
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

pub = rospy.Publisher('chatter', Int32)
rospy.init_node('talker', anonymous=True)
i=0

while True:
    print("Message published")
    i=i+1
    pub.publish(i)
    time.sleep(1)
rospy.spin()

