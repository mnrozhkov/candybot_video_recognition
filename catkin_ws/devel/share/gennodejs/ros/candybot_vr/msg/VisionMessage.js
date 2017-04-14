// Auto-generated. Do not edit!

// (in-package candybot_vr.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class VisionMessage {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.face_count = null;
      this.smile = null;
    }
    else {
      if (initObj.hasOwnProperty('face_count')) {
        this.face_count = initObj.face_count
      }
      else {
        this.face_count = 0;
      }
      if (initObj.hasOwnProperty('smile')) {
        this.smile = initObj.smile
      }
      else {
        this.smile = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type VisionMessage
    // Serialize message field [face_count]
    bufferOffset = _serializer.int32(obj.face_count, buffer, bufferOffset);
    // Serialize message field [smile]
    bufferOffset = _serializer.bool(obj.smile, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type VisionMessage
    let len;
    let data = new VisionMessage(null);
    // Deserialize message field [face_count]
    data.face_count = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [smile]
    data.smile = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 5;
  }

  static datatype() {
    // Returns string type for a message object
    return 'candybot_vr/VisionMessage';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '38c28f9d3b21cf8ed2fa3008fac27d63';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 face_count
    bool smile
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new VisionMessage(null);
    if (msg.face_count !== undefined) {
      resolved.face_count = msg.face_count;
    }
    else {
      resolved.face_count = 0
    }

    if (msg.smile !== undefined) {
      resolved.smile = msg.smile;
    }
    else {
      resolved.smile = false
    }

    return resolved;
    }
};

module.exports = VisionMessage;
