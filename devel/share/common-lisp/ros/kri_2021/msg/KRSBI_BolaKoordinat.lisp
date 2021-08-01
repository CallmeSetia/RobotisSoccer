; Auto-generated. Do not edit!


(cl:in-package kri_2021-msg)


;//! \htmlinclude KRSBI_BolaKoordinat.msg.html

(cl:defclass <KRSBI_BolaKoordinat> (roslisp-msg-protocol:ros-message)
  ((x_bola
    :reader x_bola
    :initarg :x_bola
    :type cl:float
    :initform 0.0)
   (y_bola
    :reader y_bola
    :initarg :y_bola
    :type cl:float
    :initform 0.0)
   (z_bola
    :reader z_bola
    :initarg :z_bola
    :type cl:float
    :initform 0.0)
   (x_pixel
    :reader x_pixel
    :initarg :x_pixel
    :type cl:fixnum
    :initform 0)
   (y_pixel
    :reader y_pixel
    :initarg :y_pixel
    :type cl:fixnum
    :initform 0)
   (radius
    :reader radius
    :initarg :radius
    :type cl:fixnum
    :initform 0))
)

(cl:defclass KRSBI_BolaKoordinat (<KRSBI_BolaKoordinat>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <KRSBI_BolaKoordinat>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'KRSBI_BolaKoordinat)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name kri_2021-msg:<KRSBI_BolaKoordinat> is deprecated: use kri_2021-msg:KRSBI_BolaKoordinat instead.")))

(cl:ensure-generic-function 'x_bola-val :lambda-list '(m))
(cl:defmethod x_bola-val ((m <KRSBI_BolaKoordinat>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kri_2021-msg:x_bola-val is deprecated.  Use kri_2021-msg:x_bola instead.")
  (x_bola m))

(cl:ensure-generic-function 'y_bola-val :lambda-list '(m))
(cl:defmethod y_bola-val ((m <KRSBI_BolaKoordinat>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kri_2021-msg:y_bola-val is deprecated.  Use kri_2021-msg:y_bola instead.")
  (y_bola m))

(cl:ensure-generic-function 'z_bola-val :lambda-list '(m))
(cl:defmethod z_bola-val ((m <KRSBI_BolaKoordinat>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kri_2021-msg:z_bola-val is deprecated.  Use kri_2021-msg:z_bola instead.")
  (z_bola m))

(cl:ensure-generic-function 'x_pixel-val :lambda-list '(m))
(cl:defmethod x_pixel-val ((m <KRSBI_BolaKoordinat>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kri_2021-msg:x_pixel-val is deprecated.  Use kri_2021-msg:x_pixel instead.")
  (x_pixel m))

(cl:ensure-generic-function 'y_pixel-val :lambda-list '(m))
(cl:defmethod y_pixel-val ((m <KRSBI_BolaKoordinat>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kri_2021-msg:y_pixel-val is deprecated.  Use kri_2021-msg:y_pixel instead.")
  (y_pixel m))

(cl:ensure-generic-function 'radius-val :lambda-list '(m))
(cl:defmethod radius-val ((m <KRSBI_BolaKoordinat>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kri_2021-msg:radius-val is deprecated.  Use kri_2021-msg:radius instead.")
  (radius m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <KRSBI_BolaKoordinat>) ostream)
  "Serializes a message object of type '<KRSBI_BolaKoordinat>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'x_bola))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'y_bola))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'z_bola))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let* ((signed (cl:slot-value msg 'x_pixel)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'y_pixel)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'radius)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <KRSBI_BolaKoordinat>) istream)
  "Deserializes a message object of type '<KRSBI_BolaKoordinat>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x_bola) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y_bola) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'z_bola) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'x_pixel) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'y_pixel) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'radius) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<KRSBI_BolaKoordinat>)))
  "Returns string type for a message object of type '<KRSBI_BolaKoordinat>"
  "kri_2021/KRSBI_BolaKoordinat")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'KRSBI_BolaKoordinat)))
  "Returns string type for a message object of type 'KRSBI_BolaKoordinat"
  "kri_2021/KRSBI_BolaKoordinat")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<KRSBI_BolaKoordinat>)))
  "Returns md5sum for a message object of type '<KRSBI_BolaKoordinat>"
  "6c819dfe572dd654cecc1d700d834ad7")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'KRSBI_BolaKoordinat)))
  "Returns md5sum for a message object of type 'KRSBI_BolaKoordinat"
  "6c819dfe572dd654cecc1d700d834ad7")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<KRSBI_BolaKoordinat>)))
  "Returns full string definition for message of type '<KRSBI_BolaKoordinat>"
  (cl:format cl:nil "float32 x_bola~%float32 y_bola~%float32 z_bola~%int16 x_pixel~%int16 y_pixel~%int16 radius~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'KRSBI_BolaKoordinat)))
  "Returns full string definition for message of type 'KRSBI_BolaKoordinat"
  (cl:format cl:nil "float32 x_bola~%float32 y_bola~%float32 z_bola~%int16 x_pixel~%int16 y_pixel~%int16 radius~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <KRSBI_BolaKoordinat>))
  (cl:+ 0
     4
     4
     4
     2
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <KRSBI_BolaKoordinat>))
  "Converts a ROS message object to a list"
  (cl:list 'KRSBI_BolaKoordinat
    (cl:cons ':x_bola (x_bola msg))
    (cl:cons ':y_bola (y_bola msg))
    (cl:cons ':z_bola (z_bola msg))
    (cl:cons ':x_pixel (x_pixel msg))
    (cl:cons ':y_pixel (y_pixel msg))
    (cl:cons ':radius (radius msg))
))
