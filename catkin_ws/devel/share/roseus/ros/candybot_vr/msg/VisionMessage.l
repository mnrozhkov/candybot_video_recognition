;; Auto-generated. Do not edit!


(when (boundp 'candybot_vr::VisionMessage)
  (if (not (find-package "CANDYBOT_VR"))
    (make-package "CANDYBOT_VR"))
  (shadow 'VisionMessage (find-package "CANDYBOT_VR")))
(unless (find-package "CANDYBOT_VR::VISIONMESSAGE")
  (make-package "CANDYBOT_VR::VISIONMESSAGE"))

(in-package "ROS")
;;//! \htmlinclude VisionMessage.msg.html


(defclass candybot_vr::VisionMessage
  :super ros::object
  :slots (_face_count _smile ))

(defmethod candybot_vr::VisionMessage
  (:init
   (&key
    ((:face_count __face_count) 0)
    ((:smile __smile) nil)
    )
   (send-super :init)
   (setq _face_count (round __face_count))
   (setq _smile __smile)
   self)
  (:face_count
   (&optional __face_count)
   (if __face_count (setq _face_count __face_count)) _face_count)
  (:smile
   (&optional __smile)
   (if __smile (setq _smile __smile)) _smile)
  (:serialization-length
   ()
   (+
    ;; int32 _face_count
    4
    ;; bool _smile
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _face_count
       (write-long _face_count s)
     ;; bool _smile
       (if _smile (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _face_count
     (setq _face_count (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; bool _smile
     (setq _smile (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get candybot_vr::VisionMessage :md5sum-) "38c28f9d3b21cf8ed2fa3008fac27d63")
(setf (get candybot_vr::VisionMessage :datatype-) "candybot_vr/VisionMessage")
(setf (get candybot_vr::VisionMessage :definition-)
      "int32 face_count
bool smile

")



(provide :candybot_vr/VisionMessage "38c28f9d3b21cf8ed2fa3008fac27d63")


