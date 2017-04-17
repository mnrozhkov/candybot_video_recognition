#!/usr/bin/env python3


"""
coffebot head motion controller
"""

import wiringpi
import time
import math

#use BCM pin numbers
wiringpi.wiringPiSetupGpio()

# setup WiringPi PWM
SERVO_PIN = 18
PWM_DIVISOR = 384 # clock at 50kHz (20us tick)
PWM_RANGE = 1000  # range at 1000 ticks (20ms)

# setup pin as an output
wiringpi.pinMode(SERVO_PIN, 2)
wiringpi.pwmSetMode(0)
wiringpi.pwmSetClock(PWM_DIVISOR)
wiringpi.pwmSetRange(PWM_RANGE)
wiringpi.pwmWrite(SERVO_PIN, 0) #theretically 50 (1ms) to 100 (2ms) on my servo 40-200 works ok

import rospy
from coffebot.msg import HeadMotion, HeadState

from coffebot.topic_controller import Lock


class Head(object):

    def __init__(self):

        #horizontal and vertical angles
        self._h_angle = 0
        self._v_angle = 0

        #other settings
        self._emotion = 'neutral'


    def set_horizontal_servo_position(h_pos):
        """
        Turn servo on specified angle in degrees
        Params:
            pos: angle to turn servo, in degrees
        """

        h_move = int(40 + math.floor(h_pos * (200 - 40) / 180))
        print("pos: {}".format(h_pos))
        print("move: {}".format(h_move))

        if h_move > 0:
            print("move: ", h_move)
            try:
                wiringpi.pwmWrite(SERVO_PIN, h_move)
                self._h_angle = h_move
                # time.sleep(0.5)
                # print("wiringpi.pwmWrite(18,{})".format(move))
            except:
                # clean up
                wiringpi.pwmWrite(18, 0)
                print("Exception")

    def set_vertical_servo_position(v_pos):
        """
        Turn servo on specified angle in degrees
        Params:
            pos: angle to turn servo, in degrees
        """

        v_move = int(40 + math.floor(v_pos * (200 - 40) / 180))
        print("pos: {}".format(v_pos))
        print("move: {}".format(v_move))

        if v_move > 0:
            print("move: ", v_move)
            try:
                wiringpi.pwmWrite(SERVO_PIN, v_move)
                self._v_angle = v_move
                # time.sleep(0.5)
                # print("wiringpi.pwmWrite(18,{})".format(move))
            except:
                # clean up
                wiringpi.pwmWrite(18, 0)
                print("Exception")


    def get_head_position(self):
        return (self._h_angle, self._v_angle)


    def set_emotion(self, emotion=None):
        if emotion is None:
            self._emotion = 'neutral'
        else:
            self._emotion = emotion


    def get_emotion(self):
        return self._emotion


def main():

    rospy.init_node('motion_head_controller')

    head_motion_lock = Lock()
    rospy.Subscriber('head_motion', headMotion, head_motion_lock.callback)
    head_position_publisher = rospy.Publisher('head_state')

    head = Head()

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
