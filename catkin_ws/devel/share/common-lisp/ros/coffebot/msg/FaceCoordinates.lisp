; Auto-generated. Do not edit!


(cl:in-package coffebot-msg)


;//! \htmlinclude FaceCoordinates.msg.html

(cl:defclass <FaceCoordinates> (roslisp-msg-protocol:ros-message)
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
   (w
    :reader w
    :initarg :w
    :type cl:fixnum
    :initform 0)
   (h
    :reader h
    :initarg :h
    :type cl:fixnum
    :initform 0))
)

(cl:defclass FaceCoordinates (<FaceCoordinates>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <FaceCoordinates>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'FaceCoordinates)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name coffebot-msg:<FaceCoordinates> is deprecated: use coffebot-msg:FaceCoordinates instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <FaceCoordinates>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coffebot-msg:x-val is deprecated.  Use coffebot-msg:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <FaceCoordinates>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coffebot-msg:y-val is deprecated.  Use coffebot-msg:y instead.")
  (y m))

(cl:ensure-generic-function 'w-val :lambda-list '(m))
(cl:defmethod w-val ((m <FaceCoordinates>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coffebot-msg:w-val is deprecated.  Use coffebot-msg:w instead.")
  (w m))

(cl:ensure-generic-function 'h-val :lambda-list '(m))
(cl:defmethod h-val ((m <FaceCoordinates>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coffebot-msg:h-val is deprecated.  Use coffebot-msg:h instead.")
  (h m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <FaceCoordinates>) ostream)
  "Serializes a message object of type '<FaceCoordinates>"
  (cl:let* ((signed (cl:slot-value msg 'x)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'y)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'w)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'h)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <FaceCoordinates>) istream)
  "Deserializes a message object of type '<FaceCoordinates>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'x) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'y) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'w) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'h) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<FaceCoordinates>)))
  "Returns string type for a message object of type '<FaceCoordinates>"
  "coffebot/FaceCoordinates")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'FaceCoordinates)))
  "Returns string type for a message object of type 'FaceCoordinates"
  "coffebot/FaceCoordinates")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<FaceCoordinates>)))
  "Returns md5sum for a message object of type '<FaceCoordinates>"
  "829ccd7c6b3f8326d5abe6f86da52ef9")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'FaceCoordinates)))
  "Returns md5sum for a message object of type 'FaceCoordinates"
  "829ccd7c6b3f8326d5abe6f86da52ef9")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<FaceCoordinates>)))
  "Returns full string definition for message of type '<FaceCoordinates>"
  (cl:format cl:nil "#coordinates of face on some image~%~%#left-up angle coordinates~%int16 x~%int16 y~%#width and height of face region~%int16 w~%int16 h~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'FaceCoordinates)))
  "Returns full string definition for message of type 'FaceCoordinates"
  (cl:format cl:nil "#coordinates of face on some image~%~%#left-up angle coordinates~%int16 x~%int16 y~%#width and height of face region~%int16 w~%int16 h~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <FaceCoordinates>))
  (cl:+ 0
     2
     2
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <FaceCoordinates>))
  "Converts a ROS message object to a list"
  (cl:list 'FaceCoordinates
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
    (cl:cons ':w (w msg))
    (cl:cons ':h (h msg))
))
