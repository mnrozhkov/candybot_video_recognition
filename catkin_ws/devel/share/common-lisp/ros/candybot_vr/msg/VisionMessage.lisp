; Auto-generated. Do not edit!


(cl:in-package candybot_vr-msg)


;//! \htmlinclude VisionMessage.msg.html

(cl:defclass <VisionMessage> (roslisp-msg-protocol:ros-message)
  ((face_count
    :reader face_count
    :initarg :face_count
    :type cl:integer
    :initform 0)
   (smile
    :reader smile
    :initarg :smile
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass VisionMessage (<VisionMessage>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <VisionMessage>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'VisionMessage)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name candybot_vr-msg:<VisionMessage> is deprecated: use candybot_vr-msg:VisionMessage instead.")))

(cl:ensure-generic-function 'face_count-val :lambda-list '(m))
(cl:defmethod face_count-val ((m <VisionMessage>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader candybot_vr-msg:face_count-val is deprecated.  Use candybot_vr-msg:face_count instead.")
  (face_count m))

(cl:ensure-generic-function 'smile-val :lambda-list '(m))
(cl:defmethod smile-val ((m <VisionMessage>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader candybot_vr-msg:smile-val is deprecated.  Use candybot_vr-msg:smile instead.")
  (smile m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <VisionMessage>) ostream)
  "Serializes a message object of type '<VisionMessage>"
  (cl:let* ((signed (cl:slot-value msg 'face_count)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'smile) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <VisionMessage>) istream)
  "Deserializes a message object of type '<VisionMessage>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'face_count) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:setf (cl:slot-value msg 'smile) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<VisionMessage>)))
  "Returns string type for a message object of type '<VisionMessage>"
  "candybot_vr/VisionMessage")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'VisionMessage)))
  "Returns string type for a message object of type 'VisionMessage"
  "candybot_vr/VisionMessage")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<VisionMessage>)))
  "Returns md5sum for a message object of type '<VisionMessage>"
  "38c28f9d3b21cf8ed2fa3008fac27d63")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'VisionMessage)))
  "Returns md5sum for a message object of type 'VisionMessage"
  "38c28f9d3b21cf8ed2fa3008fac27d63")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<VisionMessage>)))
  "Returns full string definition for message of type '<VisionMessage>"
  (cl:format cl:nil "int32 face_count~%bool smile~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'VisionMessage)))
  "Returns full string definition for message of type 'VisionMessage"
  (cl:format cl:nil "int32 face_count~%bool smile~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <VisionMessage>))
  (cl:+ 0
     4
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <VisionMessage>))
  "Converts a ROS message object to a list"
  (cl:list 'VisionMessage
    (cl:cons ':face_count (face_count msg))
    (cl:cons ':smile (smile msg))
))
