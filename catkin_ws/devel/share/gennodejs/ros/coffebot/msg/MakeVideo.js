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

class MakeVideo {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.start_video = null;
      this.duration = null;
      this.video_file_name = null;
    }
    else {
      if (initObj.hasOwnProperty('start_video')) {
        this.start_video = initObj.start_video
      }
      else {
        this.start_video = false;
      }
      if (initObj.hasOwnProperty('duration')) {
        this.duration = initObj.duration
      }
      else {
        this.duration = 0;
      }
      if (initObj.hasOwnProperty('video_file_name')) {
        this.video_file_name = initObj.video_file_name
      }
      else {
        this.video_file_name = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MakeVideo
    // Serialize message field [start_video]
    bufferOffset = _serializer.bool(obj.start_video, buffer, bufferOffset);
    // Serialize message field [duration]
    bufferOffset = _serializer.int8(obj.duration, buffer, bufferOffset);
    // Serialize message field [video_file_name]
    bufferOffset = _serializer.string(obj.video_file_name, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MakeVideo
    let len;
    let data = new MakeVideo(null);
    // Deserialize message field [start_video]
    data.start_video = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [duration]
    data.duration = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [video_file_name]
    data.video_file_name = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.video_file_name.length;
    return length + 6;
  }

  static datatype() {
    // Returns string type for a message object
    return 'coffebot/MakeVideo';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'ea5c471bcc115e3b226da65d49ceb188';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    #message for command to make video
    
    bool start_video
    int8 duration #duration in seconds
    string video_file_name
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new MakeVideo(null);
    if (msg.start_video !== undefined) {
      resolved.start_video = msg.start_video;
    }
    else {
      resolved.start_video = false
    }

    if (msg.duration !== undefined) {
      resolved.duration = msg.duration;
    }
    else {
      resolved.duration = 0
    }

    if (msg.video_file_name !== undefined) {
      resolved.video_file_name = msg.video_file_name;
    }
    else {
      resolved.video_file_name = ''
    }

    return resolved;
    }
};

module.exports = MakeVideo;
