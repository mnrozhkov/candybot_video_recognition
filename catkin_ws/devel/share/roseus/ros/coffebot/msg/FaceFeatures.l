;; Auto-generated. Do not edit!


(when (boundp 'coffebot::FaceFeatures)
  (if (not (find-package "COFFEBOT"))
    (make-package "COFFEBOT"))
  (shadow 'FaceFeatures (find-package "COFFEBOT")))
(unless (find-package "COFFEBOT::FACEFEATURES")
  (make-package "COFFEBOT::FACEFEATURES"))

(in-package "ROS")
;;//! \htmlinclude FaceFeatures.msg.html


(defclass coffebot::FaceFeatures
  :super ros::object
  :slots (_emotion _celebrity_name _gender _min_age _max_age ))

(defmethod coffebot::FaceFeatures
  (:init
   (&key
    ((:emotion __emotion) "")
    ((:celebrity_name __celebrity_name) "")
    ((:gender __gender) "")
    ((:min_age __min_age) 0)
    ((:max_age __max_age) 0)
    )
   (send-super :init)
   (setq _emotion (string __emotion))
   (setq _celebrity_name (string __celebrity_name))
   (setq _gender (string __gender))
   (setq _min_age (round __min_age))
   (setq _max_age (round __max_age))
   self)
  (:emotion
   (&optional __emotion)
   (if __emotion (setq _emotion __emotion)) _emotion)
  (:celebrity_name
   (&optional __celebrity_name)
   (if __celebrity_name (setq _celebrity_name __celebrity_name)) _celebrity_name)
  (:gender
   (&optional __gender)
   (if __gender (setq _gender __gender)) _gender)
  (:min_age
   (&optional __min_age)
   (if __min_age (setq _min_age __min_age)) _min_age)
  (:max_age
   (&optional __max_age)
   (if __max_age (setq _max_age __max_age)) _max_age)
  (:serialization-length
   ()
   (+
    ;; string _emotion
    4 (length _emotion)
    ;; string _celebrity_name
    4 (length _celebrity_name)
    ;; string _gender
    4 (length _gender)
    ;; int8 _min_age
    1
    ;; int8 _max_age
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _emotion
       (write-long (length _emotion) s) (princ _emotion s)
     ;; string _celebrity_name
       (write-long (length _celebrity_name) s) (princ _celebrity_name s)
     ;; string _gender
       (write-long (length _gender) s) (princ _gender s)
     ;; int8 _min_age
       (write-byte _min_age s)
     ;; int8 _max_age
       (write-byte _max_age s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _emotion
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _emotion (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _celebrity_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _celebrity_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _gender
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _gender (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; int8 _min_age
     (setq _min_age (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _min_age 127) (setq _min_age (- _min_age 256)))
   ;; int8 _max_age
     (setq _max_age (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _max_age 127) (setq _max_age (- _max_age 256)))
   ;;
   self)
  )

(setf (get coffebot::FaceFeatures :md5sum-) "85fb5ab2d65e9fa3f5c71ae7f577d551")
(setf (get coffebot::FaceFeatures :datatype-) "coffebot/FaceFeatures")
(setf (get coffebot::FaceFeatures :definition-)
      "string emotion
string celebrity_name
string gender
int8 min_age
int8 max_age

")



(provide :coffebot/FaceFeatures "85fb5ab2d65e9fa3f5c71ae7f577d551")


