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

class BallState {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.bola_state = null;
      this.bola_inFrame_Pos = null;
      this.last_bola_inFrame_Pos = null;
    }
    else {
      if (initObj.hasOwnProperty('bola_state')) {
        this.bola_state = initObj.bola_state
      }
      else {
        this.bola_state = false;
      }
      if (initObj.hasOwnProperty('bola_inFrame_Pos')) {
        this.bola_inFrame_Pos = initObj.bola_inFrame_Pos
      }
      else {
        this.bola_inFrame_Pos = '';
      }
      if (initObj.hasOwnProperty('last_bola_inFrame_Pos')) {
        this.last_bola_inFrame_Pos = initObj.last_bola_inFrame_Pos
      }
      else {
        this.last_bola_inFrame_Pos = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type BallState
    // Serialize message field [bola_state]
    bufferOffset = _serializer.bool(obj.bola_state, buffer, bufferOffset);
    // Serialize message field [bola_inFrame_Pos]
    bufferOffset = _serializer.string(obj.bola_inFrame_Pos, buffer, bufferOffset);
    // Serialize message field [last_bola_inFrame_Pos]
    bufferOffset = _serializer.string(obj.last_bola_inFrame_Pos, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type BallState
    let len;
    let data = new BallState(null);
    // Deserialize message field [bola_state]
    data.bola_state = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [bola_inFrame_Pos]
    data.bola_inFrame_Pos = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [last_bola_inFrame_Pos]
    data.last_bola_inFrame_Pos = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.bola_inFrame_Pos.length;
    length += object.last_bola_inFrame_Pos.length;
    return length + 9;
  }

  static datatype() {
    // Returns string type for a message object
    return 'kri_2021/BallState';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'de7a3afd02c72a42be761a1cf03a491c';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool bola_state
    string bola_inFrame_Pos
    string last_bola_inFrame_Pos
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new BallState(null);
    if (msg.bola_state !== undefined) {
      resolved.bola_state = msg.bola_state;
    }
    else {
      resolved.bola_state = false
    }

    if (msg.bola_inFrame_Pos !== undefined) {
      resolved.bola_inFrame_Pos = msg.bola_inFrame_Pos;
    }
    else {
      resolved.bola_inFrame_Pos = ''
    }

    if (msg.last_bola_inFrame_Pos !== undefined) {
      resolved.last_bola_inFrame_Pos = msg.last_bola_inFrame_Pos;
    }
    else {
      resolved.last_bola_inFrame_Pos = ''
    }

    return resolved;
    }
};

module.exports = BallState;
