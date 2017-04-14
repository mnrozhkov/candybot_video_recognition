# Install script for directory: /home/alex/catkin_ws/src/coffebot

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/alex/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  include("/home/alex/catkin_ws/build/coffebot/catkin_generated/safe_execute_install.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/coffebot/msg" TYPE FILE FILES
    "/home/alex/catkin_ws/src/coffebot/msg/APIAIBotAnswer.msg"
    "/home/alex/catkin_ws/src/coffebot/msg/Audio.msg"
    "/home/alex/catkin_ws/src/coffebot/msg/BotSpeechText.msg"
    "/home/alex/catkin_ws/src/coffebot/msg/Emotion.msg"
    "/home/alex/catkin_ws/src/coffebot/msg/FaceCoordinates.msg"
    "/home/alex/catkin_ws/src/coffebot/msg/FaceFeatures.msg"
    "/home/alex/catkin_ws/src/coffebot/msg/MakePhoto.msg"
    "/home/alex/catkin_ws/src/coffebot/msg/MakeVideo.msg"
    "/home/alex/catkin_ws/src/coffebot/msg/MotionPattern.msg"
    "/home/alex/catkin_ws/src/coffebot/msg/SmileDetected.msg"
    "/home/alex/catkin_ws/src/coffebot/msg/UserSpeechText.msg"
    "/home/alex/catkin_ws/src/coffebot/msg/EyesMotion.msg"
    "/home/alex/catkin_ws/src/coffebot/msg/EyesState.msg"
    "/home/alex/catkin_ws/src/coffebot/msg/HeadMotion.msg"
    "/home/alex/catkin_ws/src/coffebot/msg/HeadState.msg"
    "/home/alex/catkin_ws/src/coffebot/msg/Sound.msg"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/coffebot/action" TYPE FILE FILES
    "/home/alex/catkin_ws/src/coffebot/action/MakePhoto.action"
    "/home/alex/catkin_ws/src/coffebot/action/MakeVideo.action"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/coffebot/msg" TYPE FILE FILES
    "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoAction.msg"
    "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionGoal.msg"
    "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionResult.msg"
    "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoActionFeedback.msg"
    "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoGoal.msg"
    "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoResult.msg"
    "/home/alex/catkin_ws/devel/share/coffebot/msg/MakePhotoFeedback.msg"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/coffebot/msg" TYPE FILE FILES
    "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoAction.msg"
    "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionGoal.msg"
    "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionResult.msg"
    "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoActionFeedback.msg"
    "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoGoal.msg"
    "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoResult.msg"
    "/home/alex/catkin_ws/devel/share/coffebot/msg/MakeVideoFeedback.msg"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/coffebot/cmake" TYPE FILE FILES "/home/alex/catkin_ws/build/coffebot/catkin_generated/installspace/coffebot-msg-paths.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/alex/catkin_ws/devel/include/coffebot")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/alex/catkin_ws/devel/share/roseus/ros/coffebot")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/alex/catkin_ws/devel/share/common-lisp/ros/coffebot")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/alex/catkin_ws/devel/share/gennodejs/ros/coffebot")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python" -m compileall "/home/alex/catkin_ws/devel/lib/python2.7/dist-packages/coffebot")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/alex/catkin_ws/devel/lib/python2.7/dist-packages/coffebot" REGEX "/\\_\\_init\\_\\_\\.py$" EXCLUDE REGEX "/\\_\\_init\\_\\_\\.pyc$" EXCLUDE)
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/alex/catkin_ws/devel/lib/python2.7/dist-packages/coffebot" FILES_MATCHING REGEX "/home/alex/catkin_ws/devel/lib/python2.7/dist-packages/coffebot/.+/__init__.pyc?$")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/alex/catkin_ws/build/coffebot/catkin_generated/installspace/coffebot.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/coffebot/cmake" TYPE FILE FILES "/home/alex/catkin_ws/build/coffebot/catkin_generated/installspace/coffebot-msg-extras.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/coffebot/cmake" TYPE FILE FILES
    "/home/alex/catkin_ws/build/coffebot/catkin_generated/installspace/coffebotConfig.cmake"
    "/home/alex/catkin_ws/build/coffebot/catkin_generated/installspace/coffebotConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/coffebot" TYPE FILE FILES "/home/alex/catkin_ws/src/coffebot/package.xml")
endif()

