#!/bin/bash

source devel/setup.bash
export PYTHONPATH=/usr/local/lib/python3.5/dist-packages:$PYTHONPATH

rosrun coffebot audio_capture.py & \
rosrun coffebot audio_min_volume_detector.py & \
rosrun coffebot audio_player.py & \
rosrun coffebot core_decision_manager.py & \
rosrun coffebot core_motion_manager.py & \
rosrun coffebot dialog_bot_manager.py & \
rosrun coffebot speech_recognition.py & \
rosrun coffebot speech_synthesizer.py & \
rosrun coffebot vision_camera_capture.py & \
rosrun coffebot vision_face_tracking.py & \
rosrun coffebot vision_face_recognition.py & \
rosrun coffebot vision_photo_capture.py & \
rosrun coffebot vision_video_capture.py & \
rosrun coffebot motion_body_controller.py & \
rosrun coffebot motion_eyebrows_controller.py & \
rosrun coffebot motion_eyes_controller.py & \
rosrun coffebot motion_head_controller.py
