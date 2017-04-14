; Auto-generated. Do not edit!


(cl:in-package coffebot-msg)


;//! \htmlinclude EyesState.msg.html

(cl:defclass <EyesState> (roslisp-msg-protocol:ros-message)
  ((x
    :reader x
    :initarg :x
    :type cl:fixnum
    :initform 0)
   (y
    :reader y
    :initarg :y
    :type cl:fixnum
    :initform 0)
   (emotion
    :reader emotion
    :initarg :emotion
    :type cl:string
    :initform ""))
)

(cl:defclass EyesState (<EyesState>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <EyesState>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'EyesState)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name coffebot-msg:<EyesState> is deprecated: use coffebot-msg:EyesState instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <EyesState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coffebot-msg:x-val is deprecated.  Use coffebot-msg:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <EyesState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coffebot-msg:y-val is deprecated.  Use coffebot-msg:y instead.")
  (y m))

(cl:ensure-generic-function 'emotion-val :lambda-list '(m))
(cl:defmethod emotion-val ((m <EyesState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coffebot-msg:emotion-val is deprecated.  Use coffebot-msg:emotion instead.")
  (emotion m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <EyesState>) ostream)
  "Serializes a message object of type '<EyesState>"
  (cl:let* ((signed (cl:slot-value msg 'x)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'y)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'emotion))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'emotion))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <EyesState>) istream)
  "Deserializes a message object of type '<EyesState>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'x) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'y) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<EyesState>)))
  "Returns string type for a message object of type '<EyesState>"
  "coffebot/EyesState")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'EyesState)))
  "Returns string type for a message object of type 'EyesState"
  "coffebot/EyesState")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<EyesState>)))
  "Returns md5sum for a message object of type '<EyesState>"
  "bcfd694b6a681b718890867e9439c098")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'EyesState)))
  "Returns md5sum for a message object of type 'EyesState"
  "bcfd694b6a681b718890867e9439c098")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<EyesState>)))
  "Returns full string definition for message of type '<EyesState>"
  (cl:format cl:nil "int8 x #0.0 <= x <= 128~%int8 y #0.0 <= y <= 128~%string emotion~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'EyesState)))
  "Returns full string definition for message of type 'EyesState"
  (cl:format cl:nil "int8 x #0.0 <= x <= 128~%int8 y #0.0 <= y <= 128~%string emotion~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <EyesState>))
  (cl:+ 0
     1
     1
     4 (cl:length (cl:slot-value msg 'emotion))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <EyesState>))
  "Converts a ROS message object to a list"
  (cl:list 'EyesState
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
    (cl:cons ':emotion (emotion msg))
))
