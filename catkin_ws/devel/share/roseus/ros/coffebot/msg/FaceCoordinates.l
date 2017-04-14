;; Auto-generated. Do not edit!


(when (boundp 'coffebot::FaceCoordinates)
  (if (not (find-package "COFFEBOT"))
    (make-package "COFFEBOT"))
  (shadow 'FaceCoordinates (find-package "COFFEBOT")))
(unless (find-package "COFFEBOT::FACECOORDINATES")
  (make-package "COFFEBOT::FACECOORDINATES"))

(in-package "ROS")
;;//! \htmlinclude FaceCoordinates.msg.html


(defclass coffebot::FaceCoordinates
  :super ros::object
  :slots (_x _y _w _h ))

(defmethod coffebot::FaceCoordinates
  (:init
   (&key
    ((:x __x) 0)
    ((:y __y) 0)
    ((:w __w) 0)
    ((:h __h) 0)
    )
   (send-super :init)
   (setq _x (round __x))
   (setq _y (round __y))
   (setq _w (round __w))
   (setq _h (round __h))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:w
   (&optional __w)
   (if __w (setq _w __w)) _w)
  (:h
   (&optional __h)
   (if __h (setq _h __h)) _h)
  (:serialization-length
   ()
   (+
    ;; int16 _x
    2
    ;; int16 _y
    2
    ;; int16 _w
    2
    ;; int16 _h
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int16 _x
       (write-word _x s)
     ;; int16 _y
       (write-word _y s)
     ;; int16 _w
       (write-word _w s)
     ;; int16 _h
       (write-word _h s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int16 _x
     (setq _x (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _y
     (setq _y (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _w
     (setq _w (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _h
     (setq _h (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(setf (get coffebot::FaceCoordinates :md5sum-) "829ccd7c6b3f8326d5abe6f86da52ef9")
(setf (get coffebot::FaceCoordinates :datatype-) "coffebot/FaceCoordinates")
(setf (get coffebot::FaceCoordinates :definition-)
      "#coordinates of face on some image

#left-up angle coordinates
int16 x
int16 y
#width and height of face region
int16 w
int16 h

")



(provide :coffebot/FaceCoordinates "829ccd7c6b3f8326d5abe6f86da52ef9")


