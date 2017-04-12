// Auto-generated. Do not edit!

// (in-package coffebot.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let HeadMotion = require('./HeadMotion.js');

//-----------------------------------------------------------

class HeadState {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.state = null;
    }
    else {
      if (initObj.hasOwnProperty('state')) {
        this.state = initObj.state
      }
      else {
        this.state = new HeadMotion();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type HeadState
    // Serialize message field [state]
    bufferOffset = HeadMotion.serialize(obj.state, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type HeadState
    let len;
    let data = new HeadState(null);
    // Deserialize message field [state]
    data.state = HeadMotion.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += HeadMotion.getMessageSize(object.state);
    return length;
  }

  static datatype() {
    // Returns string type for a message object
    return 'coffebot/HeadState';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c6d209a024aaa61ffa06c3cc12da026d';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    HeadMotion state
    
    ================================================================================
    MSG: coffebot/HeadMotion
    float32 h_angle # 0.0 <= h_angle <= 360.0
    float32 v_angle # 0.0 <= v_angle <= 360.0
    string emotion
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new HeadState(null);
    if (msg.state !== undefined) {
      resolved.state = HeadMotion.Resolve(msg.state)
    }
    else {
      resolved.state = new HeadMotion()
    }

    return resolved;
    }
};

module.exports = HeadState;
