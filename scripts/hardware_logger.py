#!/usr/bin/env python3

import rospy
import json
import time

HARDWARE_HISTORY_FILE = 'hardware.hist'

def log_body():
    body_state = dict({'angle': None, 'emotion': None})
    if rospy.has_param('/body/angle') is True:
        body_state['angle'] = rospy.get_param('/body/angle')
    if rospy.has_param('/body/emotion') is True:
        body_state['emotion'] = rospy.get_param('/body/emotion')

    return body_state


def log_eyebrows():

    eyebrows_state = dict({'l_angle': None, 'r_angle': None, 'emotion': None})

    if rospy.has_param('/eyebrows/l_angle') is True:
        eyebrows_state['l_angle'] = rospy.get_param('/eyebrows/l_angle')
    if rospy.has_param('/eyebrows/r_angle') is True:
        eyebrows_state['r_angle'] = rospy.get_param('/eyebrows/r_angle')
    if rospy.has_param('/eyebrows/emotion') is True:
        eyebrows_state['emotion'] = rospy.get_param('/eyebrows/emotion')

    return eyebrows_state


def log_eyes():

    eyes_state = dict({'x': None, 'y': None, 'emotion': None})

    if rospy.has_param('/eyes/x') is True:
        eyes_state['x'] = rospy.get_param('/eyes/x')
    if rospy.has_param('/eyes/y') is True:
        eyes_state['y'] = rospy.get_param('/eyes/y')
    if rospy.has_param('/eyes/x') is True:
        eyes_state['emotion'] = rospy.get_param('/eyes/emotion')

    return eyes_state


def log_head():

    head_state = dict({'h_angle': None, 'v_angle': None, 'emotion': None})

    if rospy.has_param('/head/h_angle') is True:
        head_state['h_angle'] = rospy.get_param('/head/h_angle')
    if rospy.has_param('/head/v_angle') is True:
        head_state['v_angle'] = rospy.get_param('/head/v_angle')
    if rospy.has_param('/head/emotion') is True:
        head_state['emotion'] = rospy.get_param('/head/emotion')

    return head_state


if __name__ == '__main__':
    rospy.init_node('hardware_logger')

    while True:
        try:
            rospy.get_master().getPid()
        except:
            break

        hardware_state = dict()
        cur_time = time.time()
        hardware_state[cur_time] = dict()
        hardware_state[cur_time]['body'] = log_body()
        hardware_state[cur_time]['eyebrows'] = log_eyebrows()
        hardware_state[cur_time]['eyes'] = log_eyes()
        hardware_state[cur_time]['head'] = log_head()

        json.dumps(obj=hardware_state, fp=open(HARDWARE_HISTORY_FILE, 'a', ensure_ascii=False, indent=4))

        time.sleep(1)
