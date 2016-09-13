'''Streams audio to the Google Cloud Speech API via GRPC and sends
recognized test to analyzer'''

from __future__ import division

import contextlib
import re
import threading

from gcloud.credentials import get_credentials
from google.cloud.speech.v1beta1 import cloud_speech_pb2 as cloud_speech
from google.rpc import code_pb2
from grpc.beta import implementations
import pyaudio

import audioop
import time

import subprocess

import argparse

# Audio recording parameters
RATE = 16000
CHANNELS = 1
CHUNK = 1024  # 100ms

# Keep the request alive for this many seconds
DEADLINE_SECS = 8 * 60 * 60
SPEECH_SCOPE = 'https://www.googleapis.com/auth/cloud-platform'


audio = None
audio_stream = None


def make_channel(host, port):
    '''Creates an SSL channel with auth credentials from the environment
    Args:
        host: host name
        port: port number
    '''
    
    # In order to make an https call, use an ssl channel with defaults
    ssl_channel = implementations.ssl_channel_credentials(None, None, None)

    # Grab application default credentials from the environment
    creds = get_credentials().create_scoped([SPEECH_SCOPE])
    # Add a plugin to inject the creds into the header
    auth_header = (
        'Authorization',
        'Bearer ' + creds.get_access_token().access_token)
    auth_plugin = implementations.metadata_call_credentials(
        lambda _, cb: cb([auth_header], None),
        name='google_creds')

    # compose the two together for both ssl and google auth
    composite_channel = implementations.composite_channel_credentials(
        ssl_channel, auth_plugin)

    return implementations.secure_channel(host, port, composite_channel)



def request_stream(channels=CHANNELS, rate=RATE, chunk=CHUNK):
    """Yields `StreamingRecognizeRequest`s constructed from a recording audio
    stream.
    Args:
        stop_audio: A threading.Event object stops the recording when set.
        channels: How many audio channels to record.
        rate: The sampling rate in hertz.
        chunk: Buffer audio into chunks of this size before sending to the api.
    """
    # The initial request must contain metadata about the stream, so the
    # server knows how to interpret it.
    recognition_config = cloud_speech.RecognitionConfig(
        # There are a bunch of config options you can specify. See
        # https://goo.gl/A6xv5G for the full list.
        encoding='LINEAR16',  # raw 16-bit signed LE samples
        sample_rate=rate,  # the rate in hertz
        # See
        # https://g.co/cloud/speech/docs/best-practices#language_support
        # for a list of supported languages.
        language_code='ru-RU',  # a BCP-47 language tag
    )
    streaming_config = cloud_speech.StreamingRecognitionConfig(
        config=recognition_config,
    )

    yield cloud_speech.StreamingRecognizeRequest(
        streaming_config=streaming_config)

    start_time = time.time()
    global audio_stream
    
    while time.time() - start_time < 60:
        data = audio_stream.read(chunk)
        if not data:
            raise StopIteration()

        # Subsequent requests can all just have the content
        
        yield cloud_speech.StreamingRecognizeRequest(audio_content=data)


def listen_print_loop(recognize_stream):
    for resp in recognize_stream:
        if resp.error.code != code_pb2.OK:
            raise RuntimeError('Server error: ' + resp.error.message)

        # Display the transcriptions & their alternatives
        for result in resp.results:
            text = result.alternatives[0].transcript
            subprocess.Popen(['python', 'audio_decision.py', text])
            print(text)



def main(format, channels, rate, chunk):
    '''Listens all time. If sound detected records and
    sends data to audio analyzer/

    Args:
        format: raw audio data format, uses pyaudio constant:
                                    pyaudio.paFloat32 = 1
                                    pyaudio.paInt32 = 2
                                    pyaudio.paInt24 = 4
                                    pyaudio.paInt16 = 8
                                    pyaudio.paInt8 = 16
                                    pyaudio.paUInt = 32                            
        channels: audio channels number
        rate: audio rate
        chunk: chunk size
        min_amplitude: minimal sound amplitude equal silence

    Google Speech API recommends to use audio in audio FLAC format
    with channels = 1 and rate >= 16000
    '''

    RATE = rate
    CHANNELS = channels
    CHUNK = chunk
    
    
    global audio
    global audio_stream
    
    audio = pyaudio.PyAudio()
    audio_stream = audio.open(format=format, channels=channels, rate=rate,
                    input=True, frames_per_buffer=chunk)


    #listening loop
    while True:
        
        with cloud_speech.beta_create_Speech_stub(
            make_channel('speech.googleapis.com', 443)) as service:
            try:
                listen_print_loop(
                    service.StreamingRecognize(
                        request_stream(), DEADLINE_SECS))
            except Exception as e:
                print(str(e))

    audio_stream.stop_stream()
    audio_stream.close()
    audio.terminate()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Sets up listening')
    parser.add_argument(
        '--format', dest='format', default=pyaudio.paInt16, type=int)
    parser.add_argument(
        '--channels', dest='channels', default=1, type=int)
    parser.add_argument(
        '--rate', dest='rate', default=16000, type=int)
    parser.add_argument(
        '--chunk', dest='chunk', default=1024, type=int)
    args = parser.parse_args()

    main(args.format, args.channels, args.rate, args.chunk)
