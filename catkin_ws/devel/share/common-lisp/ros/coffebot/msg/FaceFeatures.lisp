; Auto-generated. Do not edit!


(cl:in-package coffebot-msg)


;//! \htmlinclude FaceFeatures.msg.html

(cl:defclass <FaceFeatures> (roslisp-msg-protocol:ros-message)
  ((json_emotions
    :reader json_emotions
    :initarg :json_emotions
    :type cl:string
    :initform "")
   (json_celebrities_similarity
    :reader json_celebrities_similarity
    :initarg :json_celebrities_similarity
    :type cl:string
    :initform "")
   (json_gender
    :reader json_gender
    :initarg :json_gender
    :type cl:string
    :initform "")
   (json_age
    :reader json_age
    :initarg :json_age
    :type cl:string
    :initform ""))
)

(cl:defclass FaceFeatures (<FaceFeatures>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <FaceFeatures>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'FaceFeatures)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name coffebot-msg:<FaceFeatures> is deprecated: use coffebot-msg:FaceFeatures instead.")))

(cl:ensure-generic-function 'json_emotions-val :lambda-list '(m))
(cl:defmethod json_emotions-val ((m <FaceFeatures>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coffebot-msg:json_emotions-val is deprecated.  Use coffebot-msg:json_emotions instead.")
  (json_emotions m))

(cl:ensure-generic-function 'json_celebrities_similarity-val :lambda-list '(m))
(cl:defmethod json_celebrities_similarity-val ((m <FaceFeatures>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coffebot-msg:json_celebrities_similarity-val is deprecated.  Use coffebot-msg:json_celebrities_similarity instead.")
  (json_celebrities_similarity m))

(cl:ensure-generic-function 'json_gender-val :lambda-list '(m))
(cl:defmethod json_gender-val ((m <FaceFeatures>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coffebot-msg:json_gender-val is deprecated.  Use coffebot-msg:json_gender instead.")
  (json_gender m))

(cl:ensure-generic-function 'json_age-val :lambda-list '(m))
(cl:defmethod json_age-val ((m <FaceFeatures>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coffebot-msg:json_age-val is deprecated.  Use coffebot-msg:json_age instead.")
  (json_age m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <FaceFeatures>) ostream)
  "Serializes a message object of type '<FaceFeatures>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'json_emotions))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'json_emotions))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'json_celebrities_similarity))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'json_celebrities_similarity))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'json_gender))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'json_gender))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'json_age))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'json_age))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <FaceFeatures>) istream)
  "Deserializes a message object of type '<FaceFeatures>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'json_emotions) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'json_emotions) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'json_celebrities_similarity) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'json_celebrities_similarity) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'json_gender) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'json_gender) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'json_age) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'json_age) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
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
  "15bb16ee860ec0e7cb55bbcb7c8e05d8")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'FaceFeatures)))
  "Returns md5sum for a message object of type 'FaceFeatures"
  "15bb16ee860ec0e7cb55bbcb7c8e05d8")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<FaceFeatures>)))
  "Returns full string definition for message of type '<FaceFeatures>"
  (cl:format cl:nil "string json_emotions~%string json_celebrities_similarity~%string json_gender~%string json_age~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'FaceFeatures)))
  "Returns full string definition for message of type 'FaceFeatures"
  (cl:format cl:nil "string json_emotions~%string json_celebrities_similarity~%string json_gender~%string json_age~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <FaceFeatures>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'json_emotions))
     4 (cl:length (cl:slot-value msg 'json_celebrities_similarity))
     4 (cl:length (cl:slot-value msg 'json_gender))
     4 (cl:length (cl:slot-value msg 'json_age))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <FaceFeatures>))
  "Converts a ROS message object to a list"
  (cl:list 'FaceFeatures
    (cl:cons ':json_emotions (json_emotions msg))
    (cl:cons ':json_celebrities_similarity (json_celebrities_similarity msg))
    (cl:cons ':json_gender (json_gender msg))
    (cl:cons ':json_age (json_age msg))
))
