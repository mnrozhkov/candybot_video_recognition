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

class MakePhoto {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.make_photo = null;
      this.photo_file_name = null;
    }
    else {
      if (initObj.hasOwnProperty('make_photo')) {
        this.make_photo = initObj.make_photo
      }
      else {
        this.make_photo = false;
      }
      if (initObj.hasOwnProperty('photo_file_name')) {
        this.photo_file_name = initObj.photo_file_name
      }
      else {
        this.photo_file_name = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MakePhoto
    // Serialize message field [make_photo]
    bufferOffset = _serializer.bool(obj.make_photo, buffer, bufferOffset);
    // Serialize message field [photo_file_name]
    bufferOffset = _serializer.string(obj.photo_file_name, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MakePhoto
    let len;
    let data = new MakePhoto(null);
    // Deserialize message field [make_photo]
    data.make_photo = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [photo_file_name]
    data.photo_file_name = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.photo_file_name.length;
    return length + 5;
  }

  static datatype() {
    // Returns string type for a message object
    return 'coffebot/MakePhoto';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'e0d1193fa54b08a2d5ae161d953ba3b1';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    #message for command to make photo
    
    bool make_photo
    string photo_file_name
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new MakePhoto(null);
    if (msg.make_photo !== undefined) {
      resolved.make_photo = msg.make_photo;
    }
    else {
      resolved.make_photo = false
    }

    if (msg.photo_file_name !== undefined) {
      resolved.photo_file_name = msg.photo_file_name;
    }
    else {
      resolved.photo_file_name = ''
    }

    return resolved;
    }
};

module.exports = MakePhoto;
