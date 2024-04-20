#!/usr/bin/env python2


import rospy
# we are sedding Int32 message 
from std_msgs.msg import Int32

nodeName='messagepublisher'

#this it the topic name- Make sure that in the Arduino code, the subcriber node is subscribed to this exact topic 
topicName = 'information'
 #here, we initailaize our subscriber node 
#we set "anonymous=True" to make sure that the node h as a unique name 
#this parameter will add rando number to the end of the node name
rospy.init_node(nodeName,anonymous=True)

#here, we are saying that out node is publishing messages to topicName
#we speci fy the pype of messages we want to publish (Int32)
# queue_size=5 simply means that we limit the number of queued messages if the subscriber 
# cannot recive the messages fast enough 
publisher1= rospy.Publisher(topicName, Int32, queue_size =5)

ratePublisher = rospy.Rate(2)

intMessage=1

while not rospy.is_shutdown():
	rospy.loginfo(intMessage)
	publisher1.publish(intMessage)
	intMessage=intMessage+1
	ratePublisher.sleep()
