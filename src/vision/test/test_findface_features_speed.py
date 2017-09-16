#!/usr/bin/env python3

from pathlib import Path
TOP = Path(__file__).resolve().parents[1].as_posix()
import sys
sys.path.append(TOP)

from utils import findface
import json
import time

config = open('findface.config', 'r')
findface.token = json.load(config)['findface_token']
config.close()

if __name__ == '__main__':
    img = open('test_findface.png', 'rb').read()

    N = 5
    time_sum = 0.0

    for i in range(N):
        start = time.time()
        result = findface.detect_closest_face(img=img)
        time_sum += (time.time() - start)

    with open('test_findface_features_speed.result', 'w') as out:
        out.write('avg_findface_features_recognition_time: {0}'.format(time_sum / N))
