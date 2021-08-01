;; Auto-generated. Do not edit!


(when (boundp 'kri_2021::BolaKoordinat)
  (if (not (find-package "KRI_2021"))
    (make-package "KRI_2021"))
  (shadow 'BolaKoordinat (find-package "KRI_2021")))
(unless (find-package "KRI_2021::BOLAKOORDINAT")
  (make-package "KRI_2021::BOLAKOORDINAT"))

(in-package "ROS")
;;//! \htmlinclude BolaKoordinat.msg.html


(defclass kri_2021::BolaKoordinat
  :super ros::object
  :slots (_x_bola _y_bola _z_bola _x_pixel _y_pixel _radius ))

(defmethod kri_2021::BolaKoordinat
  (:init
   (&key
    ((:x_bola __x_bola) 0.0)
    ((:y_bola __y_bola) 0.0)
    ((:z_bola __z_bola) 0.0)
    ((:x_pixel __x_pixel) 0)
    ((:y_pixel __y_pixel) 0)
    ((:radius __radius) 0)
    )
   (send-super :init)
   (setq _x_bola (float __x_bola))
   (setq _y_bola (float __y_bola))
   (setq _z_bola (float __z_bola))
   (setq _x_pixel (round __x_pixel))
   (setq _y_pixel (round __y_pixel))
   (setq _radius (round __radius))
   self)
  (:x_bola
   (&optional __x_bola)
   (if __x_bola (setq _x_bola __x_bola)) _x_bola)
  (:y_bola
   (&optional __y_bola)
   (if __y_bola (setq _y_bola __y_bola)) _y_bola)
  (:z_bola
   (&optional __z_bola)
   (if __z_bola (setq _z_bola __z_bola)) _z_bola)
  (:x_pixel
   (&optional __x_pixel)
   (if __x_pixel (setq _x_pixel __x_pixel)) _x_pixel)
  (:y_pixel
   (&optional __y_pixel)
   (if __y_pixel (setq _y_pixel __y_pixel)) _y_pixel)
  (:radius
   (&optional __radius)
   (if __radius (setq _radius __radius)) _radius)
  (:serialization-length
   ()
   (+
    ;; float32 _x_bola
    4
    ;; float32 _y_bola
    4
    ;; float32 _z_bola
    4
    ;; int16 _x_pixel
    2
    ;; int16 _y_pixel
    2
    ;; int16 _radius
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _x_bola
       (sys::poke _x_bola (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _y_bola
       (sys::poke _y_bola (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _z_bola
       (sys::poke _z_bola (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; int16 _x_pixel
       (write-word _x_pixel s)
     ;; int16 _y_pixel
       (write-word _y_pixel s)
     ;; int16 _radius
       (write-word _radius s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _x_bola
     (setq _x_bola (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _y_bola
     (setq _y_bola (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _z_bola
     (setq _z_bola (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; int16 _x_pixel
     (setq _x_pixel (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _y_pixel
     (setq _y_pixel (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _radius
     (setq _radius (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(setf (get kri_2021::BolaKoordinat :md5sum-) "6c819dfe572dd654cecc1d700d834ad7")
(setf (get kri_2021::BolaKoordinat :datatype-) "kri_2021/BolaKoordinat")
(setf (get kri_2021::BolaKoordinat :definition-)
      "float32 x_bola
float32 y_bola
float32 z_bola
int16 x_pixel
int16 y_pixel
int16 radius

")



(provide :kri_2021/BolaKoordinat "6c819dfe572dd654cecc1d700d834ad7")


