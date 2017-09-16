#!/usr/bin/env python3

from pathlib import Path
TOP = Path(__file__).resolve().parents[1].as_posix()
import sys
sys.path.append(TOP)

from synthesizer import Talker
import json
import time
from utils import audio_format_converter

config = open('speech.config', 'r')
yandex_voice_key = json.load(config)['yandex_voice_key']
config.close()

speech_synthesizer = Talker(yandex_voice_key=yandex_voice_key)

if __name__ == '__main__':
    N = 5
    time_sum = 0.0

    for i in range(N):
        text = 'привет'
        start = time.time()
        wav_data = speech_synthesizer.text_to_speech(text=text)
        time_sum += (time.time() - start)

    with open('test_speech_synthesis_speed.result', 'w') as result:
        result.write('avg_speech_synthesis_time: {0}'.format(time_sum / N))
