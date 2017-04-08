;; Auto-generated. Do not edit!


(when (boundp 'coffebot::BotSpeechText)
  (if (not (find-package "COFFEBOT"))
    (make-package "COFFEBOT"))
  (shadow 'BotSpeechText (find-package "COFFEBOT")))
(unless (find-package "COFFEBOT::BOTSPEECHTEXT")
  (make-package "COFFEBOT::BOTSPEECHTEXT"))

(in-package "ROS")
;;//! \htmlinclude BotSpeechText.msg.html


(defclass coffebot::BotSpeechText
  :super ros::object
  :slots (_text ))

(defmethod coffebot::BotSpeechText
  (:init
   (&key
    ((:text __text) "")
    )
   (send-super :init)
   (setq _text (string __text))
   self)
  (:text
   (&optional __text)
   (if __text (setq _text __text)) _text)
  (:serialization-length
   ()
   (+
    ;; string _text
    4 (length _text)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _text
       (write-long (length _text) s) (princ _text s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _text
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _text (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get coffebot::BotSpeechText :md5sum-) "74697ed3d931f6eede8bf3a8dfeca160")
(setf (get coffebot::BotSpeechText :datatype-) "coffebot/BotSpeechText")
(setf (get coffebot::BotSpeechText :definition-)
      "string text

")



(provide :coffebot/BotSpeechText "74697ed3d931f6eede8bf3a8dfeca160")


