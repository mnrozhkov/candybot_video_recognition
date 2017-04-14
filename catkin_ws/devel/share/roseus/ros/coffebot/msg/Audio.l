;; Auto-generated. Do not edit!


(when (boundp 'coffebot::Audio)
  (if (not (find-package "COFFEBOT"))
    (make-package "COFFEBOT"))
  (shadow 'Audio (find-package "COFFEBOT")))
(unless (find-package "COFFEBOT::AUDIO")
  (make-package "COFFEBOT::AUDIO"))

(in-package "ROS")
;;//! \htmlinclude Audio.msg.html


(defclass coffebot::Audio
  :super ros::object
  :slots (_content ))

(defmethod coffebot::Audio
  (:init
   (&key
    ((:content __content) (make-array 0 :initial-element 0 :element-type :char))
    )
   (send-super :init)
   (setq _content __content)
   self)
  (:content
   (&optional __content)
   (if __content (setq _content __content)) _content)
  (:serialization-length
   ()
   (+
    ;; uint8[] _content
    (* 1    (length _content)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint8[] _content
     (write-long (length _content) s)
     (princ _content s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint8[] _content
   (let ((n (sys::peek buf ptr- :integer))) (incf ptr- 4)
     (setq _content (make-array n :element-type :char))
     (replace _content buf :start2 ptr-) (incf ptr- n))
   ;;
   self)
  )

(setf (get coffebot::Audio :md5sum-) "72abf3d8306e84a4caf970654ef2815d")
(setf (get coffebot::Audio :datatype-) "coffebot/Audio")
(setf (get coffebot::Audio :definition-)
      "uint8[] content

")



(provide :coffebot/Audio "72abf3d8306e84a4caf970654ef2815d")


