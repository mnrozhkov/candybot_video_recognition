#!/usr/bin/env python3


"""
coffebot head motion controller
"""

import rospy

from coffebot.msg import HeadMotion, HeadState
from coffebot.motion.head.head_controller import Head
from coffebot.topic_controller import Lock


def main():

    rospy.init_node('motion_head_controller')

    head_motion_lock = Lock()
    rospy.Subscriber('head_motion', headMotion, head_motion_lock.callback)
    head_position_publisher = rospy.Publisher('head_state')

    head = Head(
       _h_angle = 0,
       _v_angle = 0,
       _led_on = True,
       _color = '#ffffff',
       _emotion = 'neutral',
       _h_SERVO_PIN = 18,
       _v_SERVO_PIN = 18,
       _PWM_DIVISOR = 384,      # clock at 50kHz (20us tick)
       _PWM_RANGE = 1000,       # range at 1000 ticks (20ms)
    )

    while True:

        #read HeadMotion message
        head_motion_msg =  head_motion_lock.message

        # some subscribers code here
        h_angle = None
        v_angle = None
        emotion = None

        #extract patameters from headMotion
        if head_motion_msg is not None:
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

        #if new headMotion message is equal to the old one clear field message of Lock class object
        if head_motion_lock.message == head_motion_msg:
            head_motion_lock.message = None
            # additional code here (i.e. publish head state)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
