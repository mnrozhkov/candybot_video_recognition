
(cl:in-package :asdf)

(defsystem "candybot_vr-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "VisionMessage" :depends-on ("_package_VisionMessage"))
    (:file "_package_VisionMessage" :depends-on ("_package"))
  ))