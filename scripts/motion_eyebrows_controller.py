#!/usr/bin/env python3

import rospy
from motion.eyebrows.eyebrows_controller import Eyebrows
from candybot_v2.msg import EyebrowsMotion, EyebrowsState
from utils.topic_controller import Lock

import time


if __name__ == '__main__':
    rospy.init_node('motion_eyebrows_controller')

    eyebrows = Eyebrows(_l_angle=90, _r_angle=90, _l_SERVO_CHANNEL=1, _r_SERVO_CHANNEL=0, _led_on=False, _led_color='white', _emotion='neutral')
    eyebrows_motion_lock = Lock()
    rospy.Subscriber('/motion_eyebrows_controller/eyebrows_motion', EyebrowsMotion, eyebrows_motion_lock.callback)
    eyebrows_state_publisher = rospy.Publisher('/motion_eyebrows_controller/eyebrows_state', EyebrowsState, queue_size=1)
    print('motion_eyebrows_controller start')
    while True:
        try:
            rospy.get_master().getPid()
        except:
            break

        eyebrows_msg = eyebrows_motion_lock.message
        if isinstance(eyebrows_msg, EyebrowsMotion):
            eyebrows.set_left_servo_position(angle=eyebrows_msg.l_angle)
            eyebrows.set_right_servo_position(angle=eyebrows_msg.r_angle)
            eyebrows.set_emotion(emotion=eyebrows_msg.emotion)

            eyebrows_state_msg = EyesState()
            eyebrows_state_msg.l_angle, eyebrows_state_msg.r_angle = eyebrows.get_eyebrows_position()
            eyebrows_state_publisher.publish(eyebrows_state_msg)

            rospy.set_param('/eyebrows/l_angle', eyebrows_state_msg.l_angle)
            rospy.set_param('/eyebrows/r_angle', eyebrows_state_msg.r_angle)
            rospy.set_param('/eyebrows/emotion', eyebrows_state_msg.emotion)

        if eyebrows_motion_lock.message == eyebrows_msg:
            eyebrows_motion_lock.message = None

        time.sleep(0.5)
