'''
playing audio files
'''

import io
import pyaudio
import wave
import http

import logging
import os
LOG_FOLDER = 'logs'
if os.path.exists(LOG_FOLDER) is False:
    os.mkdir(LOG_FOLDER)

logging.basicConfig(filename=LOG_FOLDER + '/' + __name__ + '.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.DEBUG)

class Player:

    def play_audio(self, audio_data_src: http.client.HTTPResponse or io.BytesIO, format: str='wav') -> None:
        '''
        plays audio_data with format=format
        audio_data: binary audio source
        format: string
        '''
        try:
            if format == 'wav':
                #define stream chunk
                chunk = 1024

                #open a wav format music
                f = wave.Wave_read(audio_data_src)
                #instantiate PyAudio
                p = pyaudio.PyAudio()
                #open stream
                stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                                channels = f.getnchannels(),
                                rate = f.getframerate(),
                                output = True)
                #read data
                data = f.readframes(chunk)

                #play stream
                while data:
                    stream.write(data)
                    data = f.readframes(chunk)

                #stop stream
                stream.stop_stream()
                stream.close()

                #close PyAudio
                p.terminate()
        except Exception as e:
            logging.error(str(e))
