; Auto-generated. Do not edit!


(cl:in-package coffebot-msg)


;//! \htmlinclude Audio.msg.html

(cl:defclass <Audio> (roslisp-msg-protocol:ros-message)
  ((content
    :reader content
    :initarg :content
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 0 :element-type 'cl:fixnum :initial-element 0)))
)

(cl:defclass Audio (<Audio>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Audio>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Audio)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name coffebot-msg:<Audio> is deprecated: use coffebot-msg:Audio instead.")))

(cl:ensure-generic-function 'content-val :lambda-list '(m))
(cl:defmethod content-val ((m <Audio>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coffebot-msg:content-val is deprecated.  Use coffebot-msg:content instead.")
  (content m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Audio>) ostream)
  "Serializes a message object of type '<Audio>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'content))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:write-byte (cl:ldb (cl:byte 8 0) ele) ostream))
   (cl:slot-value msg 'content))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Audio>) istream)
  "Deserializes a message object of type '<Audio>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'content) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'content)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:aref vals i)) (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Audio>)))
  "Returns string type for a message object of type '<Audio>"
  "coffebot/Audio")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Audio)))
  "Returns string type for a message object of type 'Audio"
  "coffebot/Audio")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Audio>)))
  "Returns md5sum for a message object of type '<Audio>"
  "72abf3d8306e84a4caf970654ef2815d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Audio)))
  "Returns md5sum for a message object of type 'Audio"
  "72abf3d8306e84a4caf970654ef2815d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Audio>)))
  "Returns full string definition for message of type '<Audio>"
  (cl:format cl:nil "uint8[] content~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Audio)))
  "Returns full string definition for message of type 'Audio"
  (cl:format cl:nil "uint8[] content~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Audio>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'content) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 1)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Audio>))
  "Converts a ROS message object to a list"
  (cl:list 'Audio
    (cl:cons ':content (content msg))
))
