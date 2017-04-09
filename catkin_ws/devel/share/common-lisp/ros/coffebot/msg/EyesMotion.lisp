; Auto-generated. Do not edit!


(cl:in-package coffebot-msg)


;//! \htmlinclude EyesMotion.msg.html

(cl:defclass <EyesMotion> (roslisp-msg-protocol:ros-message)
  ((angle
    :reader angle
    :initarg :angle
    :type cl:float
    :initform 0.0)
   (distance_from_center_percent
    :reader distance_from_center_percent
    :initarg :distance_from_center_percent
    :type cl:float
    :initform 0.0)
   (emotion
    :reader emotion
    :initarg :emotion
    :type cl:string
    :initform ""))
)

(cl:defclass EyesMotion (<EyesMotion>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <EyesMotion>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'EyesMotion)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name coffebot-msg:<EyesMotion> is deprecated: use coffebot-msg:EyesMotion instead.")))

(cl:ensure-generic-function 'angle-val :lambda-list '(m))
(cl:defmethod angle-val ((m <EyesMotion>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coffebot-msg:angle-val is deprecated.  Use coffebot-msg:angle instead.")
  (angle m))

(cl:ensure-generic-function 'distance_from_center_percent-val :lambda-list '(m))
(cl:defmethod distance_from_center_percent-val ((m <EyesMotion>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coffebot-msg:distance_from_center_percent-val is deprecated.  Use coffebot-msg:distance_from_center_percent instead.")
  (distance_from_center_percent m))

(cl:ensure-generic-function 'emotion-val :lambda-list '(m))
(cl:defmethod emotion-val ((m <EyesMotion>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coffebot-msg:emotion-val is deprecated.  Use coffebot-msg:emotion instead.")
  (emotion m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <EyesMotion>) ostream)
  "Serializes a message object of type '<EyesMotion>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'angle))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'distance_from_center_percent))))
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
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <EyesMotion>) istream)
  "Deserializes a message object of type '<EyesMotion>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'angle) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'distance_from_center_percent) (roslisp-utils:decode-single-float-bits bits)))
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<EyesMotion>)))
  "Returns string type for a message object of type '<EyesMotion>"
  "coffebot/EyesMotion")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'EyesMotion)))
  "Returns string type for a message object of type 'EyesMotion"
  "coffebot/EyesMotion")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<EyesMotion>)))
  "Returns md5sum for a message object of type '<EyesMotion>"
  "0a9c274e737c0b917a24ecaa2a12792e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'EyesMotion)))
  "Returns md5sum for a message object of type 'EyesMotion"
  "0a9c274e737c0b917a24ecaa2a12792e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<EyesMotion>)))
  "Returns full string definition for message of type '<EyesMotion>"
  (cl:format cl:nil "float32 angle~%float32 distance_from_center_percent~%string emotion~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'EyesMotion)))
  "Returns full string definition for message of type 'EyesMotion"
  (cl:format cl:nil "float32 angle~%float32 distance_from_center_percent~%string emotion~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <EyesMotion>))
  (cl:+ 0
     4
     4
     4 (cl:length (cl:slot-value msg 'emotion))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <EyesMotion>))
  "Converts a ROS message object to a list"
  (cl:list 'EyesMotion
    (cl:cons ':angle (angle msg))
    (cl:cons ':distance_from_center_percent (distance_from_center_percent msg))
    (cl:cons ':emotion (emotion msg))
))
