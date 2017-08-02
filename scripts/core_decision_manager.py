#!/usr/bin/env python3
import sys
sys.path.insert(1, '/usr/local/lib/python3.5/dist-packages')

import rospy
import smach

from candybot_v2.msg import MotionPattern, Emotion
from candybot_v2.msg import UserSpeechText, BotSpeechText, APIAIBotAnswer
from candybot_v2.msg import FaceCoordinates, SmileDetected, FaceFeatures

from core.decision_state_machine import *

import json

import time


class Decision:
    '''
    Decision making class
    Functionality:
        1. collect audio, video, text and other data
        2. make decision by all information
    '''

    def __init__(self):
        '''
        Constructor
        '''

        self.bot_text_answer = str()
        self.bot_action_answer = str()
        self.bot_action_parameter_answer = dict()
        self.smile_exists = False
        self.face_coords = dict()
        self.face_info = dict()

        self._create_subscribers()

    def callback_face_info(self, data: FaceFeatures) -> None:
        '''
        Recieve and extract face features information
        Args:
            data: face features message
        '''

        if isinstance(data, FaceFeatures):
            self.face_info = dict()
            self.face_info['emotion'] = data.emotion
            self.face_info['gender'] = data.gender
            self.face_info['age'] = [data.min_age, data.max_age]


    def callback_face_coords(self, data: FaceCoordinates) -> None:
        '''
        Recieve closest face coordinates
        Args:
            data: face coordinates message
        '''

        self.face_coords = dict({'x': int(data.x), 'y': int(data.y), 'w': int(data.w), 'h': int(data.h)})


    def callback_smile(self, data: SmileDetected) -> None:
        '''
        Recieve information about smile existance at closest face
        Args:
            data: smile detected status
        '''
        print('callback_smile:', data.detected)
        if data.detected is True:
            self.smile_exists = True


    def callback_bot_dialog(self, data: APIAIBotAnswer) -> None:
        '''
        Recieve api.ai bot answer and extract from the answer speech text,
        action name and action parameters

        Args:
            data: api.ai bot answer in format
                dictionary = {
                    'text': text, 'action':{'name': name, 'parameters':parameters
                                  }
                }
        '''

        self.bot_text_answer = data.text
        print('\n\n\n\nTEXT!!!: ', self.bot_text_answer, '\n\n\n')
        if len(data.action_name) > 0:
            self.bot_action_answer = data.action_name
        if len(data.action_parameters_in_json) > 0:
            self.bot_action_parameter_answer = json.loads(data.action_parameters_in_json)

    def _create_subscribers(self):
        '''
        Create subscribers
        '''

        self.face_info_sub = rospy.Subscriber('/vision_face_recognition/face_info', FaceFeatures, self.callback_face_info)
        self.face_coord_sub = rospy.Subscriber('/vision_face_tracking/face_coord', FaceCoordinates, self.callback_face_coords)
        self.smile_detected_sub = rospy.Subscriber('/vision_face_tracking/smile_detected', SmileDetected, self.callback_smile)
        self.bot_dialog_sub = rospy.Subscriber('/dialog_bot_aimlmanager/bot_dialog', APIAIBotAnswer, self.callback_bot_dialog)

    def _delete_subscribers(self):
        '''
        Delete (unregister) subscribers
        '''

        self.face_info_sub.unregister()
        self.face_coord_sub.unregister()
        self.smile_detected_sub.unregister()
        self.bot_dialog_sub.unregister()

    def make_decision(self) -> None:
        '''
        Make decision by all collected information at current moment
        '''

        #create ROS Smach state machine


        sm = smach.StateMachine(outcomes=['end'])
        sm.userdata.bot_text_answer = self.bot_text_answer
        sm.userdata.bot_action_answer = self.bot_action_answer
        sm.userdata.smile_exists = self.smile_exists


        with sm:
            smach.StateMachine.add('BotAnswerState', BotAnswerState(),
                                    transitions={'outcome1':'end',
                                                 'outcome2':'SmileExistsState'
                                                },
                                    remapping={'bot_text_answer':'bot_text_answer',
                                               'bot_action_answer':'bot_action_answer'
                                              })

            smach.StateMachine.add('SmileExistsState', SmileExistsState(),
                                   transitions={'outcome1':'end'},
                                   remapping={'smile_exists':'smile_exists'})

        sm.execute()

        if self.bot_text_answer == sm.userdata.bot_text_answer:
            self.bot_text_answer = None
        if self.bot_action_answer == sm.userdata.bot_action_answer:
            self.bot_action_answer = None
        if self.smile_exists == sm.userdata.smile_exists:
            self.smile_exists = False


if __name__ == '__main__':

    rospy.init_node('core_decision_manager')

    decision = Decision()
    while True:
        try:
            rospy.get_master().getPid()
        except:
            break

        decision.make_decision()
        time.sleep(0.1)
