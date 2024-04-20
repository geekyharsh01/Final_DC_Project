#!/usr/bin/env python2

import rospy
from std_msgs.msg import Int32 

nodeName1 = 'message_subs'
topicName1 = 'info_back_from_first'
topicName2 = 'info_back_from_second'
broadcastTopicName = 'addedSignals'

received_values = [0, 0]

def callback_function_1(message):
    received_values[0] = message.data

def callback_function_2(message):
    received_values[1] = message.data

def listener():
    rospy.init_node(nodeName1, anonymous=True)
    rospy.Subscriber(topicName1, Int32, callback_function_1)
    rospy.Subscriber(topicName2, Int32, callback_function_2)

    broadcast_publisher = rospy.Publisher(broadcastTopicName, Int32, queue_size=10)

    rate = rospy.Rate(10)  # Set the rate to 1 Hz

    while not rospy.is_shutdown():
        sum_value = sum(received_values)
        print("Sum of received values: %d" % sum_value)
        
        # Publish the sum value to the broadcastAddedSignals topic
        broadcast_publisher.publish(sum_value)
        
        rate.sleep()

if __name__ == '__main__':
    listener()


rospy.spin()
