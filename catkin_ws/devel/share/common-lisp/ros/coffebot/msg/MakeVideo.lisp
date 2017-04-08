; Auto-generated. Do not edit!


(cl:in-package coffebot-msg)


;//! \htmlinclude MakeVideo.msg.html

(cl:defclass <MakeVideo> (roslisp-msg-protocol:ros-message)
  ((start_video
    :reader start_video
    :initarg :start_video
    :type cl:boolean
    :initform cl:nil)
   (duration
    :reader duration
    :initarg :duration
    :type cl:fixnum
    :initform 0)
   (video_file_name
    :reader video_file_name
    :initarg :video_file_name
    :type cl:string
    :initform ""))
)

(cl:defclass MakeVideo (<MakeVideo>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MakeVideo>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MakeVideo)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name coffebot-msg:<MakeVideo> is deprecated: use coffebot-msg:MakeVideo instead.")))

(cl:ensure-generic-function 'start_video-val :lambda-list '(m))
(cl:defmethod start_video-val ((m <MakeVideo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coffebot-msg:start_video-val is deprecated.  Use coffebot-msg:start_video instead.")
  (start_video m))

(cl:ensure-generic-function 'duration-val :lambda-list '(m))
(cl:defmethod duration-val ((m <MakeVideo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coffebot-msg:duration-val is deprecated.  Use coffebot-msg:duration instead.")
  (duration m))

(cl:ensure-generic-function 'video_file_name-val :lambda-list '(m))
(cl:defmethod video_file_name-val ((m <MakeVideo>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coffebot-msg:video_file_name-val is deprecated.  Use coffebot-msg:video_file_name instead.")
  (video_file_name m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MakeVideo>) ostream)
  "Serializes a message object of type '<MakeVideo>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'start_video) 1 0)) ostream)
  (cl:let* ((signed (cl:slot-value msg 'duration)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'video_file_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'video_file_name))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MakeVideo>) istream)
  "Deserializes a message object of type '<MakeVideo>"
    (cl:setf (cl:slot-value msg 'start_video) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'duration) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'video_file_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'video_file_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MakeVideo>)))
  "Returns string type for a message object of type '<MakeVideo>"
  "coffebot/MakeVideo")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MakeVideo)))
  "Returns string type for a message object of type 'MakeVideo"
  "coffebot/MakeVideo")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MakeVideo>)))
  "Returns md5sum for a message object of type '<MakeVideo>"
  "ea5c471bcc115e3b226da65d49ceb188")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MakeVideo)))
  "Returns md5sum for a message object of type 'MakeVideo"
  "ea5c471bcc115e3b226da65d49ceb188")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MakeVideo>)))
  "Returns full string definition for message of type '<MakeVideo>"
  (cl:format cl:nil "#message for command to make video~%~%bool start_video~%int8 duration #duration in seconds~%string video_file_name~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MakeVideo)))
  "Returns full string definition for message of type 'MakeVideo"
  (cl:format cl:nil "#message for command to make video~%~%bool start_video~%int8 duration #duration in seconds~%string video_file_name~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MakeVideo>))
  (cl:+ 0
     1
     1
     4 (cl:length (cl:slot-value msg 'video_file_name))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MakeVideo>))
  "Converts a ROS message object to a list"
  (cl:list 'MakeVideo
    (cl:cons ':start_video (start_video msg))
    (cl:cons ':duration (duration msg))
    (cl:cons ':video_file_name (video_file_name msg))
))
