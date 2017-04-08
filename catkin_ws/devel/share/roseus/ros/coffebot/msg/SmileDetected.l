;; Auto-generated. Do not edit!


(when (boundp 'coffebot::SmileDetected)
  (if (not (find-package "COFFEBOT"))
    (make-package "COFFEBOT"))
  (shadow 'SmileDetected (find-package "COFFEBOT")))
(unless (find-package "COFFEBOT::SMILEDETECTED")
  (make-package "COFFEBOT::SMILEDETECTED"))

(in-package "ROS")
;;//! \htmlinclude SmileDetected.msg.html


(defclass coffebot::SmileDetected
  :super ros::object
  :slots (_detected ))

(defmethod coffebot::SmileDetected
  (:init
   (&key
    ((:detected __detected) nil)
    )
   (send-super :init)
   (setq _detected __detected)
   self)
  (:detected
   (&optional __detected)
   (if __detected (setq _detected __detected)) _detected)
  (:serialization-length
   ()
   (+
    ;; bool _detected
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _detected
       (if _detected (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _detected
     (setq _detected (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get coffebot::SmileDetected :md5sum-) "2d8633c53221d40413712b55b8360a15")
(setf (get coffebot::SmileDetected :datatype-) "coffebot/SmileDetected")
(setf (get coffebot::SmileDetected :definition-)
      "bool detected

")



(provide :coffebot/SmileDetected "2d8633c53221d40413712b55b8360a15")


