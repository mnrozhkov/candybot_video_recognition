# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(WARNING "Invoking generate_messages() without having added any message or service file before.
You should either add add_message_files() and/or add_service_files() calls or remove the invocation of generate_messages().")
message(STATUS "coffebot: 0 messages, 0 services")

set(MSG_I_FLAGS "-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(coffebot_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages

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

# target for backward compatibility
add_custom_target(coffebot_gencpp)
add_dependencies(coffebot_gencpp coffebot_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS coffebot_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages

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

# target for backward compatibility
add_custom_target(coffebot_geneus)
add_dependencies(coffebot_geneus coffebot_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS coffebot_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages

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

# target for backward compatibility
add_custom_target(coffebot_genlisp)
add_dependencies(coffebot_genlisp coffebot_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS coffebot_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages

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

# target for backward compatibility
add_custom_target(coffebot_gennodejs)
add_dependencies(coffebot_gennodejs coffebot_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS coffebot_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages

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
add_dependencies(coffebot_generate_messages_cpp std_msgs_generate_messages_cpp)

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/coffebot)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/coffebot
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
add_dependencies(coffebot_generate_messages_eus std_msgs_generate_messages_eus)

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/coffebot)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/coffebot
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
add_dependencies(coffebot_generate_messages_lisp std_msgs_generate_messages_lisp)

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/coffebot)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/coffebot
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
add_dependencies(coffebot_generate_messages_nodejs std_msgs_generate_messages_nodejs)

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
add_dependencies(coffebot_generate_messages_py std_msgs_generate_messages_py)
