; Auto-generated. Do not edit!


(cl:in-package coffebot-msg)


;//! \htmlinclude APIAIBotAnswer.msg.html

(cl:defclass <APIAIBotAnswer> (roslisp-msg-protocol:ros-message)
  ((text
    :reader text
    :initarg :text
    :type cl:string
    :initform "")
   (action_name
    :reader action_name
    :initarg :action_name
    :type cl:string
    :initform "")
   (action_parameters_in_json
    :reader action_parameters_in_json
    :initarg :action_parameters_in_json
    :type cl:string
    :initform ""))
)

(cl:defclass APIAIBotAnswer (<APIAIBotAnswer>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <APIAIBotAnswer>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'APIAIBotAnswer)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name coffebot-msg:<APIAIBotAnswer> is deprecated: use coffebot-msg:APIAIBotAnswer instead.")))

(cl:ensure-generic-function 'text-val :lambda-list '(m))
(cl:defmethod text-val ((m <APIAIBotAnswer>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coffebot-msg:text-val is deprecated.  Use coffebot-msg:text instead.")
  (text m))

(cl:ensure-generic-function 'action_name-val :lambda-list '(m))
(cl:defmethod action_name-val ((m <APIAIBotAnswer>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coffebot-msg:action_name-val is deprecated.  Use coffebot-msg:action_name instead.")
  (action_name m))

(cl:ensure-generic-function 'action_parameters_in_json-val :lambda-list '(m))
(cl:defmethod action_parameters_in_json-val ((m <APIAIBotAnswer>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coffebot-msg:action_parameters_in_json-val is deprecated.  Use coffebot-msg:action_parameters_in_json instead.")
  (action_parameters_in_json m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <APIAIBotAnswer>) ostream)
  "Serializes a message object of type '<APIAIBotAnswer>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'text))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'text))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'action_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'action_name))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'action_parameters_in_json))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'action_parameters_in_json))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <APIAIBotAnswer>) istream)
  "Deserializes a message object of type '<APIAIBotAnswer>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'text) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'text) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'action_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'action_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'action_parameters_in_json) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'action_parameters_in_json) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<APIAIBotAnswer>)))
  "Returns string type for a message object of type '<APIAIBotAnswer>"
  "coffebot/APIAIBotAnswer")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'APIAIBotAnswer)))
  "Returns string type for a message object of type 'APIAIBotAnswer"
  "coffebot/APIAIBotAnswer")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<APIAIBotAnswer>)))
  "Returns md5sum for a message object of type '<APIAIBotAnswer>"
  "d9356e8a4f86a7632a7fb741a0ba9d22")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'APIAIBotAnswer)))
  "Returns md5sum for a message object of type 'APIAIBotAnswer"
  "d9356e8a4f86a7632a7fb741a0ba9d22")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<APIAIBotAnswer>)))
  "Returns full string definition for message of type '<APIAIBotAnswer>"
  (cl:format cl:nil "string text~%string action_name~%string action_parameters_in_json~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'APIAIBotAnswer)))
  "Returns full string definition for message of type 'APIAIBotAnswer"
  (cl:format cl:nil "string text~%string action_name~%string action_parameters_in_json~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <APIAIBotAnswer>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'text))
     4 (cl:length (cl:slot-value msg 'action_name))
     4 (cl:length (cl:slot-value msg 'action_parameters_in_json))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <APIAIBotAnswer>))
  "Converts a ROS message object to a list"
  (cl:list 'APIAIBotAnswer
    (cl:cons ':text (text msg))
    (cl:cons ':action_name (action_name msg))
    (cl:cons ':action_parameters_in_json (action_parameters_in_json msg))
))
