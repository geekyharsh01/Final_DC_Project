#!/usr/bin/env python2

import rospy

from std_msgs.msg import Int32 

nodeName1 = 'messagesubs'


topicName1 = 'info_back_from_first'

def callBackFunction(message):
	print("from Arduino, we recive %d" %message.data)


rospy.init_node(nodeName1, anonymous=True)
rospy.Subscriber(topicName1, Int32, callBackFunction)

rospy.spin()
