; Auto-generated. Do not edit!


(cl:in-package coffebot-msg)


;//! \htmlinclude MakePhotoResult.msg.html

(cl:defclass <MakePhotoResult> (roslisp-msg-protocol:ros-message)
  ((result
    :reader result
    :initarg :result
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass MakePhotoResult (<MakePhotoResult>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MakePhotoResult>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MakePhotoResult)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name coffebot-msg:<MakePhotoResult> is deprecated: use coffebot-msg:MakePhotoResult instead.")))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <MakePhotoResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coffebot-msg:result-val is deprecated.  Use coffebot-msg:result instead.")
  (result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MakePhotoResult>) ostream)
  "Serializes a message object of type '<MakePhotoResult>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'result) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MakePhotoResult>) istream)
  "Deserializes a message object of type '<MakePhotoResult>"
    (cl:setf (cl:slot-value msg 'result) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MakePhotoResult>)))
  "Returns string type for a message object of type '<MakePhotoResult>"
  "coffebot/MakePhotoResult")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MakePhotoResult)))
  "Returns string type for a message object of type 'MakePhotoResult"
  "coffebot/MakePhotoResult")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MakePhotoResult>)))
  "Returns md5sum for a message object of type '<MakePhotoResult>"
  "eb13ac1f1354ccecb7941ee8fa2192e8")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MakePhotoResult)))
  "Returns md5sum for a message object of type 'MakePhotoResult"
  "eb13ac1f1354ccecb7941ee8fa2192e8")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MakePhotoResult>)))
  "Returns full string definition for message of type '<MakePhotoResult>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#result~%bool result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MakePhotoResult)))
  "Returns full string definition for message of type 'MakePhotoResult"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#result~%bool result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MakePhotoResult>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MakePhotoResult>))
  "Converts a ROS message object to a list"
  (cl:list 'MakePhotoResult
    (cl:cons ':result (result msg))
))
