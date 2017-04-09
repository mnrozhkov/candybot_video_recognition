# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "coffebot: 27 messages, 0 services")

set(MSG_I_FLAGS "-Icoffebot:/home/alex/catkin_ws/src/coffebot/msg;-Icoffebot:/home/alex/catkin_ws/devel/share/coffebot/msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg;-Iactionlib_msgs:/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(coffebot_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/MotionPattern.msg" NAME_WE)
add_custom_target(_coffebot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "coffebot" "/home/alex/catkin_ws/src/coffebot/msg/MotionPattern.msg" ""
)

get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionResult.msg" NAME_WE)
add_custom_target(_coffebot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "coffebot" "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionResult.msg" "coffebot/MakePhotoResult:actionlib_msgs/GoalID:std_msgs/Header:actionlib_msgs/GoalStatus"
)

get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/BotSpeechText.msg" NAME_WE)
add_custom_target(_coffebot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "coffebot" "/home/alex/catkin_ws/src/coffebot/msg/BotSpeechText.msg" ""
)

get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoGoal.msg" NAME_WE)
add_custom_target(_coffebot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "coffebot" "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoGoal.msg" "coffebot/MakeVideo"
)

get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/EyesState.msg" NAME_WE)
add_custom_target(_coffebot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "coffebot" "/home/alex/catkin_ws/src/coffebot/msg/EyesState.msg" ""
)

get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/SmileDetected.msg" NAME_WE)
add_custom_target(_coffebot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "coffebot" "/home/alex/catkin_ws/src/coffebot/msg/SmileDetected.msg" ""
)

get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoAction.msg" NAME_WE)
add_custom_target(_coffebot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "coffebot" "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoAction.msg" "coffebot/MakePhotoActionFeedback:std_msgs/Header:coffebot/MakePhotoActionResult:coffebot/MakePhoto:coffebot/MakePhotoGoal:coffebot/MakePhotoResult:coffebot/MakePhotoFeedback:actionlib_msgs/GoalID:coffebot/MakePhotoActionGoal:actionlib_msgs/GoalStatus"
)

get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoResult.msg" NAME_WE)
add_custom_target(_coffebot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "coffebot" "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoResult.msg" ""
)

get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoAction.msg" NAME_WE)
add_custom_target(_coffebot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "coffebot" "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoAction.msg" "coffebot/MakeVideo:std_msgs/Header:coffebot/MakeVideoResult:coffebot/MakeVideoFeedback:coffebot/MakeVideoActionGoal:coffebot/MakeVideoActionFeedback:coffebot/MakeVideoActionResult:actionlib_msgs/GoalID:coffebot/MakeVideoGoal:actionlib_msgs/GoalStatus"
)

get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionGoal.msg" NAME_WE)
add_custom_target(_coffebot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "coffebot" "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionGoal.msg" "coffebot/MakePhoto:actionlib_msgs/GoalID:coffebot/MakePhotoGoal:std_msgs/Header"
)

get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoResult.msg" NAME_WE)
add_custom_target(_coffebot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "coffebot" "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoResult.msg" ""
)

get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/UserSpeechText.msg" NAME_WE)
add_custom_target(_coffebot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "coffebot" "/home/alex/catkin_ws/src/coffebot/msg/UserSpeechText.msg" ""
)

get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoGoal.msg" NAME_WE)
add_custom_target(_coffebot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "coffebot" "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoGoal.msg" "coffebot/MakePhoto"
)

get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/FaceCoordinates.msg" NAME_WE)
add_custom_target(_coffebot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "coffebot" "/home/alex/catkin_ws/src/coffebot/msg/FaceCoordinates.msg" ""
)

get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/MakePhoto.msg" NAME_WE)
add_custom_target(_coffebot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "coffebot" "/home/alex/catkin_ws/src/coffebot/msg/MakePhoto.msg" ""
)

get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoFeedback.msg" NAME_WE)
add_custom_target(_coffebot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "coffebot" "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoFeedback.msg" ""
)

get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoFeedback.msg" NAME_WE)
add_custom_target(_coffebot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "coffebot" "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoFeedback.msg" ""
)

get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionResult.msg" NAME_WE)
add_custom_target(_coffebot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "coffebot" "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionResult.msg" "coffebot/MakeVideoResult:actionlib_msgs/GoalID:std_msgs/Header:actionlib_msgs/GoalStatus"
)

get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/MakeVideo.msg" NAME_WE)
add_custom_target(_coffebot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "coffebot" "/home/alex/catkin_ws/src/coffebot/msg/MakeVideo.msg" ""
)

get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/APIAIBotAnswer.msg" NAME_WE)
add_custom_target(_coffebot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "coffebot" "/home/alex/catkin_ws/src/coffebot/msg/APIAIBotAnswer.msg" ""
)

get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionFeedback.msg" NAME_WE)
add_custom_target(_coffebot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "coffebot" "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionFeedback.msg" "actionlib_msgs/GoalID:std_msgs/Header:coffebot/MakeVideoFeedback:actionlib_msgs/GoalStatus"
)

get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionFeedback.msg" NAME_WE)
add_custom_target(_coffebot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "coffebot" "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionFeedback.msg" "actionlib_msgs/GoalID:coffebot/MakePhotoFeedback:std_msgs/Header:actionlib_msgs/GoalStatus"
)

get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/Emotion.msg" NAME_WE)
add_custom_target(_coffebot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "coffebot" "/home/alex/catkin_ws/src/coffebot/msg/Emotion.msg" ""
)

get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/EyesMotion.msg" NAME_WE)
add_custom_target(_coffebot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "coffebot" "/home/alex/catkin_ws/src/coffebot/msg/EyesMotion.msg" ""
)

get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/Audio.msg" NAME_WE)
add_custom_target(_coffebot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "coffebot" "/home/alex/catkin_ws/src/coffebot/msg/Audio.msg" ""
)

get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/FaceFeatures.msg" NAME_WE)
add_custom_target(_coffebot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "coffebot" "/home/alex/catkin_ws/src/coffebot/msg/FaceFeatures.msg" ""
)

get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionGoal.msg" NAME_WE)
add_custom_target(_coffebot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "coffebot" "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionGoal.msg" "coffebot/MakeVideo:actionlib_msgs/GoalID:std_msgs/Header:coffebot/MakeVideoGoal"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/MotionPattern.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/coffebot
)
_generate_msg_cpp(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionResult.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/coffebot
)
_generate_msg_cpp(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/BotSpeechText.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/coffebot
)
_generate_msg_cpp(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/src/coffebot/msg/MakeVideo.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/coffebot
)
_generate_msg_cpp(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/EyesState.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/coffebot
)
_generate_msg_cpp(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/SmileDetected.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/coffebot
)
_generate_msg_cpp(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoAction.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionFeedback.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionResult.msg;/home/alex/catkin_ws/src/coffebot/msg/MakePhoto.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoGoal.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoResult.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionGoal.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/coffebot
)
_generate_msg_cpp(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/coffebot
)
_generate_msg_cpp(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoAction.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/src/coffebot/msg/MakeVideo.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoResult.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoFeedback.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionGoal.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionFeedback.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoGoal.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/coffebot
)
_generate_msg_cpp(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/src/coffebot/msg/MakePhoto.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoGoal.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/coffebot
)
_generate_msg_cpp(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/coffebot
)
_generate_msg_cpp(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/UserSpeechText.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/coffebot
)
_generate_msg_cpp(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/src/coffebot/msg/MakePhoto.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/coffebot
)
_generate_msg_cpp(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/FaceCoordinates.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/coffebot
)
_generate_msg_cpp(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/MakePhoto.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/coffebot
)
_generate_msg_cpp(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/coffebot
)
_generate_msg_cpp(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/coffebot
)
_generate_msg_cpp(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionResult.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/coffebot
)
_generate_msg_cpp(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/MakeVideo.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/coffebot
)
_generate_msg_cpp(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/APIAIBotAnswer.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/coffebot
)
_generate_msg_cpp(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/coffebot
)
_generate_msg_cpp(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoFeedback.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/coffebot
)
_generate_msg_cpp(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/Emotion.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/coffebot
)
_generate_msg_cpp(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/EyesMotion.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/coffebot
)
_generate_msg_cpp(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/Audio.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/coffebot
)
_generate_msg_cpp(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/FaceFeatures.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/coffebot
)
_generate_msg_cpp(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/src/coffebot/msg/MakeVideo.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoGoal.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/coffebot
)

### Generating Services

### Generating Module File
_generate_module_cpp(coffebot
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/coffebot
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(coffebot_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(coffebot_generate_messages coffebot_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/MotionPattern.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_cpp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionResult.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_cpp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/BotSpeechText.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_cpp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoGoal.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_cpp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/EyesState.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_cpp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/SmileDetected.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_cpp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoAction.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_cpp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoResult.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_cpp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoAction.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_cpp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionGoal.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_cpp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoResult.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_cpp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/UserSpeechText.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_cpp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoGoal.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_cpp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/FaceCoordinates.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_cpp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/MakePhoto.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_cpp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoFeedback.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_cpp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoFeedback.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_cpp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionResult.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_cpp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/MakeVideo.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_cpp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/APIAIBotAnswer.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_cpp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionFeedback.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_cpp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionFeedback.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_cpp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/Emotion.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_cpp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/EyesMotion.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_cpp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/Audio.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_cpp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/FaceFeatures.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_cpp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionGoal.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_cpp _coffebot_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(coffebot_gencpp)
add_dependencies(coffebot_gencpp coffebot_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS coffebot_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/MotionPattern.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/coffebot
)
_generate_msg_eus(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionResult.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/coffebot
)
_generate_msg_eus(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/BotSpeechText.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/coffebot
)
_generate_msg_eus(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/src/coffebot/msg/MakeVideo.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/coffebot
)
_generate_msg_eus(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/EyesState.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/coffebot
)
_generate_msg_eus(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/SmileDetected.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/coffebot
)
_generate_msg_eus(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoAction.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionFeedback.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionResult.msg;/home/alex/catkin_ws/src/coffebot/msg/MakePhoto.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoGoal.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoResult.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionGoal.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/coffebot
)
_generate_msg_eus(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/coffebot
)
_generate_msg_eus(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoAction.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/src/coffebot/msg/MakeVideo.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoResult.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoFeedback.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionGoal.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionFeedback.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoGoal.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/coffebot
)
_generate_msg_eus(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/src/coffebot/msg/MakePhoto.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoGoal.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/coffebot
)
_generate_msg_eus(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/coffebot
)
_generate_msg_eus(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/UserSpeechText.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/coffebot
)
_generate_msg_eus(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/src/coffebot/msg/MakePhoto.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/coffebot
)
_generate_msg_eus(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/FaceCoordinates.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/coffebot
)
_generate_msg_eus(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/MakePhoto.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/coffebot
)
_generate_msg_eus(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/coffebot
)
_generate_msg_eus(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/coffebot
)
_generate_msg_eus(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionResult.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/coffebot
)
_generate_msg_eus(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/MakeVideo.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/coffebot
)
_generate_msg_eus(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/APIAIBotAnswer.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/coffebot
)
_generate_msg_eus(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/coffebot
)
_generate_msg_eus(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoFeedback.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/coffebot
)
_generate_msg_eus(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/Emotion.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/coffebot
)
_generate_msg_eus(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/EyesMotion.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/coffebot
)
_generate_msg_eus(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/Audio.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/coffebot
)
_generate_msg_eus(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/FaceFeatures.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/coffebot
)
_generate_msg_eus(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/src/coffebot/msg/MakeVideo.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoGoal.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/coffebot
)

### Generating Services

### Generating Module File
_generate_module_eus(coffebot
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/coffebot
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(coffebot_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(coffebot_generate_messages coffebot_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/MotionPattern.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_eus _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionResult.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_eus _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/BotSpeechText.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_eus _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoGoal.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_eus _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/EyesState.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_eus _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/SmileDetected.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_eus _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoAction.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_eus _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoResult.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_eus _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoAction.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_eus _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionGoal.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_eus _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoResult.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_eus _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/UserSpeechText.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_eus _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoGoal.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_eus _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/FaceCoordinates.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_eus _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/MakePhoto.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_eus _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoFeedback.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_eus _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoFeedback.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_eus _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionResult.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_eus _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/MakeVideo.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_eus _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/APIAIBotAnswer.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_eus _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionFeedback.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_eus _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionFeedback.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_eus _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/Emotion.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_eus _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/EyesMotion.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_eus _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/Audio.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_eus _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/FaceFeatures.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_eus _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionGoal.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_eus _coffebot_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(coffebot_geneus)
add_dependencies(coffebot_geneus coffebot_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS coffebot_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/MotionPattern.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/coffebot
)
_generate_msg_lisp(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionResult.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/coffebot
)
_generate_msg_lisp(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/BotSpeechText.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/coffebot
)
_generate_msg_lisp(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/src/coffebot/msg/MakeVideo.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/coffebot
)
_generate_msg_lisp(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/EyesState.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/coffebot
)
_generate_msg_lisp(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/SmileDetected.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/coffebot
)
_generate_msg_lisp(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoAction.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionFeedback.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionResult.msg;/home/alex/catkin_ws/src/coffebot/msg/MakePhoto.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoGoal.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoResult.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionGoal.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/coffebot
)
_generate_msg_lisp(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/coffebot
)
_generate_msg_lisp(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoAction.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/src/coffebot/msg/MakeVideo.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoResult.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoFeedback.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionGoal.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionFeedback.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoGoal.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/coffebot
)
_generate_msg_lisp(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/src/coffebot/msg/MakePhoto.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoGoal.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/coffebot
)
_generate_msg_lisp(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/coffebot
)
_generate_msg_lisp(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/UserSpeechText.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/coffebot
)
_generate_msg_lisp(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/src/coffebot/msg/MakePhoto.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/coffebot
)
_generate_msg_lisp(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/FaceCoordinates.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/coffebot
)
_generate_msg_lisp(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/MakePhoto.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/coffebot
)
_generate_msg_lisp(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/coffebot
)
_generate_msg_lisp(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/coffebot
)
_generate_msg_lisp(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionResult.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/coffebot
)
_generate_msg_lisp(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/MakeVideo.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/coffebot
)
_generate_msg_lisp(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/APIAIBotAnswer.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/coffebot
)
_generate_msg_lisp(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/coffebot
)
_generate_msg_lisp(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoFeedback.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/coffebot
)
_generate_msg_lisp(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/Emotion.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/coffebot
)
_generate_msg_lisp(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/EyesMotion.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/coffebot
)
_generate_msg_lisp(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/Audio.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/coffebot
)
_generate_msg_lisp(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/FaceFeatures.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/coffebot
)
_generate_msg_lisp(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/src/coffebot/msg/MakeVideo.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoGoal.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/coffebot
)

### Generating Services

### Generating Module File
_generate_module_lisp(coffebot
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/coffebot
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(coffebot_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(coffebot_generate_messages coffebot_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/MotionPattern.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_lisp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionResult.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_lisp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/BotSpeechText.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_lisp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoGoal.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_lisp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/EyesState.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_lisp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/SmileDetected.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_lisp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoAction.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_lisp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoResult.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_lisp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoAction.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_lisp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionGoal.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_lisp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoResult.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_lisp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/UserSpeechText.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_lisp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoGoal.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_lisp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/FaceCoordinates.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_lisp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/MakePhoto.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_lisp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoFeedback.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_lisp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoFeedback.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_lisp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionResult.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_lisp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/MakeVideo.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_lisp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/APIAIBotAnswer.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_lisp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionFeedback.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_lisp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionFeedback.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_lisp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/Emotion.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_lisp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/EyesMotion.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_lisp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/Audio.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_lisp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/FaceFeatures.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_lisp _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionGoal.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_lisp _coffebot_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(coffebot_genlisp)
add_dependencies(coffebot_genlisp coffebot_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS coffebot_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/MotionPattern.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/coffebot
)
_generate_msg_nodejs(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionResult.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/coffebot
)
_generate_msg_nodejs(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/BotSpeechText.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/coffebot
)
_generate_msg_nodejs(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/src/coffebot/msg/MakeVideo.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/coffebot
)
_generate_msg_nodejs(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/EyesState.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/coffebot
)
_generate_msg_nodejs(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/SmileDetected.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/coffebot
)
_generate_msg_nodejs(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoAction.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionFeedback.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionResult.msg;/home/alex/catkin_ws/src/coffebot/msg/MakePhoto.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoGoal.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoResult.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionGoal.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/coffebot
)
_generate_msg_nodejs(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/coffebot
)
_generate_msg_nodejs(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoAction.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/src/coffebot/msg/MakeVideo.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoResult.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoFeedback.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionGoal.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionFeedback.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoGoal.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/coffebot
)
_generate_msg_nodejs(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/src/coffebot/msg/MakePhoto.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoGoal.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/coffebot
)
_generate_msg_nodejs(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/coffebot
)
_generate_msg_nodejs(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/UserSpeechText.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/coffebot
)
_generate_msg_nodejs(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/src/coffebot/msg/MakePhoto.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/coffebot
)
_generate_msg_nodejs(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/FaceCoordinates.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/coffebot
)
_generate_msg_nodejs(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/MakePhoto.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/coffebot
)
_generate_msg_nodejs(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/coffebot
)
_generate_msg_nodejs(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/coffebot
)
_generate_msg_nodejs(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionResult.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/coffebot
)
_generate_msg_nodejs(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/MakeVideo.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/coffebot
)
_generate_msg_nodejs(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/APIAIBotAnswer.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/coffebot
)
_generate_msg_nodejs(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/coffebot
)
_generate_msg_nodejs(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoFeedback.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/coffebot
)
_generate_msg_nodejs(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/Emotion.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/coffebot
)
_generate_msg_nodejs(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/EyesMotion.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/coffebot
)
_generate_msg_nodejs(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/Audio.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/coffebot
)
_generate_msg_nodejs(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/FaceFeatures.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/coffebot
)
_generate_msg_nodejs(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/src/coffebot/msg/MakeVideo.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoGoal.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/coffebot
)

### Generating Services

### Generating Module File
_generate_module_nodejs(coffebot
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/coffebot
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(coffebot_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(coffebot_generate_messages coffebot_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/MotionPattern.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_nodejs _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionResult.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_nodejs _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/BotSpeechText.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_nodejs _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoGoal.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_nodejs _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/EyesState.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_nodejs _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/SmileDetected.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_nodejs _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoAction.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_nodejs _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoResult.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_nodejs _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoAction.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_nodejs _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionGoal.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_nodejs _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoResult.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_nodejs _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/UserSpeechText.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_nodejs _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoGoal.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_nodejs _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/FaceCoordinates.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_nodejs _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/MakePhoto.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_nodejs _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoFeedback.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_nodejs _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoFeedback.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_nodejs _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionResult.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_nodejs _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/MakeVideo.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_nodejs _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/APIAIBotAnswer.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_nodejs _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionFeedback.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_nodejs _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionFeedback.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_nodejs _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/Emotion.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_nodejs _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/EyesMotion.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_nodejs _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/Audio.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_nodejs _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/FaceFeatures.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_nodejs _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionGoal.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_nodejs _coffebot_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(coffebot_gennodejs)
add_dependencies(coffebot_gennodejs coffebot_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS coffebot_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/MotionPattern.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/coffebot
)
_generate_msg_py(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionResult.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/coffebot
)
_generate_msg_py(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/BotSpeechText.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/coffebot
)
_generate_msg_py(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/src/coffebot/msg/MakeVideo.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/coffebot
)
_generate_msg_py(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/EyesState.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/coffebot
)
_generate_msg_py(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/SmileDetected.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/coffebot
)
_generate_msg_py(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoAction.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionFeedback.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionResult.msg;/home/alex/catkin_ws/src/coffebot/msg/MakePhoto.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoGoal.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoResult.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionGoal.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/coffebot
)
_generate_msg_py(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/coffebot
)
_generate_msg_py(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoAction.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/src/coffebot/msg/MakeVideo.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoResult.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoFeedback.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionGoal.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionFeedback.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoGoal.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/coffebot
)
_generate_msg_py(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/src/coffebot/msg/MakePhoto.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoGoal.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/coffebot
)
_generate_msg_py(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoResult.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/coffebot
)
_generate_msg_py(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/UserSpeechText.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/coffebot
)
_generate_msg_py(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/src/coffebot/msg/MakePhoto.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/coffebot
)
_generate_msg_py(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/FaceCoordinates.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/coffebot
)
_generate_msg_py(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/MakePhoto.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/coffebot
)
_generate_msg_py(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/coffebot
)
_generate_msg_py(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoFeedback.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/coffebot
)
_generate_msg_py(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionResult.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoResult.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/coffebot
)
_generate_msg_py(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/MakeVideo.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/coffebot
)
_generate_msg_py(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/APIAIBotAnswer.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/coffebot
)
_generate_msg_py(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoFeedback.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/coffebot
)
_generate_msg_py(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoFeedback.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalStatus.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/coffebot
)
_generate_msg_py(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/Emotion.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/coffebot
)
_generate_msg_py(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/EyesMotion.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/coffebot
)
_generate_msg_py(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/Audio.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/coffebot
)
_generate_msg_py(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/FaceFeatures.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/coffebot
)
_generate_msg_py(coffebot
  "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionGoal.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/src/coffebot/msg/MakeVideo.msg;/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg/GoalID.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoGoal.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/coffebot
)

### Generating Services

### Generating Module File
_generate_module_py(coffebot
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/coffebot
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(coffebot_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(coffebot_generate_messages coffebot_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/MotionPattern.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_py _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionResult.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_py _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/BotSpeechText.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_py _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoGoal.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_py _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/EyesState.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_py _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/SmileDetected.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_py _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoAction.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_py _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoResult.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_py _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoAction.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_py _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionGoal.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_py _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoResult.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_py _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/UserSpeechText.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_py _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoGoal.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_py _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/FaceCoordinates.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_py _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/MakePhoto.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_py _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoFeedback.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_py _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoFeedback.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_py _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionResult.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_py _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/MakeVideo.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_py _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/APIAIBotAnswer.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_py _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionFeedback.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_py _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionFeedback.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_py _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/Emotion.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_py _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/EyesMotion.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_py _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/Audio.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_py _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/FaceFeatures.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_py _coffebot_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionGoal.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_py _coffebot_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(coffebot_genpy)
add_dependencies(coffebot_genpy coffebot_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS coffebot_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/coffebot)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/coffebot
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(coffebot_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET actionlib_msgs_generate_messages_cpp)
  add_dependencies(coffebot_generate_messages_cpp actionlib_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/coffebot)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/coffebot
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(coffebot_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET actionlib_msgs_generate_messages_eus)
  add_dependencies(coffebot_generate_messages_eus actionlib_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/coffebot)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/coffebot
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(coffebot_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET actionlib_msgs_generate_messages_lisp)
  add_dependencies(coffebot_generate_messages_lisp actionlib_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/coffebot)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/coffebot
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(coffebot_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET actionlib_msgs_generate_messages_nodejs)
  add_dependencies(coffebot_generate_messages_nodejs actionlib_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/coffebot)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/coffebot\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/coffebot
    DESTINATION ${genpy_INSTALL_DIR}
    # skip all init files
    PATTERN "__init__.py" EXCLUDE
    PATTERN "__init__.pyc" EXCLUDE
  )
  # install init files which are not in the root folder of the generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/coffebot
    DESTINATION ${genpy_INSTALL_DIR}
    FILES_MATCHING
    REGEX "${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/coffebot/.+/__init__.pyc?$"
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(coffebot_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET actionlib_msgs_generate_messages_py)
  add_dependencies(coffebot_generate_messages_py actionlib_msgs_generate_messages_py)
endif()
