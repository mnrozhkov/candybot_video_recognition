;; Auto-generated. Do not edit!


(when (boundp 'coffebot::HeadState)
  (if (not (find-package "COFFEBOT"))
    (make-package "COFFEBOT"))
  (shadow 'HeadState (find-package "COFFEBOT")))
(unless (find-package "COFFEBOT::HEADSTATE")
  (make-package "COFFEBOT::HEADSTATE"))

(in-package "ROS")
;;//! \htmlinclude HeadState.msg.html


(defclass coffebot::HeadState
  :super ros::object
  :slots (_state ))

(defmethod coffebot::HeadState
  (:init
   (&key
    ((:state __state) (instance coffebot::HeadMotion :init))
    )
   (send-super :init)
   (setq _state __state)
   self)
  (:state
   (&rest __state)
   (if (keywordp (car __state))
       (send* _state __state)
     (progn
       (if __state (setq _state (car __state)))
       _state)))
  (:serialization-length
   ()
   (+
    ;; coffebot/HeadMotion _state
    (send _state :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; coffebot/HeadMotion _state
       (send _state :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; coffebot/HeadMotion _state
     (send _state :deserialize buf ptr-) (incf ptr- (send _state :serialization-length))
   ;;
   self)
  )

(setf (get coffebot::HeadState :md5sum-) "c6d209a024aaa61ffa06c3cc12da026d")
(setf (get coffebot::HeadState :datatype-) "coffebot/HeadState")
(setf (get coffebot::HeadState :definition-)
      "HeadMotion state

================================================================================
MSG: coffebot/HeadMotion
float32 h_angle # 0.0 <= h_angle <= 360.0
float32 v_angle # 0.0 <= v_angle <= 360.0
string emotion

")



(provide :coffebot/HeadState "c6d209a024aaa61ffa06c3cc12da026d")


