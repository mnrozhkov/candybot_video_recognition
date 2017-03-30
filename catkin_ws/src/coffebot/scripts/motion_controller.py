#!/usr/bin/env python3

import rospy
import std_msgs

if __name__ == '__main__':

    rospy.init_node('motion_controller')
    
    position_publisher = rospy.Publisher('position', std_msgs.msg.String, queue_size=1)

    def callback_motion(data):
        pass


    rospy.Subscriber('motion', std_msgs.msg.String, callback_motion)

    rospy.spin()
