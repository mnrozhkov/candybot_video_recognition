;; Auto-generated. Do not edit!


(when (boundp 'coffebot::APIAIBotAnswer)
  (if (not (find-package "COFFEBOT"))
    (make-package "COFFEBOT"))
  (shadow 'APIAIBotAnswer (find-package "COFFEBOT")))
(unless (find-package "COFFEBOT::APIAIBOTANSWER")
  (make-package "COFFEBOT::APIAIBOTANSWER"))

(in-package "ROS")
;;//! \htmlinclude APIAIBotAnswer.msg.html


(defclass coffebot::APIAIBotAnswer
  :super ros::object
  :slots (_text _action_name _action_parameters_in_json ))

(defmethod coffebot::APIAIBotAnswer
  (:init
   (&key
    ((:text __text) "")
    ((:action_name __action_name) "")
    ((:action_parameters_in_json __action_parameters_in_json) "")
    )
   (send-super :init)
   (setq _text (string __text))
   (setq _action_name (string __action_name))
   (setq _action_parameters_in_json (string __action_parameters_in_json))
   self)
  (:text
   (&optional __text)
   (if __text (setq _text __text)) _text)
  (:action_name
   (&optional __action_name)
   (if __action_name (setq _action_name __action_name)) _action_name)
  (:action_parameters_in_json
   (&optional __action_parameters_in_json)
   (if __action_parameters_in_json (setq _action_parameters_in_json __action_parameters_in_json)) _action_parameters_in_json)
  (:serialization-length
   ()
   (+
    ;; string _text
    4 (length _text)
    ;; string _action_name
    4 (length _action_name)
    ;; string _action_parameters_in_json
    4 (length _action_parameters_in_json)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _text
       (write-long (length _text) s) (princ _text s)
     ;; string _action_name
       (write-long (length _action_name) s) (princ _action_name s)
     ;; string _action_parameters_in_json
       (write-long (length _action_parameters_in_json) s) (princ _action_parameters_in_json s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _text
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _text (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _action_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _action_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _action_parameters_in_json
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _action_parameters_in_json (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get coffebot::APIAIBotAnswer :md5sum-) "d9356e8a4f86a7632a7fb741a0ba9d22")
(setf (get coffebot::APIAIBotAnswer :datatype-) "coffebot/APIAIBotAnswer")
(setf (get coffebot::APIAIBotAnswer :definition-)
      "string text
string action_name
string action_parameters_in_json

")



(provide :coffebot/APIAIBotAnswer "d9356e8a4f86a7632a7fb741a0ba9d22")


