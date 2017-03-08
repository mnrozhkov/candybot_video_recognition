#!/usr/bin/env python3
'''Meke decision by recieved data'''

import rospy
from BotClient import APIAIBot
from typing import Dict
import json
from coffebot.audio.synthesizer import Talker
import std_msgs
import logging

logging.basicConfig(filename='desicions.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.ERROR)


class DecisionMaker:
    
    def __init__(self):
        self._parse_config()
        self.bot = APIAIBot(self._bot_client_key) #create object bot for using api.ai API
        self.talker = Talker(self._yandex_voice_key) #create object talker for TTS
        
    def _parse_config(self) -> None:
        config = json.load(open('coffebot.config', 'r'))
        self._bot_client_key = config['bot_client_key']
        self._yandex_voice_key = config['yandex_voice_key']

    def run_processes(self, *args) -> None:
        '''Resumes viewing and listening'''
        for arg in args:
            rospy.set_param(arg, True)

    def stop_processes(self, *args) -> None:
        '''Stops viewing and listening'''

        for arg in args:
            rospy.set_param(arg, False)

    def make_command(self, command: str, parameters: Dict) -> None:
    
        print('command: ', command, 'parameters: ', parameters)
        try:
            #split command into parts
            command_parts = command.split('.')
            #get command group
            command_group = command_parts[len(command_parts) - 2]
            #get command name
            command_name = command_parts[len(command_parts) - 1]
            #import command group module from command_modules folder
            command_module = __import__('command_modules.' + command_group)
            #call function with command name and parameters as arguments
            getattr(command_module, command_name)(parameters)
        except Exception as e:
            print(str(e))
    

    def callback_listen(self, data: std_msgs.msg.String) -> None:
        '''Listening callback function.
        Args:
            data: listen data, ROS String type
        '''
        print(type(data))
        if rospy.get_param('listening'):
            self.stop_processes('listening')
            d = data.data
            print('listened: ', d)
            answer = self.bot.request(d)
            text = answer['text']
            print('bot answer: ', text)
            if len(text) > 0:
                self.talker.sayyandex(text)
            if 'action' in answer.keys():
                self.make_command(answer['action']['name'], answer['action']['parameters'])
        self.run_processes('listening')

        if not rospy.get_param('listening'):
            self.run_processes('listening')


    def recieve(self):
        '''Recieves messages from listener and viewer
        '''
    
        rospy.init_node('decision_maker', anonymous=True)
        rospy.Subscriber('audio_decision', std_msgs.msg.String, self.callback_listen)
        print('I ready to recieve messages')
        rospy.spin()


def main():
    
    decision_maker = DecisionMaker()
    decision_maker.recieve()


if __name__ == '__main__':
    main()
