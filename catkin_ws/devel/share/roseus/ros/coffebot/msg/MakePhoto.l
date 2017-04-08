;; Auto-generated. Do not edit!


(when (boundp 'coffebot::MakePhoto)
  (if (not (find-package "COFFEBOT"))
    (make-package "COFFEBOT"))
  (shadow 'MakePhoto (find-package "COFFEBOT")))
(unless (find-package "COFFEBOT::MAKEPHOTO")
  (make-package "COFFEBOT::MAKEPHOTO"))

(in-package "ROS")
;;//! \htmlinclude MakePhoto.msg.html


(defclass coffebot::MakePhoto
  :super ros::object
  :slots (_make_photo _photo_file_name ))

(defmethod coffebot::MakePhoto
  (:init
   (&key
    ((:make_photo __make_photo) nil)
    ((:photo_file_name __photo_file_name) "")
    )
   (send-super :init)
   (setq _make_photo __make_photo)
   (setq _photo_file_name (string __photo_file_name))
   self)
  (:make_photo
   (&optional __make_photo)
   (if __make_photo (setq _make_photo __make_photo)) _make_photo)
  (:photo_file_name
   (&optional __photo_file_name)
   (if __photo_file_name (setq _photo_file_name __photo_file_name)) _photo_file_name)
  (:serialization-length
   ()
   (+
    ;; bool _make_photo
    1
    ;; string _photo_file_name
    4 (length _photo_file_name)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _make_photo
       (if _make_photo (write-byte -1 s) (write-byte 0 s))
     ;; string _photo_file_name
       (write-long (length _photo_file_name) s) (princ _photo_file_name s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _make_photo
     (setq _make_photo (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; string _photo_file_name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _photo_file_name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get coffebot::MakePhoto :md5sum-) "e0d1193fa54b08a2d5ae161d953ba3b1")
(setf (get coffebot::MakePhoto :datatype-) "coffebot/MakePhoto")
(setf (get coffebot::MakePhoto :definition-)
      "#message for command to make photo

bool make_photo
string photo_file_name

")



(provide :coffebot/MakePhoto "e0d1193fa54b08a2d5ae161d953ba3b1")


