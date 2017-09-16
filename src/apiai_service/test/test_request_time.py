#!/usr/bin/env python3

from pathlib import Path
TOP = Path(__file__).resolve().parents[1].as_posix()
import sys
sys.path.append(TOP)

from bot_client import APIAIBot
import json
import time

config = open('test_request_time.config', 'r')
bot_client_key = json.load(config)['apiai_client_key']
config.close()
bot = APIAIBot(client_key=bot_client_key)

def request_time():
    msg = 'Здравствуйте'
    start = time.time()
    bot_answer = bot.request(msg=msg)
    return (time.time() - start)


if __name__ == '__main__':

    N = 10
    time_sum = 0.0
    for i in range(N):
        time_sum += request_time()

    with open('test_time_request.result', 'w') as result:
        result.write('avg_request_time: {0}'.format(time_sum / N))
