
"use strict";

let BotSpeechText = require('./BotSpeechText.js');
let MakePhoto = require('./MakePhoto.js');
let FaceFeatures = require('./FaceFeatures.js');
let MotionPattern = require('./MotionPattern.js');
let Emotion = require('./Emotion.js');
let APIAIBotAnswer = require('./APIAIBotAnswer.js');
let SmileDetected = require('./SmileDetected.js');
let EyesState = require('./EyesState.js');
let Audio = require('./Audio.js');
let UserSpeechText = require('./UserSpeechText.js');
let FaceCoordinates = require('./FaceCoordinates.js');
let EyesMotion = require('./EyesMotion.js');
let MakeVideo = require('./MakeVideo.js');

module.exports = {
  BotSpeechText: BotSpeechText,
  MakePhoto: MakePhoto,
  FaceFeatures: FaceFeatures,
  MotionPattern: MotionPattern,
  Emotion: Emotion,
  APIAIBotAnswer: APIAIBotAnswer,
  SmileDetected: SmileDetected,
  EyesState: EyesState,
  Audio: Audio,
  UserSpeechText: UserSpeechText,
  FaceCoordinates: FaceCoordinates,
  EyesMotion: EyesMotion,
  MakeVideo: MakeVideo,
};
