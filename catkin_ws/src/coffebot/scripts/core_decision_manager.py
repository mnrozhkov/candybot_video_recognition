#!/usr/bin/env python3

import rospy
import std_msgs

from coffebot.core import decision_manager
import json

import time

class InputDataReciever:

    def __init__(self):

        self.bot_text_answer = None
        self.bot_action_answer = str()
        self.bot_action_parameter_answer = dict()
        self.smile_exists = False
        self.user_emotion = str()


        def callback_face_info(data: std_msgs.msg.String) -> None:
            pass


        def callback_face_coord(data: std_msgs.msg.String) -> None:
            pass


        def callback_smile(data: std_msgs.msg.Bool) -> None:
            pass


        def callback_bot_dialog(data: std_msgs.msg.String) -> None:
            pass



        rospy.Subscriber('face_info', std_msgs.msg.String, callback_face_info)
        rospy.Subscriber('face_coord', std_msgs.msg.String, callback_face_coord)
        rospy.Subscriber('smile', std_msgs.msg.Bool, callback_smile)
        rospy.Subscriber('bot_dialog', std_msgs.msg.String, callback_bot_dialog)


if __name__ == '__main__':

    rospy.init_node('core_decision_manager')

    idr = InputDataReciever()
    decision = decision_manager.Decision()

    pattern = decision.make_decision(idr.bot_text_answer, idr.bot_action_answer, idr.bot_action_parameter_answer, idr.smile_exists, idr.user_emotion)

    pattern_publisher = rospy.Publisher('pattern', std_msgs.msg.String, queue_size=1)
    emotion_publisher = rospy.Publisher('emotion', std_msgs.msg.String, queue_size=1)
    make_video_publisher = rospy.Publisher('make_video', std_msgs.msg.String, queue_size=1)
    make_photo_publisher = rospy.Publisher('make_photo', std_msgs.msg.String, queue_size=1)

    while True:
        #.....
        pattern_publisher.publish(json.dumps(pattern))
        emotion_publisher.publish('')
        make_video_publisher.publish('')
        make_photo_publisher('')

        time.sleep(0.1)
