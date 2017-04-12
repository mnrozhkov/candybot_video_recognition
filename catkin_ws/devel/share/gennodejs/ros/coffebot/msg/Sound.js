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

class Sound {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.category = null;
      this.name = null;
    }
    else {
      if (initObj.hasOwnProperty('category')) {
        this.category = initObj.category
      }
      else {
        this.category = '';
      }
      if (initObj.hasOwnProperty('name')) {
        this.name = initObj.name
      }
      else {
        this.name = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Sound
    // Serialize message field [category]
    bufferOffset = _serializer.string(obj.category, buffer, bufferOffset);
    // Serialize message field [name]
    bufferOffset = _serializer.string(obj.name, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Sound
    let len;
    let data = new Sound(null);
    // Deserialize message field [category]
    data.category = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [name]
    data.name = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.category.length;
    length += object.name.length;
    return length + 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'coffebot/Sound';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'edd49c676a52b2338bcc9f97439ac87c';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string category
    string name
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Sound(null);
    if (msg.category !== undefined) {
      resolved.category = msg.category;
    }
    else {
      resolved.category = ''
    }

    if (msg.name !== undefined) {
      resolved.name = msg.name;
    }
    else {
      resolved.name = ''
    }

    return resolved;
    }
};

module.exports = Sound;
