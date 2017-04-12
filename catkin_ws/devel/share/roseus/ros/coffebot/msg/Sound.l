;; Auto-generated. Do not edit!


(when (boundp 'coffebot::Sound)
  (if (not (find-package "COFFEBOT"))
    (make-package "COFFEBOT"))
  (shadow 'Sound (find-package "COFFEBOT")))
(unless (find-package "COFFEBOT::SOUND")
  (make-package "COFFEBOT::SOUND"))

(in-package "ROS")
;;//! \htmlinclude Sound.msg.html


(defclass coffebot::Sound
  :super ros::object
  :slots (_category _name ))

(defmethod coffebot::Sound
  (:init
   (&key
    ((:category __category) "")
    ((:name __name) "")
    )
   (send-super :init)
   (setq _category (string __category))
   (setq _name (string __name))
   self)
  (:category
   (&optional __category)
   (if __category (setq _category __category)) _category)
  (:name
   (&optional __name)
   (if __name (setq _name __name)) _name)
  (:serialization-length
   ()
   (+
    ;; string _category
    4 (length _category)
    ;; string _name
    4 (length _name)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _category
       (write-long (length _category) s) (princ _category s)
     ;; string _name
       (write-long (length _name) s) (princ _name s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _category
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _category (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get coffebot::Sound :md5sum-) "edd49c676a52b2338bcc9f97439ac87c")
(setf (get coffebot::Sound :datatype-) "coffebot/Sound")
(setf (get coffebot::Sound :definition-)
      "string category
string name

")



(provide :coffebot/Sound "edd49c676a52b2338bcc9f97439ac87c")


