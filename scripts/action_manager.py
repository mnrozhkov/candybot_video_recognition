#!/usr/bin/env python3

import rospy
from std_msgs.msg import String, Bool
from candybot_v2.msg import BotSpeechText
from network.weather import WeatherInfo
import time

class ActionManager:

    def __init__(self):
        self._actions = {
            'give_candy': self._give_candy,
            'say_weather': self._say_weather
        }

        rospy.Subscriber('/action_manager/action_name', String, self._callback_action)

        self.give_candy_publisher = rospy.Publisher('/action_manager/give_candy', Bool, queue_size=1)
        self.say_weather_publisher = rospy.Publisher('/core_decision_manager/bot_speech_text', BotSpeechText, queue_size=1)

        self.weather_info = WeatherInfo(openweathermap_key=rospy.get_param('openweathermap_key'))

    def _give_candy(self):
        print('action_manager.give_candy')
        self.give_candy_publisher.publish(True)

    def _say_weather(self):
        weather = self.weather_info.get_weather()
        print('action_manager.weather:', weather)
        if isinstance(weather, str):
            self.say_weather_publisher.publish(BotSpeechText(text=weather))

    def _callback_action(self, data):
        action = self._actions.get(data.data) #get action function
        if action is not None:
            action() #call action



if __name__ == '__main__':

    rospy.init_node('action_manager')
    action_manager = ActionManager()
    print('action_manager')

    while True:

        try:
            rospy.get_master().getPid()
        except:
            print(666)
            break

        time.sleep(0.5)
