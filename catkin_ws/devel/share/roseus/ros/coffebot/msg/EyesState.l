;; Auto-generated. Do not edit!


(when (boundp 'coffebot::EyesState)
  (if (not (find-package "COFFEBOT"))
    (make-package "COFFEBOT"))
  (shadow 'EyesState (find-package "COFFEBOT")))
(unless (find-package "COFFEBOT::EYESSTATE")
  (make-package "COFFEBOT::EYESSTATE"))

(in-package "ROS")
;;//! \htmlinclude EyesState.msg.html


(defclass coffebot::EyesState
  :super ros::object
  :slots (_x _y _emotion ))

(defmethod coffebot::EyesState
  (:init
   (&key
    ((:x __x) 0)
    ((:y __y) 0)
    ((:emotion __emotion) "")
    )
   (send-super :init)
   (setq _x (round __x))
   (setq _y (round __y))
   (setq _emotion (string __emotion))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:emotion
   (&optional __emotion)
   (if __emotion (setq _emotion __emotion)) _emotion)
  (:serialization-length
   ()
   (+
    ;; int8 _x
    1
    ;; int8 _y
    1
    ;; string _emotion
    4 (length _emotion)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int8 _x
       (write-byte _x s)
     ;; int8 _y
       (write-byte _y s)
     ;; string _emotion
       (write-long (length _emotion) s) (princ _emotion s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int8 _x
     (setq _x (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _x 127) (setq _x (- _x 256)))
   ;; int8 _y
     (setq _y (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _y 127) (setq _y (- _y 256)))
   ;; string _emotion
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _emotion (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get coffebot::EyesState :md5sum-) "bcfd694b6a681b718890867e9439c098")
(setf (get coffebot::EyesState :datatype-) "coffebot/EyesState")
(setf (get coffebot::EyesState :definition-)
      "int8 x
int8 y
string emotion

")



(provide :coffebot/EyesState "bcfd694b6a681b718890867e9439c098")


