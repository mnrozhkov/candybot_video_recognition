#!/usr/bin/env python3

from pathlib import Path
TOP = Path(__file__).resolve().parents[1].as_posix()
import sys
sys.path.append(TOP)

from recorder import Recorder
from recognizer import SpeechRecognizer
import json
import time
from utils import audio_format_converter

config = open('speech.config', 'r')
yandex_voice_key = json.load(config)['yandex_voice_key']
config.close()

audio_recorder = Recorder()
speech_recognizer = SpeechRecognizer(yandex_voice_key=yandex_voice_key)

if __name__ == '__main__':
    N = 5
    time_sum = 0.0

    for i in range(N):
        print('listen')
        raw_audio = audio_recorder.listen_audio()
        wav_data = audio_format_converter.raw_audio2wav(raw_audio)
        start = time.time()
        text = speech_recognizer.recognize_speech(wav_data=wav_data)
        time_sum += (time.time() - start)
        print(text)

    with open('test_speech_recognition_speed.result', 'w') as result:
        result.write('avg_speech_recognition_time: {0}'.format(time_sum / N))
