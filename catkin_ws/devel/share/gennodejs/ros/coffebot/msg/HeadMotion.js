// Auto-generated. Do not edit!

// (in-package coffebot.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class HeadMotion {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.h_angle = null;
      this.v_angle = null;
      this.emotion = null;
    }
    else {
      if (initObj.hasOwnProperty('h_angle')) {
        this.h_angle = initObj.h_angle
      }
      else {
        this.h_angle = 0.0;
      }
      if (initObj.hasOwnProperty('v_angle')) {
        this.v_angle = initObj.v_angle
      }
      else {
        this.v_angle = 0.0;
      }
      if (initObj.hasOwnProperty('emotion')) {
        this.emotion = initObj.emotion
      }
      else {
        this.emotion = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type HeadMotion
    // Serialize message field [h_angle]
    bufferOffset = _serializer.float32(obj.h_angle, buffer, bufferOffset);
    // Serialize message field [v_angle]
    bufferOffset = _serializer.float32(obj.v_angle, buffer, bufferOffset);
    // Serialize message field [emotion]
    bufferOffset = _serializer.string(obj.emotion, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type HeadMotion
    let len;
    let data = new HeadMotion(null);
    // Deserialize message field [h_angle]
    data.h_angle = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [v_angle]
    data.v_angle = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [emotion]
    data.emotion = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.emotion.length;
    return length + 12;
  }

  static datatype() {
    // Returns string type for a message object
    return 'coffebot/HeadMotion';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '57dac4b62b684f84f46d1dd244edf1e0';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
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
    const resolved = new HeadMotion(null);
    if (msg.h_angle !== undefined) {
      resolved.h_angle = msg.h_angle;
    }
    else {
      resolved.h_angle = 0.0
    }

    if (msg.v_angle !== undefined) {
      resolved.v_angle = msg.v_angle;
    }
    else {
      resolved.v_angle = 0.0
    }

    if (msg.emotion !== undefined) {
      resolved.emotion = msg.emotion;
    }
    else {
      resolved.emotion = ''
    }

    return resolved;
    }
};

module.exports = HeadMotion;
