'''Allows read and write audio files'''

import wave
import time

class AudioReader:
    '''Allows read audio files'''
    def __init__(self):
        pass

    def read(self, file, file_format=None):
        pass


class AudioWriter:

    '''Allows write audio files'''

    def __init__(self, audio_frames, channels, sample_size, rate):
        '''Constructor
        Args:
            audio_frames: audio frames list
            channels: audio channels number
            sample_size: format sample size
            rate: audio rate
        '''
        
        self.audio_frames = audio_frames
        self.wave_file_name = str(time.time()) + '.wav'
        self.wave_file = wave.open(self.wave_file_name, 'wb')
        self.wave_file.setnchannels(channels)
        self.wave_file.setsampwidth(sample_size)
        self.wave_file.setframerate(rate)

    def write(self):
        '''Writes audio file'''
        
        self.wave_file.writeframes(b''.join(self.audio_frames))
        self.wave_file.close
        return self.wave_file_name
