; Auto-generated. Do not edit!


(cl:in-package coffebot-msg)


;//! \htmlinclude UserSpeechText.msg.html

(cl:defclass <UserSpeechText> (roslisp-msg-protocol:ros-message)
  ((text
    :reader text
    :initarg :text
    :type cl:string
    :initform ""))
)

(cl:defclass UserSpeechText (<UserSpeechText>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <UserSpeechText>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'UserSpeechText)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name coffebot-msg:<UserSpeechText> is deprecated: use coffebot-msg:UserSpeechText instead.")))

(cl:ensure-generic-function 'text-val :lambda-list '(m))
(cl:defmethod text-val ((m <UserSpeechText>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coffebot-msg:text-val is deprecated.  Use coffebot-msg:text instead.")
  (text m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <UserSpeechText>) ostream)
  "Serializes a message object of type '<UserSpeechText>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'text))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'text))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <UserSpeechText>) istream)
  "Deserializes a message object of type '<UserSpeechText>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'text) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'text) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<UserSpeechText>)))
  "Returns string type for a message object of type '<UserSpeechText>"
  "coffebot/UserSpeechText")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'UserSpeechText)))
  "Returns string type for a message object of type 'UserSpeechText"
  "coffebot/UserSpeechText")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<UserSpeechText>)))
  "Returns md5sum for a message object of type '<UserSpeechText>"
  "74697ed3d931f6eede8bf3a8dfeca160")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'UserSpeechText)))
  "Returns md5sum for a message object of type 'UserSpeechText"
  "74697ed3d931f6eede8bf3a8dfeca160")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<UserSpeechText>)))
  "Returns full string definition for message of type '<UserSpeechText>"
  (cl:format cl:nil "string text~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'UserSpeechText)))
  "Returns full string definition for message of type 'UserSpeechText"
  (cl:format cl:nil "string text~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <UserSpeechText>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'text))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <UserSpeechText>))
  "Converts a ROS message object to a list"
  (cl:list 'UserSpeechText
    (cl:cons ':text (text msg))
))
