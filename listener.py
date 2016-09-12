'''Listens all time and if detects sound records them and sends to module
audio_analyzer'''

import pyaudio
import audioop
import time
import pickle

import subprocess

import argparse
    

def main(format, channels, rate, chunk, min_amplitude):
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
    
    audio = pyaudio.PyAudio()
    stream = audio.open(format=format, channels=channels, rate=rate,
                    input=True, frames_per_buffer=chunk)

    frames = []
    was_speech = False
    start_record_time = 0

    #listening loop
    while True:
        data = stream.read(chunk)           #listens sound
        amplitude = audioop.rms(data, 2)    #and if speech was already
        if amplitude >= min_amplitude:      #record speech until silence
            was_speech = True
            start_record_time = time.time()
        if was_speech:
            frames.append(data)
        if was_speech and (time.time() - start_record_time >= 2):
            frames_file = 'frames.pickle'
            with open(frames_file, 'wb') as file:
                pickle.dump(frames, file)

            #after record initiates subporcess for audio data analyzing
            subprocess.Popen(['python', 'audio_analyzer.py',
                              str(frames_file),
                              str(channels),
                              str(audio.get_sample_size(format)),
                              str(rate)])
            was_speech = False
            frames = []

    stream.stop_stream()
    stream.close()
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
    parser.add_argument(
        '--min_amplitude', dest='min_amplitude', default=4000, type=int)
    args = parser.parse_args()

    main(args.format, args.channels, args.rate, args.chunk, args.min_amplitude)
