# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "candybot_vr: 1 messages, 0 services")

set(MSG_I_FLAGS "-Icandybot_vr:/home/alex/catkin_ws/src/candybot_vr/msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(candybot_vr_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/alex/catkin_ws/src/candybot_vr/msg/VisionMessage.msg" NAME_WE)
add_custom_target(_candybot_vr_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "candybot_vr" "/home/alex/catkin_ws/src/candybot_vr/msg/VisionMessage.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(candybot_vr
  "/home/alex/catkin_ws/src/candybot_vr/msg/VisionMessage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/candybot_vr
)

### Generating Services

### Generating Module File
_generate_module_cpp(candybot_vr
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/candybot_vr
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(candybot_vr_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(candybot_vr_generate_messages candybot_vr_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/alex/catkin_ws/src/candybot_vr/msg/VisionMessage.msg" NAME_WE)
add_dependencies(candybot_vr_generate_messages_cpp _candybot_vr_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(candybot_vr_gencpp)
add_dependencies(candybot_vr_gencpp candybot_vr_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS candybot_vr_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(candybot_vr
  "/home/alex/catkin_ws/src/candybot_vr/msg/VisionMessage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/candybot_vr
)

### Generating Services

### Generating Module File
_generate_module_eus(candybot_vr
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/candybot_vr
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(candybot_vr_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(candybot_vr_generate_messages candybot_vr_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/alex/catkin_ws/src/candybot_vr/msg/VisionMessage.msg" NAME_WE)
add_dependencies(candybot_vr_generate_messages_eus _candybot_vr_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(candybot_vr_geneus)
add_dependencies(candybot_vr_geneus candybot_vr_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS candybot_vr_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(candybot_vr
  "/home/alex/catkin_ws/src/candybot_vr/msg/VisionMessage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/candybot_vr
)

### Generating Services

### Generating Module File
_generate_module_lisp(candybot_vr
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/candybot_vr
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(candybot_vr_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(candybot_vr_generate_messages candybot_vr_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/alex/catkin_ws/src/candybot_vr/msg/VisionMessage.msg" NAME_WE)
add_dependencies(candybot_vr_generate_messages_lisp _candybot_vr_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(candybot_vr_genlisp)
add_dependencies(candybot_vr_genlisp candybot_vr_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS candybot_vr_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(candybot_vr
  "/home/alex/catkin_ws/src/candybot_vr/msg/VisionMessage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/candybot_vr
)

### Generating Services

### Generating Module File
_generate_module_nodejs(candybot_vr
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/candybot_vr
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(candybot_vr_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(candybot_vr_generate_messages candybot_vr_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/alex/catkin_ws/src/candybot_vr/msg/VisionMessage.msg" NAME_WE)
add_dependencies(candybot_vr_generate_messages_nodejs _candybot_vr_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(candybot_vr_gennodejs)
add_dependencies(candybot_vr_gennodejs candybot_vr_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS candybot_vr_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(candybot_vr
  "/home/alex/catkin_ws/src/candybot_vr/msg/VisionMessage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/candybot_vr
)

### Generating Services

### Generating Module File
_generate_module_py(candybot_vr
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/candybot_vr
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(candybot_vr_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(candybot_vr_generate_messages candybot_vr_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/alex/catkin_ws/src/candybot_vr/msg/VisionMessage.msg" NAME_WE)
add_dependencies(candybot_vr_generate_messages_py _candybot_vr_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(candybot_vr_genpy)
add_dependencies(candybot_vr_genpy candybot_vr_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS candybot_vr_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/candybot_vr)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/candybot_vr
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(candybot_vr_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/candybot_vr)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/candybot_vr
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(candybot_vr_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/candybot_vr)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/candybot_vr
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(candybot_vr_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/candybot_vr)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/candybot_vr
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(candybot_vr_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/candybot_vr)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/candybot_vr\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/candybot_vr
    DESTINATION ${genpy_INSTALL_DIR}
    # skip all init files
    PATTERN "__init__.py" EXCLUDE
    PATTERN "__init__.pyc" EXCLUDE
  )
  # install init files which are not in the root folder of the generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/candybot_vr
    DESTINATION ${genpy_INSTALL_DIR}
    FILES_MATCHING
    REGEX "${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/candybot_vr/.+/__init__.pyc?$"
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(candybot_vr_generate_messages_py std_msgs_generate_messages_py)
endif()
