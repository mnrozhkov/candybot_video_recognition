#!/usr/bin/env python3
'''
    1. recieve string from decision_publication topic
    2. convert it to dict
    3. by decision dict execute task
'''

import rospy
import std_msgs

import json

import time

class TaskExecutor():

    def execute(decision_dictionary: dict) -> None:

        pass


def main():

    texecutor = TaskExecutor()

    def callback_decision_publication(data: std_msgs.msg.String) -> None:
        decision_dictionary = json.loads(data.data)
        texecutor.execute(decision_dictionary)

    rospy.Subscriber('decision_publication', std_msgs.msg.String, callback_decision_publication)
    while True:
        time.sleep(0.1)


if __name__ == '__main__':
    main()
