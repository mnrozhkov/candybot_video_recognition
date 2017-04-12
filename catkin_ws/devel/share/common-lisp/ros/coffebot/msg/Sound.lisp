; Auto-generated. Do not edit!


(cl:in-package coffebot-msg)


;//! \htmlinclude Sound.msg.html

(cl:defclass <Sound> (roslisp-msg-protocol:ros-message)
  ((category
    :reader category
    :initarg :category
    :type cl:string
    :initform "")
   (name
    :reader name
    :initarg :name
    :type cl:string
    :initform ""))
)

(cl:defclass Sound (<Sound>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Sound>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Sound)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name coffebot-msg:<Sound> is deprecated: use coffebot-msg:Sound instead.")))

(cl:ensure-generic-function 'category-val :lambda-list '(m))
(cl:defmethod category-val ((m <Sound>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coffebot-msg:category-val is deprecated.  Use coffebot-msg:category instead.")
  (category m))

(cl:ensure-generic-function 'name-val :lambda-list '(m))
(cl:defmethod name-val ((m <Sound>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coffebot-msg:name-val is deprecated.  Use coffebot-msg:name instead.")
  (name m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Sound>) ostream)
  "Serializes a message object of type '<Sound>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'category))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'category))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'name))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Sound>) istream)
  "Deserializes a message object of type '<Sound>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'category) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'category) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Sound>)))
  "Returns string type for a message object of type '<Sound>"
  "coffebot/Sound")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Sound)))
  "Returns string type for a message object of type 'Sound"
  "coffebot/Sound")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Sound>)))
  "Returns md5sum for a message object of type '<Sound>"
  "edd49c676a52b2338bcc9f97439ac87c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Sound)))
  "Returns md5sum for a message object of type 'Sound"
  "edd49c676a52b2338bcc9f97439ac87c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Sound>)))
  "Returns full string definition for message of type '<Sound>"
  (cl:format cl:nil "string category~%string name~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Sound)))
  "Returns full string definition for message of type 'Sound"
  (cl:format cl:nil "string category~%string name~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Sound>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'category))
     4 (cl:length (cl:slot-value msg 'name))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Sound>))
  "Converts a ROS message object to a list"
  (cl:list 'Sound
    (cl:cons ':category (category msg))
    (cl:cons ':name (name msg))
))
