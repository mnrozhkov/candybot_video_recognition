;; Auto-generated. Do not edit!


(when (boundp 'coffebot::Emotion)
  (if (not (find-package "COFFEBOT"))
    (make-package "COFFEBOT"))
  (shadow 'Emotion (find-package "COFFEBOT")))
(unless (find-package "COFFEBOT::EMOTION")
  (make-package "COFFEBOT::EMOTION"))

(in-package "ROS")
;;//! \htmlinclude Emotion.msg.html


(defclass coffebot::Emotion
  :super ros::object
  :slots (_name ))

(defmethod coffebot::Emotion
  (:init
   (&key
    ((:name __name) "")
    )
   (send-super :init)
   (setq _name (string __name))
   self)
  (:name
   (&optional __name)
   (if __name (setq _name __name)) _name)
  (:serialization-length
   ()
   (+
    ;; string _name
    4 (length _name)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _name
       (write-long (length _name) s) (princ _name s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get coffebot::Emotion :md5sum-) "c1f3d28f1b044c871e6eff2e9fc3c667")
(setf (get coffebot::Emotion :datatype-) "coffebot/Emotion")
(setf (get coffebot::Emotion :definition-)
      "string name

")



(provide :coffebot/Emotion "c1f3d28f1b044c871e6eff2e9fc3c667")


