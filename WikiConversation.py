import pyaudio
import wave
import audioop
import time


import soundfile


import argparse
import base64
import json

from googleapiclient import discovery
import httplib2
from oauth2client.client import GoogleCredentials


import wikipedia


from gtts import gTTS


import pyglet


import sys


FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1024

SPEECH_DISCOVERY_URL = ('https://{api}.googleapis.com/$discovery/rest?'
                 'version={apiVersion}')


#records audio from microphone from first "loud" sound until silence
def record(file_name=None, min_amplitude=500):
    audio = pyaudio.PyAudio()
    was_speech = False #detect first "loud" sound
    silence_count = 0 #counter of chunks with silence
    print ("recording...")
    frames = []
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
    while True:
        data = stream.read(CHUNK) #read next chunk and add it to array
        amplitude = audioop.rms(data, 2)
        print('amplitude=',amplitude)
        if amplitude >= min_amplitude: 
            was_speech = True           #if speech (sounds) was
            silence_count = 0           #wait for "long" silence
        if was_speech:
            frames.append(data)
        if was_speech and amplitude < min_amplitude:
            silence_count +=1
        if silence_count >= 30: #break if detected "long" silence
            break
        
    print("finished recording")
     
    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()
    if file_name is None:
        file_name = str(time.time()) + '.wav'
    waveFile = wave.open(file_name, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
    return file_name


def convert_to_flac(wave_file):
    data, samplerate = soundfile.read(wave_file)
    flac_file = wave_file[:-4] + '.flac'
    soundfile.write(flac_file, data, samplerate)
    print('samplerate=', samplerate)
    return flac_file


def google_speech_connect(flac_file, lang='ru-RU'):
    credentials = GoogleCredentials.get_application_default().create_scoped(
        ['https://www.googleapis.com/auth/cloud-platform'])
    http = httplib2.Http()
    credentials.authorize(http)

    service = discovery.build('speech', 'v1beta1', http=http,
                              discoveryServiceUrl=SPEECH_DISCOVERY_URL)
    with open(flac_file, 'rb') as speech:
        speech_content = base64.b64encode(speech.read())

    service_request = service.speech().syncrecognize(
        body={
            'config': {
                'encoding': 'FLAC',  
                'sampleRate': RATE,  
                'languageCode': lang
            },
            'audio': {
                'content': speech_content.decode('UTF-8')
                }
            })
    response = service_request.execute()
    return response


def get_text(response):
    return response['results'][0]['alternatives'][0]['transcript']


def get_wiki_page(text,lang='ru'):
    wikipedia.set_lang(lang)
    return wikipedia.summary(text)


def tts(wiki_page, lang='ru'):
    gtts = gTTS(wiki_page, lang=lang)
    mp3_file_name = str(time.time()) + '.mp3'
    gtts.save(mp3_file_name)
    return mp3_file_name


def play_mp3(mp3_file):
    player = pyglet.media.Player()
    player.queue(pyglet.media.load(mp3_file))
    player.play()
    #music = pyglet.resource.media(mp3_file)
    #music.play()
    print('Если хотите закончить прослушивание, нажмите q')
    c = sys.stdin.read(1)
    if c == 'q':
        player.delete()


def main():
    play_mp3(tts(get_wiki_page(get_text(google_speech_connect(convert_to_flac(record()))))))

#main()

