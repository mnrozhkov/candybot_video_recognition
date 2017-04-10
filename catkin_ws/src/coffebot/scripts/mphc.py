#!/usr/bin/env python3

import rospy
import actionlib

from coffebot.msg import MakePhotoAction, MakePhotoGoal

if __name__ == '__main__':
    rospy.init_node('mphc')
    print('mphc')
    client = actionlib.SimpleActionClient('make_photo', MakePhotoAction)
    client.wait_for_server()

    goal = MakePhotoGoal()
    goal.make_photo_command.make_photo = True
    goal.make_photo_command.photo_file_name = 'jjj.png'

    client.send_goal(goal)
    client.wait_for_result()
