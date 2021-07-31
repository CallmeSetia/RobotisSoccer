// Auto-generated. Do not edit!

// (in-package kri_2021.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class KRSBI_BolaKoordinat {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.x_bola = null;
      this.y_bola = null;
      this.z_bola = null;
      this.x_pixel = null;
      this.y_pixel = null;
      this.radius = null;
    }
    else {
      if (initObj.hasOwnProperty('x_bola')) {
        this.x_bola = initObj.x_bola
      }
      else {
        this.x_bola = 0.0;
      }
      if (initObj.hasOwnProperty('y_bola')) {
        this.y_bola = initObj.y_bola
      }
      else {
        this.y_bola = 0.0;
      }
      if (initObj.hasOwnProperty('z_bola')) {
        this.z_bola = initObj.z_bola
      }
      else {
        this.z_bola = 0.0;
      }
      if (initObj.hasOwnProperty('x_pixel')) {
        this.x_pixel = initObj.x_pixel
      }
      else {
        this.x_pixel = 0;
      }
      if (initObj.hasOwnProperty('y_pixel')) {
        this.y_pixel = initObj.y_pixel
      }
      else {
        this.y_pixel = 0;
      }
      if (initObj.hasOwnProperty('radius')) {
        this.radius = initObj.radius
      }
      else {
        this.radius = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type KRSBI_BolaKoordinat
    // Serialize message field [x_bola]
    bufferOffset = _serializer.float32(obj.x_bola, buffer, bufferOffset);
    // Serialize message field [y_bola]
    bufferOffset = _serializer.float32(obj.y_bola, buffer, bufferOffset);
    // Serialize message field [z_bola]
    bufferOffset = _serializer.float32(obj.z_bola, buffer, bufferOffset);
    // Serialize message field [x_pixel]
    bufferOffset = _serializer.int16(obj.x_pixel, buffer, bufferOffset);
    // Serialize message field [y_pixel]
    bufferOffset = _serializer.int16(obj.y_pixel, buffer, bufferOffset);
    // Serialize message field [radius]
    bufferOffset = _serializer.int16(obj.radius, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type KRSBI_BolaKoordinat
    let len;
    let data = new KRSBI_BolaKoordinat(null);
    // Deserialize message field [x_bola]
    data.x_bola = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [y_bola]
    data.y_bola = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [z_bola]
    data.z_bola = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [x_pixel]
    data.x_pixel = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [y_pixel]
    data.y_pixel = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [radius]
    data.radius = _deserializer.int16(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 18;
  }

  static datatype() {
    // Returns string type for a message object
    return 'kri_2021/KRSBI_BolaKoordinat';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '6c819dfe572dd654cecc1d700d834ad7';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 x_bola
    float32 y_bola
    float32 z_bola
    int16 x_pixel
    int16 y_pixel
    int16 radius
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new KRSBI_BolaKoordinat(null);
    if (msg.x_bola !== undefined) {
      resolved.x_bola = msg.x_bola;
    }
    else {
      resolved.x_bola = 0.0
    }

    if (msg.y_bola !== undefined) {
      resolved.y_bola = msg.y_bola;
    }
    else {
      resolved.y_bola = 0.0
    }

    if (msg.z_bola !== undefined) {
      resolved.z_bola = msg.z_bola;
    }
    else {
      resolved.z_bola = 0.0
    }

    if (msg.x_pixel !== undefined) {
      resolved.x_pixel = msg.x_pixel;
    }
    else {
      resolved.x_pixel = 0
    }

    if (msg.y_pixel !== undefined) {
      resolved.y_pixel = msg.y_pixel;
    }
    else {
      resolved.y_pixel = 0
    }

    if (msg.radius !== undefined) {
      resolved.radius = msg.radius;
    }
    else {
      resolved.radius = 0
    }

    return resolved;
    }
};

module.exports = KRSBI_BolaKoordinat;
