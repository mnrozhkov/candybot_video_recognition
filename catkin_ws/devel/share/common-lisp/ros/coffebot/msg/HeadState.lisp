; Auto-generated. Do not edit!


(cl:in-package coffebot-msg)


;//! \htmlinclude HeadState.msg.html

(cl:defclass <HeadState> (roslisp-msg-protocol:ros-message)
  ((state
    :reader state
    :initarg :state
    :type coffebot-msg:HeadMotion
    :initform (cl:make-instance 'coffebot-msg:HeadMotion)))
)

(cl:defclass HeadState (<HeadState>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <HeadState>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'HeadState)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name coffebot-msg:<HeadState> is deprecated: use coffebot-msg:HeadState instead.")))

(cl:ensure-generic-function 'state-val :lambda-list '(m))
(cl:defmethod state-val ((m <HeadState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coffebot-msg:state-val is deprecated.  Use coffebot-msg:state instead.")
  (state m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <HeadState>) ostream)
  "Serializes a message object of type '<HeadState>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'state) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <HeadState>) istream)
  "Deserializes a message object of type '<HeadState>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'state) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<HeadState>)))
  "Returns string type for a message object of type '<HeadState>"
  "coffebot/HeadState")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'HeadState)))
  "Returns string type for a message object of type 'HeadState"
  "coffebot/HeadState")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<HeadState>)))
  "Returns md5sum for a message object of type '<HeadState>"
  "c6d209a024aaa61ffa06c3cc12da026d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'HeadState)))
  "Returns md5sum for a message object of type 'HeadState"
  "c6d209a024aaa61ffa06c3cc12da026d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<HeadState>)))
  "Returns full string definition for message of type '<HeadState>"
  (cl:format cl:nil "HeadMotion state~%~%================================================================================~%MSG: coffebot/HeadMotion~%float32 h_angle # 0.0 <= h_angle <= 360.0~%float32 v_angle # 0.0 <= v_angle <= 360.0~%string emotion~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'HeadState)))
  "Returns full string definition for message of type 'HeadState"
  (cl:format cl:nil "HeadMotion state~%~%================================================================================~%MSG: coffebot/HeadMotion~%float32 h_angle # 0.0 <= h_angle <= 360.0~%float32 v_angle # 0.0 <= v_angle <= 360.0~%string emotion~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <HeadState>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'state))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <HeadState>))
  "Converts a ROS message object to a list"
  (cl:list 'HeadState
    (cl:cons ':state (state msg))
))
