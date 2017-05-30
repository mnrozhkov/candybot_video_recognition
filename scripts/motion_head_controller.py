#!/usr/bin/env python3


"""
candybot_v2 head motion controller
"""

import rospy

from candybot_v2.msg import HeadMotion, HeadState
from motion.head.head_controller import Head
from utils.topic_controller import Lock

import time


def main():

    rospy.init_node('motion_head_controller')

    head_motion_lock = Lock()
    rospy.Subscriber('/motion_head_controller/head_motion', HeadMotion, head_motion_lock.callback)
    head_position_publisher = rospy.Publisher('/motion_head_controller/head_state', HeadState, queue_size=1)

    head = Head(
       _h_angle = 0,
       _v_angle = 0,
       #_led_on = True,
       #_color = '#ffffff',
       _emotion = 'neutral',
       #_h_SERVO_PIN = 18,
       #_v_SERVO_PIN = 18,
       #_PWM_DIVISOR = 384,      # clock at 50kHz (20us tick)
       #_PWM_RANGE = 1000,       # range at 1000 ticks (20ms)
       _h_SERVO_CHANNEL=3,
       _v_SERVO_CHANNEL=2
    )
    print('motion_head_controller start')
    while True:
        try:
            rospy.get_master().getPid()
        except:
            break

        #read HeadMotion message
        head_motion_msg =  head_motion_lock.message

        # some subscribers code here
        h_angle = None
        v_angle = None
        emotion = None

        #extract patameters from headMotion
        if isinstance(head_motion_msg, HeadMotion):
            h_angle = head_motion_msg.h_angle
            v_angle = head_motion_msg.v_angle
            emotion = head_motion_msg.emotion

        # check params
        if h_angle is not None:
            head.set_horizontal_servo_position(h_angle)
        if v_angle is not None:
            head.set_vertical_servo_position(v_angle)
        if emotion is not None:
            head.set_emotion(emotion)

        head_state_msg = HeadState()
        head_state_msg.state.h_angle, head_state_msg.state.v_angle = head.get_head_position()
        head_state_msg.state.emotion = head.get_emotion()

        head_position_publisher.publish(head_state_msg)

        rospy.set_param('/head/h_angle', head_state_msg.state.h_angle)
        rospy.set_param('/head/v_angle', head_state_msg.state.v_angle)
        rospy.set_param('/head/emotion', head_state_msg.state.emotion)

        #if new headMotion message is equal to the old one clear field message of Lock class object
        if head_motion_lock.message == head_motion_msg:
            head_motion_lock.message = None
            # additional code here (i.e. publish head state)

        time.sleep(0.5)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
