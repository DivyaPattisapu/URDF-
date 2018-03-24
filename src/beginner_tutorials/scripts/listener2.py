import rospy
from std_msgs.msg import Int32

def factorial(a):
	if a==1:
		return 1
	elif a==0:
		return 1
	else:
		return a*factorial(a-1)
		
def callback(inp):
	print factorial(inp.data)
	
rospy.init_node('listener', anonymous=True)

rospy.Subscriber('chatter', Int32, callback)
rospy.spin() 


