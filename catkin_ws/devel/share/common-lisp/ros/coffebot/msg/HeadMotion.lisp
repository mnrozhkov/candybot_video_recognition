; Auto-generated. Do not edit!


(cl:in-package coffebot-msg)


;//! \htmlinclude HeadMotion.msg.html

(cl:defclass <HeadMotion> (roslisp-msg-protocol:ros-message)
  ((h_angle
    :reader h_angle
    :initarg :h_angle
    :type cl:float
    :initform 0.0)
   (v_angle
    :reader v_angle
    :initarg :v_angle
    :type cl:float
    :initform 0.0)
   (emotion
    :reader emotion
    :initarg :emotion
    :type cl:string
    :initform ""))
)

(cl:defclass HeadMotion (<HeadMotion>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <HeadMotion>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'HeadMotion)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name coffebot-msg:<HeadMotion> is deprecated: use coffebot-msg:HeadMotion instead.")))

(cl:ensure-generic-function 'h_angle-val :lambda-list '(m))
(cl:defmethod h_angle-val ((m <HeadMotion>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coffebot-msg:h_angle-val is deprecated.  Use coffebot-msg:h_angle instead.")
  (h_angle m))

(cl:ensure-generic-function 'v_angle-val :lambda-list '(m))
(cl:defmethod v_angle-val ((m <HeadMotion>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coffebot-msg:v_angle-val is deprecated.  Use coffebot-msg:v_angle instead.")
  (v_angle m))

(cl:ensure-generic-function 'emotion-val :lambda-list '(m))
(cl:defmethod emotion-val ((m <HeadMotion>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coffebot-msg:emotion-val is deprecated.  Use coffebot-msg:emotion instead.")
  (emotion m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <HeadMotion>) ostream)
  "Serializes a message object of type '<HeadMotion>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'h_angle))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'v_angle))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'emotion))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'emotion))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <HeadMotion>) istream)
  "Deserializes a message object of type '<HeadMotion>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'h_angle) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'v_angle) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'emotion) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'emotion) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<HeadMotion>)))
  "Returns string type for a message object of type '<HeadMotion>"
  "coffebot/HeadMotion")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'HeadMotion)))
  "Returns string type for a message object of type 'HeadMotion"
  "coffebot/HeadMotion")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<HeadMotion>)))
  "Returns md5sum for a message object of type '<HeadMotion>"
  "57dac4b62b684f84f46d1dd244edf1e0")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'HeadMotion)))
  "Returns md5sum for a message object of type 'HeadMotion"
  "57dac4b62b684f84f46d1dd244edf1e0")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<HeadMotion>)))
  "Returns full string definition for message of type '<HeadMotion>"
  (cl:format cl:nil "float32 h_angle # 0.0 <= h_angle <= 360.0~%float32 v_angle # 0.0 <= v_angle <= 360.0~%string emotion~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'HeadMotion)))
  "Returns full string definition for message of type 'HeadMotion"
  (cl:format cl:nil "float32 h_angle # 0.0 <= h_angle <= 360.0~%float32 v_angle # 0.0 <= v_angle <= 360.0~%string emotion~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <HeadMotion>))
  (cl:+ 0
     4
     4
     4 (cl:length (cl:slot-value msg 'emotion))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <HeadMotion>))
  "Converts a ROS message object to a list"
  (cl:list 'HeadMotion
    (cl:cons ':h_angle (h_angle msg))
    (cl:cons ':v_angle (v_angle msg))
    (cl:cons ':emotion (emotion msg))
))
