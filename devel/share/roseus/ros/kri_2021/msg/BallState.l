;; Auto-generated. Do not edit!


(when (boundp 'kri_2021::BallState)
  (if (not (find-package "KRI_2021"))
    (make-package "KRI_2021"))
  (shadow 'BallState (find-package "KRI_2021")))
(unless (find-package "KRI_2021::BALLSTATE")
  (make-package "KRI_2021::BALLSTATE"))

(in-package "ROS")
;;//! \htmlinclude BallState.msg.html


(defclass kri_2021::BallState
  :super ros::object
  :slots (_bola_state _bola_inFrame_Pos ))

(defmethod kri_2021::BallState
  (:init
   (&key
    ((:bola_state __bola_state) nil)
    ((:bola_inFrame_Pos __bola_inFrame_Pos) "")
    )
   (send-super :init)
   (setq _bola_state __bola_state)
   (setq _bola_inFrame_Pos (string __bola_inFrame_Pos))
   self)
  (:bola_state
   (&optional __bola_state)
   (if __bola_state (setq _bola_state __bola_state)) _bola_state)
  (:bola_inFrame_Pos
   (&optional __bola_inFrame_Pos)
   (if __bola_inFrame_Pos (setq _bola_inFrame_Pos __bola_inFrame_Pos)) _bola_inFrame_Pos)
  (:serialization-length
   ()
   (+
    ;; bool _bola_state
    1
    ;; string _bola_inFrame_Pos
    4 (length _bola_inFrame_Pos)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _bola_state
       (if _bola_state (write-byte -1 s) (write-byte 0 s))
     ;; string _bola_inFrame_Pos
       (write-long (length _bola_inFrame_Pos) s) (princ _bola_inFrame_Pos s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _bola_state
     (setq _bola_state (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; string _bola_inFrame_Pos
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _bola_inFrame_Pos (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get kri_2021::BallState :md5sum-) "01006ac4b22c22b20f8ef7ceb455f461")
(setf (get kri_2021::BallState :datatype-) "kri_2021/BallState")
(setf (get kri_2021::BallState :definition-)
      "bool bola_state
string bola_inFrame_Pos


")



(provide :kri_2021/BallState "01006ac4b22c22b20f8ef7ceb455f461")


