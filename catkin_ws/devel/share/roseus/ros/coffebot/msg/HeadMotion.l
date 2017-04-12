;; Auto-generated. Do not edit!


(when (boundp 'coffebot::HeadMotion)
  (if (not (find-package "COFFEBOT"))
    (make-package "COFFEBOT"))
  (shadow 'HeadMotion (find-package "COFFEBOT")))
(unless (find-package "COFFEBOT::HEADMOTION")
  (make-package "COFFEBOT::HEADMOTION"))

(in-package "ROS")
;;//! \htmlinclude HeadMotion.msg.html


(defclass coffebot::HeadMotion
  :super ros::object
  :slots (_h_angle _v_angle _emotion ))

(defmethod coffebot::HeadMotion
  (:init
   (&key
    ((:h_angle __h_angle) 0.0)
    ((:v_angle __v_angle) 0.0)
    ((:emotion __emotion) "")
    )
   (send-super :init)
   (setq _h_angle (float __h_angle))
   (setq _v_angle (float __v_angle))
   (setq _emotion (string __emotion))
   self)
  (:h_angle
   (&optional __h_angle)
   (if __h_angle (setq _h_angle __h_angle)) _h_angle)
  (:v_angle
   (&optional __v_angle)
   (if __v_angle (setq _v_angle __v_angle)) _v_angle)
  (:emotion
   (&optional __emotion)
   (if __emotion (setq _emotion __emotion)) _emotion)
  (:serialization-length
   ()
   (+
    ;; float32 _h_angle
    4
    ;; float32 _v_angle
    4
    ;; string _emotion
    4 (length _emotion)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _h_angle
       (sys::poke _h_angle (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _v_angle
       (sys::poke _v_angle (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; string _emotion
       (write-long (length _emotion) s) (princ _emotion s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _h_angle
     (setq _h_angle (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _v_angle
     (setq _v_angle (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; string _emotion
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _emotion (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get coffebot::HeadMotion :md5sum-) "57dac4b62b684f84f46d1dd244edf1e0")
(setf (get coffebot::HeadMotion :datatype-) "coffebot/HeadMotion")
(setf (get coffebot::HeadMotion :definition-)
      "float32 h_angle # 0.0 <= h_angle <= 360.0
float32 v_angle # 0.0 <= v_angle <= 360.0
string emotion

")



(provide :coffebot/HeadMotion "57dac4b62b684f84f46d1dd244edf1e0")


