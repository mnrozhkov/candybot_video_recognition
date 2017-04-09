;; Auto-generated. Do not edit!


(when (boundp 'coffebot::EyesMotion)
  (if (not (find-package "COFFEBOT"))
    (make-package "COFFEBOT"))
  (shadow 'EyesMotion (find-package "COFFEBOT")))
(unless (find-package "COFFEBOT::EYESMOTION")
  (make-package "COFFEBOT::EYESMOTION"))

(in-package "ROS")
;;//! \htmlinclude EyesMotion.msg.html


(defclass coffebot::EyesMotion
  :super ros::object
  :slots (_angle _distance_from_center_percent _emotion ))

(defmethod coffebot::EyesMotion
  (:init
   (&key
    ((:angle __angle) 0.0)
    ((:distance_from_center_percent __distance_from_center_percent) 0.0)
    ((:emotion __emotion) "")
    )
   (send-super :init)
   (setq _angle (float __angle))
   (setq _distance_from_center_percent (float __distance_from_center_percent))
   (setq _emotion (string __emotion))
   self)
  (:angle
   (&optional __angle)
   (if __angle (setq _angle __angle)) _angle)
  (:distance_from_center_percent
   (&optional __distance_from_center_percent)
   (if __distance_from_center_percent (setq _distance_from_center_percent __distance_from_center_percent)) _distance_from_center_percent)
  (:emotion
   (&optional __emotion)
   (if __emotion (setq _emotion __emotion)) _emotion)
  (:serialization-length
   ()
   (+
    ;; float32 _angle
    4
    ;; float32 _distance_from_center_percent
    4
    ;; string _emotion
    4 (length _emotion)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _angle
       (sys::poke _angle (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _distance_from_center_percent
       (sys::poke _distance_from_center_percent (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; string _emotion
       (write-long (length _emotion) s) (princ _emotion s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _angle
     (setq _angle (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _distance_from_center_percent
     (setq _distance_from_center_percent (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; string _emotion
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _emotion (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get coffebot::EyesMotion :md5sum-) "0a9c274e737c0b917a24ecaa2a12792e")
(setf (get coffebot::EyesMotion :datatype-) "coffebot/EyesMotion")
(setf (get coffebot::EyesMotion :definition-)
      "float32 angle
float32 distance_from_center_percent
string emotion

")



(provide :coffebot/EyesMotion "0a9c274e737c0b917a24ecaa2a12792e")


