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

class EyesMotion {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.angle = null;
      this.distance_from_center_percent = null;
      this.emotion = null;
    }
    else {
      if (initObj.hasOwnProperty('angle')) {
        this.angle = initObj.angle
      }
      else {
        this.angle = 0.0;
      }
      if (initObj.hasOwnProperty('distance_from_center_percent')) {
        this.distance_from_center_percent = initObj.distance_from_center_percent
      }
      else {
        this.distance_from_center_percent = 0.0;
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
    // Serializes a message object of type EyesMotion
    // Serialize message field [angle]
    bufferOffset = _serializer.float32(obj.angle, buffer, bufferOffset);
    // Serialize message field [distance_from_center_percent]
    bufferOffset = _serializer.float32(obj.distance_from_center_percent, buffer, bufferOffset);
    // Serialize message field [emotion]
    bufferOffset = _serializer.string(obj.emotion, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type EyesMotion
    let len;
    let data = new EyesMotion(null);
    // Deserialize message field [angle]
    data.angle = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [distance_from_center_percent]
    data.distance_from_center_percent = _deserializer.float32(buffer, bufferOffset);
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
    return 'coffebot/EyesMotion';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '0a9c274e737c0b917a24ecaa2a12792e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 angle # 0.0 <= angle <= 360.0
    float32 distance_from_center_percent # 0.0 <= distance_from_center_percent <= 1.0
    string emotion
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new EyesMotion(null);
    if (msg.angle !== undefined) {
      resolved.angle = msg.angle;
    }
    else {
      resolved.angle = 0.0
    }

    if (msg.distance_from_center_percent !== undefined) {
      resolved.distance_from_center_percent = msg.distance_from_center_percent;
    }
    else {
      resolved.distance_from_center_percent = 0.0
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

module.exports = EyesMotion;
