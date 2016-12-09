// Auto-generated. Do not edit!

// (in-package candybot_vr.msg)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');

//-----------------------------------------------------------

class VisionMessage {
  constructor() {
    this.face_count = 0;
    this.smile = false;
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type VisionMessage
    // Serialize message field [face_count]
    bufferInfo = _serializer.int32(obj.face_count, bufferInfo);
    // Serialize message field [smile]
    bufferInfo = _serializer.bool(obj.smile, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type VisionMessage
    let tmp;
    let len;
    let data = new VisionMessage();
    // Deserialize message field [face_count]
    tmp = _deserializer.int32(buffer);
    data.face_count = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [smile]
    tmp = _deserializer.bool(buffer);
    data.smile = tmp.data;
    buffer = tmp.buffer;
    return {
      data: data,
      buffer: buffer
    }
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

};

module.exports = VisionMessage;
