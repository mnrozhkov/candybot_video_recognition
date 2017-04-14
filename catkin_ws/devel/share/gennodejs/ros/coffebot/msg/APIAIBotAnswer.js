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

class APIAIBotAnswer {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.text = null;
      this.action_name = null;
      this.action_parameters_in_json = null;
    }
    else {
      if (initObj.hasOwnProperty('text')) {
        this.text = initObj.text
      }
      else {
        this.text = '';
      }
      if (initObj.hasOwnProperty('action_name')) {
        this.action_name = initObj.action_name
      }
      else {
        this.action_name = '';
      }
      if (initObj.hasOwnProperty('action_parameters_in_json')) {
        this.action_parameters_in_json = initObj.action_parameters_in_json
      }
      else {
        this.action_parameters_in_json = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type APIAIBotAnswer
    // Serialize message field [text]
    bufferOffset = _serializer.string(obj.text, buffer, bufferOffset);
    // Serialize message field [action_name]
    bufferOffset = _serializer.string(obj.action_name, buffer, bufferOffset);
    // Serialize message field [action_parameters_in_json]
    bufferOffset = _serializer.string(obj.action_parameters_in_json, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type APIAIBotAnswer
    let len;
    let data = new APIAIBotAnswer(null);
    // Deserialize message field [text]
    data.text = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [action_name]
    data.action_name = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [action_parameters_in_json]
    data.action_parameters_in_json = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.text.length;
    length += object.action_name.length;
    length += object.action_parameters_in_json.length;
    return length + 12;
  }

  static datatype() {
    // Returns string type for a message object
    return 'coffebot/APIAIBotAnswer';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd9356e8a4f86a7632a7fb741a0ba9d22';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string text
    string action_name
    string action_parameters_in_json
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new APIAIBotAnswer(null);
    if (msg.text !== undefined) {
      resolved.text = msg.text;
    }
    else {
      resolved.text = ''
    }

    if (msg.action_name !== undefined) {
      resolved.action_name = msg.action_name;
    }
    else {
      resolved.action_name = ''
    }

    if (msg.action_parameters_in_json !== undefined) {
      resolved.action_parameters_in_json = msg.action_parameters_in_json;
    }
    else {
      resolved.action_parameters_in_json = ''
    }

    return resolved;
    }
};

module.exports = APIAIBotAnswer;
