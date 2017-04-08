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
      this.json_emotions = null;
      this.json_celebrities_similarity = null;
      this.json_gender = null;
      this.json_age = null;
    }
    else {
      if (initObj.hasOwnProperty('json_emotions')) {
        this.json_emotions = initObj.json_emotions
      }
      else {
        this.json_emotions = '';
      }
      if (initObj.hasOwnProperty('json_celebrities_similarity')) {
        this.json_celebrities_similarity = initObj.json_celebrities_similarity
      }
      else {
        this.json_celebrities_similarity = '';
      }
      if (initObj.hasOwnProperty('json_gender')) {
        this.json_gender = initObj.json_gender
      }
      else {
        this.json_gender = '';
      }
      if (initObj.hasOwnProperty('json_age')) {
        this.json_age = initObj.json_age
      }
      else {
        this.json_age = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type FaceFeatures
    // Serialize message field [json_emotions]
    bufferOffset = _serializer.string(obj.json_emotions, buffer, bufferOffset);
    // Serialize message field [json_celebrities_similarity]
    bufferOffset = _serializer.string(obj.json_celebrities_similarity, buffer, bufferOffset);
    // Serialize message field [json_gender]
    bufferOffset = _serializer.string(obj.json_gender, buffer, bufferOffset);
    // Serialize message field [json_age]
    bufferOffset = _serializer.string(obj.json_age, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type FaceFeatures
    let len;
    let data = new FaceFeatures(null);
    // Deserialize message field [json_emotions]
    data.json_emotions = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [json_celebrities_similarity]
    data.json_celebrities_similarity = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [json_gender]
    data.json_gender = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [json_age]
    data.json_age = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.json_emotions.length;
    length += object.json_celebrities_similarity.length;
    length += object.json_gender.length;
    length += object.json_age.length;
    return length + 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'coffebot/FaceFeatures';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '15bb16ee860ec0e7cb55bbcb7c8e05d8';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string json_emotions
    string json_celebrities_similarity
    string json_gender
    string json_age
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new FaceFeatures(null);
    if (msg.json_emotions !== undefined) {
      resolved.json_emotions = msg.json_emotions;
    }
    else {
      resolved.json_emotions = ''
    }

    if (msg.json_celebrities_similarity !== undefined) {
      resolved.json_celebrities_similarity = msg.json_celebrities_similarity;
    }
    else {
      resolved.json_celebrities_similarity = ''
    }

    if (msg.json_gender !== undefined) {
      resolved.json_gender = msg.json_gender;
    }
    else {
      resolved.json_gender = ''
    }

    if (msg.json_age !== undefined) {
      resolved.json_age = msg.json_age;
    }
    else {
      resolved.json_age = ''
    }

    return resolved;
    }
};

module.exports = FaceFeatures;
