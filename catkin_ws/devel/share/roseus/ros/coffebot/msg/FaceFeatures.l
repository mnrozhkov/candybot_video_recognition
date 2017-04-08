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
  :slots (_json_emotions _json_celebrities_similarity _json_gender _json_age ))

(defmethod coffebot::FaceFeatures
  (:init
   (&key
    ((:json_emotions __json_emotions) "")
    ((:json_celebrities_similarity __json_celebrities_similarity) "")
    ((:json_gender __json_gender) "")
    ((:json_age __json_age) "")
    )
   (send-super :init)
   (setq _json_emotions (string __json_emotions))
   (setq _json_celebrities_similarity (string __json_celebrities_similarity))
   (setq _json_gender (string __json_gender))
   (setq _json_age (string __json_age))
   self)
  (:json_emotions
   (&optional __json_emotions)
   (if __json_emotions (setq _json_emotions __json_emotions)) _json_emotions)
  (:json_celebrities_similarity
   (&optional __json_celebrities_similarity)
   (if __json_celebrities_similarity (setq _json_celebrities_similarity __json_celebrities_similarity)) _json_celebrities_similarity)
  (:json_gender
   (&optional __json_gender)
   (if __json_gender (setq _json_gender __json_gender)) _json_gender)
  (:json_age
   (&optional __json_age)
   (if __json_age (setq _json_age __json_age)) _json_age)
  (:serialization-length
   ()
   (+
    ;; string _json_emotions
    4 (length _json_emotions)
    ;; string _json_celebrities_similarity
    4 (length _json_celebrities_similarity)
    ;; string _json_gender
    4 (length _json_gender)
    ;; string _json_age
    4 (length _json_age)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _json_emotions
       (write-long (length _json_emotions) s) (princ _json_emotions s)
     ;; string _json_celebrities_similarity
       (write-long (length _json_celebrities_similarity) s) (princ _json_celebrities_similarity s)
     ;; string _json_gender
       (write-long (length _json_gender) s) (princ _json_gender s)
     ;; string _json_age
       (write-long (length _json_age) s) (princ _json_age s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _json_emotions
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _json_emotions (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _json_celebrities_similarity
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _json_celebrities_similarity (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _json_gender
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _json_gender (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _json_age
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _json_age (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get coffebot::FaceFeatures :md5sum-) "15bb16ee860ec0e7cb55bbcb7c8e05d8")
(setf (get coffebot::FaceFeatures :datatype-) "coffebot/FaceFeatures")
(setf (get coffebot::FaceFeatures :definition-)
      "string json_emotions
string json_celebrities_similarity
string json_gender
string json_age

")



(provide :coffebot/FaceFeatures "15bb16ee860ec0e7cb55bbcb7c8e05d8")


