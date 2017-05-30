#!/bin/bash

source devel/setup.bash
export PYTHONPATH=/usr/local/lib/python3.5/dist-packages:$PYTHONPATH

rosrun candybot_v2 audio_capture.py & \
rosrun candybot_v2 audio_min_volume_detector.py & \
rosrun candybot_v2 audio_player.py & \
rosrun candybot_v2 core_decision_manager.py & \
rosrun candybot_v2 core_motion_manager.py & \
rosrun candybot_v2 dialog_bot_manager.py & \
rosrun candybot_v2 speech_recognition.py & \
rosrun candybot_v2 speech_synthesizer.py & \
rosrun candybot_v2 vision_camera_capture.py & \
rosrun candybot_v2 vision_face_tracking.py & \
rosrun candybot_v2 vision_face_recognition.py & \
rosrun candybot_v2 vision_photo_capture.py & \
rosrun candybot_v2 vision_video_capture.py & \
rosrun candybot_v2 motion_body_controller.py & \
rosrun candybot_v2 motion_eyebrows_controller.py & \
rosrun candybot_v2 motion_eyes_controller.py & \
rosrun candybot_v2 motion_head_controller.py
