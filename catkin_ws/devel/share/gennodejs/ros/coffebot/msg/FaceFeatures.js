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

class FaceFeatures {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.emotion = null;
      this.celebrity_name = null;
      this.gender = null;
      this.min_age = null;
      this.max_age = null;
    }
    else {
      if (initObj.hasOwnProperty('emotion')) {
        this.emotion = initObj.emotion
      }
      else {
        this.emotion = '';
      }
      if (initObj.hasOwnProperty('celebrity_name')) {
        this.celebrity_name = initObj.celebrity_name
      }
      else {
        this.celebrity_name = '';
      }
      if (initObj.hasOwnProperty('gender')) {
        this.gender = initObj.gender
      }
      else {
        this.gender = '';
      }
      if (initObj.hasOwnProperty('min_age')) {
        this.min_age = initObj.min_age
      }
      else {
        this.min_age = 0;
      }
      if (initObj.hasOwnProperty('max_age')) {
        this.max_age = initObj.max_age
      }
      else {
        this.max_age = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type FaceFeatures
    // Serialize message field [emotion]
    bufferOffset = _serializer.string(obj.emotion, buffer, bufferOffset);
    // Serialize message field [celebrity_name]
    bufferOffset = _serializer.string(obj.celebrity_name, buffer, bufferOffset);
    // Serialize message field [gender]
    bufferOffset = _serializer.string(obj.gender, buffer, bufferOffset);
    // Serialize message field [min_age]
    bufferOffset = _serializer.int8(obj.min_age, buffer, bufferOffset);
    // Serialize message field [max_age]
    bufferOffset = _serializer.int8(obj.max_age, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type FaceFeatures
    let len;
    let data = new FaceFeatures(null);
    // Deserialize message field [emotion]
    data.emotion = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [celebrity_name]
    data.celebrity_name = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [gender]
    data.gender = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [min_age]
    data.min_age = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [max_age]
    data.max_age = _deserializer.int8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.emotion.length;
    length += object.celebrity_name.length;
    length += object.gender.length;
    return length + 14;
  }

  static datatype() {
    // Returns string type for a message object
    return 'coffebot/FaceFeatures';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '85fb5ab2d65e9fa3f5c71ae7f577d551';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string emotion
    string celebrity_name
    string gender
    int8 min_age
    int8 max_age
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new FaceFeatures(null);
    if (msg.emotion !== undefined) {
      resolved.emotion = msg.emotion;
    }
    else {
      resolved.emotion = ''
    }

    if (msg.celebrity_name !== undefined) {
      resolved.celebrity_name = msg.celebrity_name;
    }
    else {
      resolved.celebrity_name = ''
    }

    if (msg.gender !== undefined) {
      resolved.gender = msg.gender;
    }
    else {
      resolved.gender = ''
    }

    if (msg.min_age !== undefined) {
      resolved.min_age = msg.min_age;
    }
    else {
      resolved.min_age = 0
    }

    if (msg.max_age !== undefined) {
      resolved.max_age = msg.max_age;
    }
    else {
      resolved.max_age = 0
    }

    return resolved;
    }
};

module.exports = FaceFeatures;
