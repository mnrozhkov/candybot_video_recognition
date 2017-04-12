; Auto-generated. Do not edit!


(cl:in-package coffebot-msg)


;//! \htmlinclude MakePhoto.msg.html

(cl:defclass <MakePhoto> (roslisp-msg-protocol:ros-message)
  ((make_photo
    :reader make_photo
    :initarg :make_photo
    :type cl:boolean
    :initform cl:nil)
   (photo_file_name
    :reader photo_file_name
    :initarg :photo_file_name
    :type cl:string
    :initform ""))
)

(cl:defclass MakePhoto (<MakePhoto>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MakePhoto>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MakePhoto)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name coffebot-msg:<MakePhoto> is deprecated: use coffebot-msg:MakePhoto instead.")))

(cl:ensure-generic-function 'make_photo-val :lambda-list '(m))
(cl:defmethod make_photo-val ((m <MakePhoto>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coffebot-msg:make_photo-val is deprecated.  Use coffebot-msg:make_photo instead.")
  (make_photo m))

(cl:ensure-generic-function 'photo_file_name-val :lambda-list '(m))
(cl:defmethod photo_file_name-val ((m <MakePhoto>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coffebot-msg:photo_file_name-val is deprecated.  Use coffebot-msg:photo_file_name instead.")
  (photo_file_name m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MakePhoto>) ostream)
  "Serializes a message object of type '<MakePhoto>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'make_photo) 1 0)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'photo_file_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'photo_file_name))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MakePhoto>) istream)
  "Deserializes a message object of type '<MakePhoto>"
    (cl:setf (cl:slot-value msg 'make_photo) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'photo_file_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'photo_file_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MakePhoto>)))
  "Returns string type for a message object of type '<MakePhoto>"
  "coffebot/MakePhoto")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MakePhoto)))
  "Returns string type for a message object of type 'MakePhoto"
  "coffebot/MakePhoto")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MakePhoto>)))
  "Returns md5sum for a message object of type '<MakePhoto>"
  "e0d1193fa54b08a2d5ae161d953ba3b1")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MakePhoto)))
  "Returns md5sum for a message object of type 'MakePhoto"
  "e0d1193fa54b08a2d5ae161d953ba3b1")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MakePhoto>)))
  "Returns full string definition for message of type '<MakePhoto>"
  (cl:format cl:nil "#message for command to make photo~%~%bool make_photo~%string photo_file_name~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MakePhoto)))
  "Returns full string definition for message of type 'MakePhoto"
  (cl:format cl:nil "#message for command to make photo~%~%bool make_photo~%string photo_file_name~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MakePhoto>))
  (cl:+ 0
     1
     4 (cl:length (cl:slot-value msg 'photo_file_name))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MakePhoto>))
  "Converts a ROS message object to a list"
  (cl:list 'MakePhoto
    (cl:cons ':make_photo (make_photo msg))
    (cl:cons ':photo_file_name (photo_file_name msg))
))
