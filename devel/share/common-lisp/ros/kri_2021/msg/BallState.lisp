; Auto-generated. Do not edit!


(cl:in-package kri_2021-msg)


;//! \htmlinclude BallState.msg.html

(cl:defclass <BallState> (roslisp-msg-protocol:ros-message)
  ((bola_state
    :reader bola_state
    :initarg :bola_state
    :type cl:boolean
    :initform cl:nil)
   (bola_inFrame_Pos
    :reader bola_inFrame_Pos
    :initarg :bola_inFrame_Pos
    :type cl:string
    :initform "")
   (last_bola_inFrame_Pos
    :reader last_bola_inFrame_Pos
    :initarg :last_bola_inFrame_Pos
    :type cl:string
    :initform ""))
)

(cl:defclass BallState (<BallState>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <BallState>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'BallState)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name kri_2021-msg:<BallState> is deprecated: use kri_2021-msg:BallState instead.")))

(cl:ensure-generic-function 'bola_state-val :lambda-list '(m))
(cl:defmethod bola_state-val ((m <BallState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kri_2021-msg:bola_state-val is deprecated.  Use kri_2021-msg:bola_state instead.")
  (bola_state m))

(cl:ensure-generic-function 'bola_inFrame_Pos-val :lambda-list '(m))
(cl:defmethod bola_inFrame_Pos-val ((m <BallState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kri_2021-msg:bola_inFrame_Pos-val is deprecated.  Use kri_2021-msg:bola_inFrame_Pos instead.")
  (bola_inFrame_Pos m))

(cl:ensure-generic-function 'last_bola_inFrame_Pos-val :lambda-list '(m))
(cl:defmethod last_bola_inFrame_Pos-val ((m <BallState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader kri_2021-msg:last_bola_inFrame_Pos-val is deprecated.  Use kri_2021-msg:last_bola_inFrame_Pos instead.")
  (last_bola_inFrame_Pos m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <BallState>) ostream)
  "Serializes a message object of type '<BallState>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'bola_state) 1 0)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'bola_inFrame_Pos))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'bola_inFrame_Pos))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'last_bola_inFrame_Pos))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'last_bola_inFrame_Pos))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <BallState>) istream)
  "Deserializes a message object of type '<BallState>"
    (cl:setf (cl:slot-value msg 'bola_state) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'bola_inFrame_Pos) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'bola_inFrame_Pos) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'last_bola_inFrame_Pos) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'last_bola_inFrame_Pos) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<BallState>)))
  "Returns string type for a message object of type '<BallState>"
  "kri_2021/BallState")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'BallState)))
  "Returns string type for a message object of type 'BallState"
  "kri_2021/BallState")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<BallState>)))
  "Returns md5sum for a message object of type '<BallState>"
  "de7a3afd02c72a42be761a1cf03a491c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'BallState)))
  "Returns md5sum for a message object of type 'BallState"
  "de7a3afd02c72a42be761a1cf03a491c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<BallState>)))
  "Returns full string definition for message of type '<BallState>"
  (cl:format cl:nil "bool bola_state~%string bola_inFrame_Pos~%string last_bola_inFrame_Pos~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'BallState)))
  "Returns full string definition for message of type 'BallState"
  (cl:format cl:nil "bool bola_state~%string bola_inFrame_Pos~%string last_bola_inFrame_Pos~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <BallState>))
  (cl:+ 0
     1
     4 (cl:length (cl:slot-value msg 'bola_inFrame_Pos))
     4 (cl:length (cl:slot-value msg 'last_bola_inFrame_Pos))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <BallState>))
  "Converts a ROS message object to a list"
  (cl:list 'BallState
    (cl:cons ':bola_state (bola_state msg))
    (cl:cons ':bola_inFrame_Pos (bola_inFrame_Pos msg))
    (cl:cons ':last_bola_inFrame_Pos (last_bola_inFrame_Pos msg))
))
