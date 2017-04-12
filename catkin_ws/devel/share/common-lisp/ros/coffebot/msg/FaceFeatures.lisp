; Auto-generated. Do not edit!


(cl:in-package coffebot-msg)


;//! \htmlinclude FaceFeatures.msg.html

(cl:defclass <FaceFeatures> (roslisp-msg-protocol:ros-message)
  ((emotion
    :reader emotion
    :initarg :emotion
    :type cl:string
    :initform "")
   (celebrity_name
    :reader celebrity_name
    :initarg :celebrity_name
    :type cl:string
    :initform "")
   (gender
    :reader gender
    :initarg :gender
    :type cl:string
    :initform "")
   (min_age
    :reader min_age
    :initarg :min_age
    :type cl:fixnum
    :initform 0)
   (max_age
    :reader max_age
    :initarg :max_age
    :type cl:fixnum
    :initform 0))
)

(cl:defclass FaceFeatures (<FaceFeatures>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <FaceFeatures>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'FaceFeatures)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name coffebot-msg:<FaceFeatures> is deprecated: use coffebot-msg:FaceFeatures instead.")))

(cl:ensure-generic-function 'emotion-val :lambda-list '(m))
(cl:defmethod emotion-val ((m <FaceFeatures>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coffebot-msg:emotion-val is deprecated.  Use coffebot-msg:emotion instead.")
  (emotion m))

(cl:ensure-generic-function 'celebrity_name-val :lambda-list '(m))
(cl:defmethod celebrity_name-val ((m <FaceFeatures>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coffebot-msg:celebrity_name-val is deprecated.  Use coffebot-msg:celebrity_name instead.")
  (celebrity_name m))

(cl:ensure-generic-function 'gender-val :lambda-list '(m))
(cl:defmethod gender-val ((m <FaceFeatures>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coffebot-msg:gender-val is deprecated.  Use coffebot-msg:gender instead.")
  (gender m))

(cl:ensure-generic-function 'min_age-val :lambda-list '(m))
(cl:defmethod min_age-val ((m <FaceFeatures>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coffebot-msg:min_age-val is deprecated.  Use coffebot-msg:min_age instead.")
  (min_age m))

(cl:ensure-generic-function 'max_age-val :lambda-list '(m))
(cl:defmethod max_age-val ((m <FaceFeatures>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coffebot-msg:max_age-val is deprecated.  Use coffebot-msg:max_age instead.")
  (max_age m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <FaceFeatures>) ostream)
  "Serializes a message object of type '<FaceFeatures>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'emotion))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'emotion))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'celebrity_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'celebrity_name))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'gender))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'gender))
  (cl:let* ((signed (cl:slot-value msg 'min_age)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'max_age)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <FaceFeatures>) istream)
  "Deserializes a message object of type '<FaceFeatures>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'emotion) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'emotion) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'celebrity_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'celebrity_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'gender) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'gender) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'min_age) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'max_age) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<FaceFeatures>)))
  "Returns string type for a message object of type '<FaceFeatures>"
  "coffebot/FaceFeatures")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'FaceFeatures)))
  "Returns string type for a message object of type 'FaceFeatures"
  "coffebot/FaceFeatures")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<FaceFeatures>)))
  "Returns md5sum for a message object of type '<FaceFeatures>"
  "85fb5ab2d65e9fa3f5c71ae7f577d551")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'FaceFeatures)))
  "Returns md5sum for a message object of type 'FaceFeatures"
  "85fb5ab2d65e9fa3f5c71ae7f577d551")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<FaceFeatures>)))
  "Returns full string definition for message of type '<FaceFeatures>"
  (cl:format cl:nil "string emotion~%string celebrity_name~%string gender~%int8 min_age~%int8 max_age~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'FaceFeatures)))
  "Returns full string definition for message of type 'FaceFeatures"
  (cl:format cl:nil "string emotion~%string celebrity_name~%string gender~%int8 min_age~%int8 max_age~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <FaceFeatures>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'emotion))
     4 (cl:length (cl:slot-value msg 'celebrity_name))
     4 (cl:length (cl:slot-value msg 'gender))
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <FaceFeatures>))
  "Converts a ROS message object to a list"
  (cl:list 'FaceFeatures
    (cl:cons ':emotion (emotion msg))
    (cl:cons ':celebrity_name (celebrity_name msg))
    (cl:cons ':gender (gender msg))
    (cl:cons ':min_age (min_age msg))
    (cl:cons ':max_age (max_age msg))
))
