# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "coffebot: 1 messages, 0 services")

set(MSG_I_FLAGS "-Icoffebot:/home/alex/catkin_ws/src/coffebot/msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(coffebot_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/Audio.msg" NAME_WE)
add_custom_target(_coffebot_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "coffebot" "/home/alex/catkin_ws/src/coffebot/msg/Audio.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/Audio.msg"
  "${MSG_I_FLAGS}"
  ""
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
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/Audio.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_cpp _coffebot_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(coffebot_gencpp)
add_dependencies(coffebot_gencpp coffebot_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS coffebot_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/Audio.msg"
  "${MSG_I_FLAGS}"
  ""
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
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/Audio.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_eus _coffebot_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(coffebot_geneus)
add_dependencies(coffebot_geneus coffebot_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS coffebot_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/Audio.msg"
  "${MSG_I_FLAGS}"
  ""
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
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/Audio.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_lisp _coffebot_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(coffebot_genlisp)
add_dependencies(coffebot_genlisp coffebot_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS coffebot_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/Audio.msg"
  "${MSG_I_FLAGS}"
  ""
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
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/Audio.msg" NAME_WE)
add_dependencies(coffebot_generate_messages_nodejs _coffebot_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(coffebot_gennodejs)
add_dependencies(coffebot_gennodejs coffebot_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS coffebot_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(coffebot
  "/home/alex/catkin_ws/src/coffebot/msg/Audio.msg"
  "${MSG_I_FLAGS}"
  ""
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
get_filename_component(_filename "/home/alex/catkin_ws/src/coffebot/msg/Audio.msg" NAME_WE)
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
