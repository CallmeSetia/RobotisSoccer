
(cl:in-package :asdf)

(defsystem "kri_2021-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "BallState" :depends-on ("_package_BallState"))
    (:file "_package_BallState" :depends-on ("_package"))
    (:file "BolaKoordinat" :depends-on ("_package_BolaKoordinat"))
    (:file "_package_BolaKoordinat" :depends-on ("_package"))
  ))