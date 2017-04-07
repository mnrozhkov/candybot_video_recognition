
"use strict";

let BotSpeechText = require('./BotSpeechText.js');
let MakePhoto = require('./MakePhoto.js');
let MotionPattern = require('./MotionPattern.js');
let Emotion = require('./Emotion.js');
let APIAIBotAnswer = require('./APIAIBotAnswer.js');
let SmileDetected = require('./SmileDetected.js');
let Audio = require('./Audio.js');
let UserSpeechText = require('./UserSpeechText.js');
let FaceCoordinates = require('./FaceCoordinates.js');
let FaceDetected = require('./FaceDetected.js');
let MakeVideo = require('./MakeVideo.js');

module.exports = {
  BotSpeechText: BotSpeechText,
  MakePhoto: MakePhoto,
  MotionPattern: MotionPattern,
  Emotion: Emotion,
  APIAIBotAnswer: APIAIBotAnswer,
  SmileDetected: SmileDetected,
  Audio: Audio,
  UserSpeechText: UserSpeechText,
  FaceCoordinates: FaceCoordinates,
  FaceDetected: FaceDetected,
  MakeVideo: MakeVideo,
};
