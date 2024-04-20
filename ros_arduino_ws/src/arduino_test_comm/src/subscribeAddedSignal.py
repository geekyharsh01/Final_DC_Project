#!/usr/bin/env python2

import rospy

from std_msgs.msg import Int32 

nodeName1 = 'messagesubs222'


topicName1 = 'addedSignals'

def callBackFunction(message):
	print("From Broadcast, we recive %d" %message.data)


rospy.init_node(nodeName1, anonymous=True)
rospy.Subscriber(topicName1, Int32, callBackFunction)

rospy.spin()
