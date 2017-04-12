; Auto-generated. Do not edit!


(cl:in-package coffebot-msg)


;//! \htmlinclude SmileDetected.msg.html

(cl:defclass <SmileDetected> (roslisp-msg-protocol:ros-message)
  ((detected
    :reader detected
    :initarg :detected
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass SmileDetected (<SmileDetected>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SmileDetected>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SmileDetected)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name coffebot-msg:<SmileDetected> is deprecated: use coffebot-msg:SmileDetected instead.")))

(cl:ensure-generic-function 'detected-val :lambda-list '(m))
(cl:defmethod detected-val ((m <SmileDetected>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coffebot-msg:detected-val is deprecated.  Use coffebot-msg:detected instead.")
  (detected m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SmileDetected>) ostream)
  "Serializes a message object of type '<SmileDetected>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'detected) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SmileDetected>) istream)
  "Deserializes a message object of type '<SmileDetected>"
    (cl:setf (cl:slot-value msg 'detected) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SmileDetected>)))
  "Returns string type for a message object of type '<SmileDetected>"
  "coffebot/SmileDetected")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SmileDetected)))
  "Returns string type for a message object of type 'SmileDetected"
  "coffebot/SmileDetected")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SmileDetected>)))
  "Returns md5sum for a message object of type '<SmileDetected>"
  "2d8633c53221d40413712b55b8360a15")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SmileDetected)))
  "Returns md5sum for a message object of type 'SmileDetected"
  "2d8633c53221d40413712b55b8360a15")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SmileDetected>)))
  "Returns full string definition for message of type '<SmileDetected>"
  (cl:format cl:nil "bool detected~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SmileDetected)))
  "Returns full string definition for message of type 'SmileDetected"
  (cl:format cl:nil "bool detected~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SmileDetected>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SmileDetected>))
  "Converts a ROS message object to a list"
  (cl:list 'SmileDetected
    (cl:cons ':detected (detected msg))
))
