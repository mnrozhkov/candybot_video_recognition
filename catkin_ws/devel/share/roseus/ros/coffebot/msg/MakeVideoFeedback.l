;; Auto-generated. Do not edit!


(when (boundp 'coffebot::MakeVideoFeedback)
  (if (not (find-package "COFFEBOT"))
    (make-package "COFFEBOT"))
  (shadow 'MakeVideoFeedback (find-package "COFFEBOT")))
(unless (find-package "COFFEBOT::MAKEVIDEOFEEDBACK")
  (make-package "COFFEBOT::MAKEVIDEOFEEDBACK"))

(in-package "ROS")
;;//! \htmlinclude MakeVideoFeedback.msg.html


(defclass coffebot::MakeVideoFeedback
  :super ros::object
  :slots ())

(defmethod coffebot::MakeVideoFeedback
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(setf (get coffebot::MakeVideoFeedback :md5sum-) "d41d8cd98f00b204e9800998ecf8427e")
(setf (get coffebot::MakeVideoFeedback :datatype-) "coffebot/MakeVideoFeedback")
(setf (get coffebot::MakeVideoFeedback :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
#feedback


")



(provide :coffebot/MakeVideoFeedback "d41d8cd98f00b204e9800998ecf8427e")

