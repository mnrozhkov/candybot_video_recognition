;; Auto-generated. Do not edit!


(when (boundp 'coffebot::MakeVideo)
  (if (not (find-package "COFFEBOT"))
    (make-package "COFFEBOT"))
  (shadow 'MakeVideo (find-package "COFFEBOT")))
(unless (find-package "COFFEBOT::MAKEVIDEO")
  (make-package "COFFEBOT::MAKEVIDEO"))

(in-package "ROS")
;;//! \htmlinclude MakeVideo.msg.html


(defclass coffebot::MakeVideo
  :super ros::object
  :slots (_start_video _duration _video_file_name ))

(defmethod coffebot::MakeVideo
  (:init
   (&key
    ((:start_video __start_video) nil)
    ((:duration __duration) 0)
    ((:video_file_name __video_file_name) "")
    )
   (send-super :init)
   (setq _start_video __start_video)
   (setq _duration (round __duration))
   (setq _video_file_name (string __video_file_name))
   self)
  (:start_video
   (&optional __start_video)
   (if __start_video (setq _start_video __start_video)) _start_video)
  (:duration
   (&optional __duration)
   (if __duration (setq _duration __duration)) _duration)
  (:video_file_name
   (&optional __video_file_name)
   (if __video_file_name (setq _video_file_name __video_file_name)) _video_file_name)
  (:serialization-length
   ()
   (+
    ;; bool _start_video
    1
    ;; int8 _duration
    1
    ;; string _video_file_name
    4 (length _video_file_name)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _start_video
       (if _start_video (write-byte -1 s) (write-byte 0 s))
     ;; int8 _duration
       (write-byte _duration s)
     ;; string _video_file_name
       (write-long (length _video_file_name) s) (princ _video_file_name s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _start_video
     (setq _start_video (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; int8 _duration
     (setq _duration (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _duration 127) (setq _duration (- _duration 256)))
   ;; string _video_file_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _video_file_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get coffebot::MakeVideo :md5sum-) "ea5c471bcc115e3b226da65d49ceb188")
(setf (get coffebot::MakeVideo :datatype-) "coffebot/MakeVideo")
(setf (get coffebot::MakeVideo :definition-)
      "#message for command to make video

bool start_video
int8 duration #duration in seconds
string video_file_name

")



(provide :coffebot/MakeVideo "ea5c471bcc115e3b226da65d49ceb188")


